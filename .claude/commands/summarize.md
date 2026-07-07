---
name: summarize
description: Provides a strict 3-sentence summary formatted with (a), (b), and (c).
---

# Summarize Skill

## Purpose
This skill reviews the current session history and outputs a concise three-sentence summary structured strictly in a bulleted skeleton format.

## Process
1. Analyze the current session history (files edited, commands run, questions asked).
2. Generate exactly three sentences covering:
   - **(a) what was accomplished / performed**
   - **(b) what foundational skills or concepts were learned**
   - **(c) what is still open or unfinished**
3. **CRITICAL RULE:** Do NOT print a block of prose. You MUST split the three sentences and print them precisely into the following bulleted format:

- **(a)** [Insert Sentence 1 here]
- **(b)** [Insert Sentence 2 here]
- **(c)** [Insert Sentence 3 here]