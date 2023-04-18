# Define the DNA sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# Define the start codon
start_codon = 'ATG'
# Define the stop codons
stop_codons = ['TGA', 'TAA', 'TAG']
# Import the re module for regular expressions
import re
# Use re.findall() to find all occurrences of the pattern '^ATG.+TAA' in seq
# This pattern means start with ATG and end with TAA, with any number of characters in between
a=re.findall(r'^ATG.+TAA',seq)
# Use re.findall() to find all occurrences of the pattern '^ATG.+TGA' in seq
# This pattern means start with ATG and end with TGA, with any number of characters in between
b=re.findall(r'^ATG.+TGA',seq)
# Print the sum of the lengths of lists a and b
# This will give the number of matches for both patterns
print(len(a)+len(b))
