# Define the amino acid list
amino_acid_list = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'x']
# Define the BLOSUM62 matrix
BLOSUM62 = [
            [ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0],
            [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1],
            [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1],
            [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
            [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2],
            [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0],
            [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2],
            [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1],
            [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1],
            [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1],
            [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
            [ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1],

]
# Define the filenames for the human, mouse and cat ACE2 protein sequences
human = "ACE2_human.fa"
mouse = "ACE2_mouse.fa"
cat = "ACE2_cat.fa"

# Define a function to extract the protein sequence from a file
def extract(filename):
    with open(filename, "r") as f:
        for line in f:
            # Ignore lines that start with '>'
            if not line.startswith('>'):
                # Remove any whitespace and return the sequence
                result = line.strip()
                return result

# Extract the protein sequences for human, mouse and cat
human_seq = extract(human)
mouse_seq = extract(mouse)
cat_seq = extract(cat)

# Initialize a variable to store the edit distance between human and mouse
edit_distance1 = 0
# Loop through each position in the human and mouse sequences
for i in range(len(human_seq)):
    # If the amino acids at this position are different
    if human_seq[i] == mouse_seq[i]:
        # Increment the edit distance by 1
        edit_distance1 += 1
# Calculate and print the percentage of identical amino acids between human and mouse
print('The similarity between mouse and human is',"{:.2%}".format(edit_distance1 / len(human_seq)))

# Initialize a variable to store the edit distance between human and cat
edit_distance2 = 0
# Loop through each position in the human and cat sequences
for i in range(len(human_seq)):
    # If the amino acids at this position are different
    if human_seq[i] == cat_seq[i]:
        # Increment the edit distance by 1
        edit_distance2 += 1
# Calculate and print the percentage of identical amino acids between human and cat
print('The similarity between human and cat is',"{:.2%}".format(edit_distance2 / len(human_seq)))

# Initialize a variable to store the edit distance between mouse and cat
edit_distance3 = 0
# Loop through each position in the mouse and cat sequences
for i in range(len(mouse_seq)):
    # If the amino acids at this position are different
    if mouse_seq[i] == cat_seq[i]:
        # Increment the edit distance by 1
        edit_distance3 += 1
# Calculate and print the percentage of identical amino acids between mouse and cat
print('The similarity between mouse and cat is',"{:.2%}".format(edit_distance3 / len(human_seq)))
def BLOSUM_score(seq1, seq2):
    score = 0
    # Loop through each position in the two sequences
    for i in range(len(seq1)):
        # Find the index of the first amino acid in `amino_acid_list`
        x = amino_acid_list.index(seq1[i])
        # Find the index of the second amino acid in `amino_acid_list`
        y = amino_acid_list.index(seq2[i])
        # Add the BLOSUM score for this pair of amino acids to the total score
        score += BLOSUM62[x][y]
    return score

# Calculate and print the BLOSUM scores between each pair of sequences
score1 = BLOSUM_score(mouse_seq, human_seq)
score2 = BLOSUM_score(mouse_seq, cat_seq)
score3 = BLOSUM_score(human_seq, cat_seq)

print('\n')
print('The score between mouse and human is:', score1)
print('The score between mouse and cat is:', score2)
print('The score between cat and human is:', score3)
