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
- Converted SAM to BAM, then in makegff.py extracted only the 5' end coordinate (keeping only the + strand) and visualized the result in MetaScope.

### Broke / Struggled
- The reference FASTA and the chipexo.gff had different genome names, so MetaScope treated them as two different genomes; fixed by making the names match.
- Writing and verifying makegff.py (the BAM-to-GFF conversion needed for MetaScope) took a while.

### Learned
- Learned the different genome file formats and why each one exists.
- Deeply realized how much the lab's own MetaScope visualization tool eases analysis of experimental results.

---
