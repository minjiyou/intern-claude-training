## Session — 2026-07-07

### Done
- Learned how to use Claude Code.

### Broke / Struggled
- Realized that even though Claude Code is AI, you need to write precise prompts/instructions to get the output you actually want.

### Learned
- Experienced firsthand how much more convenient and comfortable writing code becomes when using Claude Code.

---

## Session — 2026-07-10

### Done
- Learned the content and meaning of each column in a GFF file.
- Learned what preparation is needed to read a GFF file as CSV, and achieved faster bio computations using pandas vectorized operations.

### Broke / Struggled
- Got an error where the file path couldn't be found when using a relative path.
- Realized the importance of setting up an absolute path correctly.

### Learned
- Realized that understanding the basic data structure and analysis of GFF files is fundamental to bioinformatics data analysis.

---

## Session — 2026-07-20

### Done
- Learned how to fetch reference data (reads and genome) from a DB via code and used both files as input to generate a SAM file.
- Learned that Bowtie is a mapping algorithm that rapidly aligns tens of millions of short NGS reads to a reference, producing a SAM file with each read's mapped coordinate, strand, and mapping quality as tab-separated text.
- Converted SAM to BAM, then in makegff.py extracted each read's 5' end coordinate, keeping `+` and `-` strands separate (not discarded), and visualized the result in MetaScope.

### Broke / Struggled
- The reference FASTA and the chipexo.gff had different genome names, so MetaScope treated them as two different genomes; fixed by making the names match.
- Writing and verifying makegff.py (the BAM-to-GFF conversion needed for MetaScope) took a while.

### Learned
- Learned the different genome file formats and why each one exists.
- Deeply realized how much the lab's own MetaScope visualization tool eases analysis of experimental results.

---

## Session — 2026-07-28

### Done
- Read a paper on how FUR binding directly represses or activates iron uptake under three different conditions, and ran several analyses using the paper's data.
- Used the MEME algorithm on all 144 FUR binding sites under iron-replete conditions to find a shared short DNA motif (the fur box): took the midpoint of each ChIP-exo start/end, cut 50bp on each side to build MEME input sequences, and got a significant 24bp motif with a meaningful p-value, confirming the ChIP-exo coordinates correspond to sequences actually recognized by the FUR protein.
- Learned how to parse sequences with Biopython while building the MEME input.
- Integrated three tracks (annotation, rnaseq.gff, fur_sites.gff) in MetaScope to visually confirm whether FUR binding sites are directly repressive.

### Broke / Struggled
- Took some time to understand the logic of the function used for TSS distance analysis.
- Had to think through how to scale the y-axis for rnaseq.gff in MetaScope (e.g., log scaling).

### Learned
- Learned multiple ways to check whether a binding site sits near a TSS, in order to determine if it's at an operator or promoter position — the histogram-based distance analysis was especially clarifying.
- Understood that connecting binding sites to a regulatory mechanism requires integrating RNA-seq with ChIP-exo results, not just the ChIP-exo data alone.

---

## Session — 2026-08-06

### Done
- Implemented the code for the operon-size enrichment hypothesis drafted in Part 2, building the full pipeline to test it.
- Ran the pipeline and checked the visualization results; found that operon size is not skewed toward the size expected by the hypothesis.

### Broke / Struggled
- Expected FUR-regulated operons to be enriched for single-gene operons, but the background distribution actually had more non-single-gene operons than expected.
- Lacked sufficient grounds to judge the result as biologically significant, which was disappointing.

### Learned
- Learned about a database of E. coli transcriptional data and how to compare it against experimental results for analysis.
- Learned the definition and use case of the Mann-Whitney U test, a newly encountered statistical distribution/test.

---

## Session — 2026-08-11

### Done
- Wrote the step-by-step code in Part 4 and defined what each step does.

### Broke / Struggled
- Got a small p-value, so had to re-check the unmapped TUs; rebuilt the mapping logic to catch TUs that could still be mapped, and the p-value dropped after re-mapping.

### Learned
- Learned that choosing which distribution to use, and which visualization/graph type to use, both matter.
- Realized that mapping is especially important in bioinformatics data analysis.

---
