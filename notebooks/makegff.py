import argparse
import math
from collections import Counter

import pysam


def five_prime_counts(bam_path):
    """정렬된 BAM에서 매핑된 read마다 5' end 좌표(1-based)를 strand별로 세어 반환한다."""
    counts = Counter()
    with pysam.AlignmentFile(bam_path, "rb") as bam:
        for read in bam.fetch():
            if read.is_unmapped or read.is_secondary or read.is_supplementary:
                continue

            strand = "-" if read.is_reverse else "+"
            # 5' end: '+' strand는 정렬 시작점, '-' strand는 정렬 끝점.
            # reference_start는 0-based라 +1로 1-based 보정, reference_end는 이미 그 위치와 같다.
            position = read.reference_end if read.is_reverse else read.reference_start + 1

            # [염색체 ID 일치화] annotation GFF는 버전 없는 'NC_000913'을 쓰는데
            # BAM의 reference_name은 fasta 헤더 그대로인 'NC_000913.3'이라, MetaScope에서
            # 서로 다른 chromosome으로 인식돼버린다. 버전 suffix를 잘라 맞춰준다.
            ref_name = read.reference_name.split(".")[0]

            counts[(ref_name, strand, position)] += 1

    return counts


def write_gff(counts, gff_path, log_scale=False):
    """(seqname, strand, position)별 count를 MetaScope용 GFF 한 줄로 기록한다."""
    with open(gff_path, "w") as gff:
        for (seqname, strand, position), count in sorted(
            counts.items(), key=lambda kv: (kv[0][0], kv[0][2], kv[0][1])
        ):
            magnitude = round(math.log2(count + 1), 3) if log_scale else count
            # score 부호로 strand를 표시: '-' strand는 음수로 써서 같은 track 안에서
            # MetaScope가 위(+)/아래(-)로 mirror해서 그리게 한다 (feature 이름은 하나로 통일).
            score = magnitude if strand == "+" else -magnitude
            gff.write(
                f"{seqname}\tmakegff\tfiveprime\t{position}\t{position}\t{score}\t{strand}\t.\tdepth={count}\n"
            )


def main():
    parser = argparse.ArgumentParser(
        description="Convert a sorted BAM into a 5'-end pileup GFF for MetaScope."
    )
    parser.add_argument("bam", help="sorted, indexed BAM file")
    parser.add_argument("gff", help="output GFF path")
    parser.add_argument(
        "--log_scale",
        action="store_true",
        help="score = log2(count+1) instead of the raw read count",
    )
    args = parser.parse_args()

    counts = five_prime_counts(args.bam)
    write_gff(counts, args.gff, log_scale=args.log_scale)


if __name__ == "__main__":
    main()
