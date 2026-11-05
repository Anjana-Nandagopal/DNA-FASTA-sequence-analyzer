# DNA FASTA sequence analyzer
A Python project to analyse DNA sequences in FASTA format
# DNA FASTA Sequence Analyser

## About
This is a beginner Python project developed to
practise basic bioinformatics and DNA sequence
analysis. 

The program reads DNA sequences in FASTA format
and calculates basic sequence statistics.


## What I Learned : -

While developing this project, I practised the following Python concepts:
File handling: Reading DNA sequences from an external FASTA file.
Functions: Dividing the program into smaller functions such as read_fasta() and analyse_sequence().
Dictionaries: Storing multiple sequences using their FASTA headers as identifiers.
Loops: Going through sequences and counting individual nucleotides.
Conditional statements: Checking whether a nucleotide is valid or invalid.
String methods: Using methods such as strip(), upper(), startswith() and count().
Lists: Storing invalid characters found in a sequence.
Basic calculations: Calculating sequence length and GC percentage.

The concepts used in this project were explored through introductory bioinformatics learning materials and documentation.

NCBI – FASTA Format for Nucleotide Sequences – Understanding the structure of FASTA files and sequence identifiers.

UC San Diego – Biology Meets Programming: Bioinformatics for Beginners – Introductory bioinformatics concepts and sequence analysis.

Python Documentation – Reference for Python syntax and built-in functions.

## Features
- Reads multiple DNA sequences from a FASTA file
- Calculates sequence length
- Counts A, T, G and C nucleotides
- Calculates GC percentage
- Identifies invalid characters
- Displays sequence validity

## Requirements
- Python 3

## How to Run

1. Download the repository.
2. Open the project folder in Terminal.
3. Run:

python3 fasta_analyser.py

4. Enter the FASTA filename when prompted.

## Limitations
Currently, the program accepts only A, T, G
and C. IUPAC ambiguity codes are not supported.

## Language
Python
