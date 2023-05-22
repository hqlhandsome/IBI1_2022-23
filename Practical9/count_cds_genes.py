stop_codons = input("Input the stop codons（TAA/TAG/TGA）: ")
# This line asks the user to input one of the three stop codons (TAA, TAG or TGA) and assigns it to the variable stop_codons.
# The input function takes a string as an argument and displays it as a prompt.
# The user’s input is returned as a string.

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = f"{stop_codons}_stop_genes.fa"
# These two lines assign the names of the input and output files to variables.
# The input file contains the gene sequences in fasta format.
# The output file will contain only the gene sequences that end with the given stop codon.
# The output file name is constructed using an f-string, which allows us to insert variables inside curly braces.
with open(input_file, "r") as input_handle, open(output_file, "w") as output_handle:
#This line uses the with statement to open both files and assign them to variables.
# The input file is opened in read mode (“r”) and the output file is opened in write mode (“w”).
# The with statement ensures that the files are closed automatically after the code block is executed.
    sequence = ""
    gene_name = ""
    # These two lines initialize two empty strings that will store the sequence and the gene name of each gene in the input file.
    for line in input_handle:
    # These two lines initialize two empty strings that will store the sequence and the gene name of each gene in the input file.
        if line.startswith(">"):
        # This line checks if the current line starts with ">", which indicates that it is a header line that contains the gene name.
            if sequence.endswith(stop_codons):
            # This line checks if the previous sequence ends with the given stop codon, which means it is a gene of interest.
                count = sequence.count(stop_codons)
                # This line counts how many times the stop codon appears in the sequence and assigns it to the variable count.
                # The count method takes a substring as an argument and returns the number of occurrences in the string.
                output_handle.write(f">{gene_name} {count}\n{sequence}\n")
                # This line writes the gene name, the count and the sequence to the output file in fasta format.
                # The f-string allows us to insert variables inside curly braces.
                # The "\n" represents a newline character.
            gene_name = line.split()[0][1:]
            # This line assigns the gene name to the variable.
            # It splits the line by whitespace and takes the first element, which is the header.
            # Then it slices off the first character, which is ">", and keeps the rest.
            sequence = ""
            # This line resets the sequence to an empty string for the next gene.
        else:
        # This else clause executes if the current line does not start with ">", which means it is a sequence line.
            sequence += line.strip()
            # This line adds the current line to the sequence variable after stripping off any whitespace characters from both ends
    if sequence.endswith(stop_codons): # Check if the last sequence ends with the stop codon
        output_handle.write(f">{gene_name}\n{sequence}\n")
