# TaxaPrune
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes PhyloSeq-compatible OTU and TAX tables and
prunes all taxa whose names contain a user-specified pattern of text.

The plugin takes as input a parameter file of keyword-value pairs:

otu: Input OTU table (input)
tax: Input TAX table (input)
pattern: text pattern (input)
newotu: New OTU table (output)
newtax: New TAX table (output)

Files corresponding to "newotu" and "newtax" will be generated, prefixed
by the user-specified PREFIX.
