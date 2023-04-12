seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
start_codon = 'ATG'
stop_codons = ['TGA', 'TAA']

# Initialize a counter for the number of possible coding sequences
count = 1

# Loop through the sequence and check for the start codon
for i in range(len(seq) - 2):
  if seq[i:i+3] == start_codon:
    # If the start codon is found, loop through the rest of the sequence and check for the stop codons
    for j in range(i+3, len(seq) - 2, 3):
      if seq[j:j+3] in stop_codons:
        # If a stop codon is found, increment the counter
        count += 1
        break


# Print the result
print(f'The number of possible coding sequences is {count}.')
