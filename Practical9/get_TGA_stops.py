input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "TGA_genes.fa"
# These two lines assign the names of the input and output files to variables.
# The input file contains the gene sequences in fasta format.
# The output file will contain only the gene sequences that end with TGA, which is a stop codon.
with open(input_file, "r") as input_handle, open(output_file, "w") as output_handle:
    #This line uses the with statement to open both files and assign them to variables.
    # The input file is opened in read mode (“r”) and the output file is opened in write mode (“w”).
    # The with statement ensures that the files are closed automatically after the code block is executed.
    sequence = ""
    gene_name = ""
    # These two lines initialize two empty strings that will store the sequence and the gene name of each gene in the input file.
    for line in input_handle:
    # This line starts a loop that iterates over each line in the input file.
        if line.startswith(">"):
        # This line checks if the current line starts with ">", which indicates that it is a header line that contains the gene name.
            if sequence.endswith("TGA"):
             # This line checks if the previous sequence ends with TGA, which means it is a wanted gene.
                output_handle.write(f">{gene_name}\n{sequence}\n")
                # This line writes the gene name and the sequence to the output file in fasta format.
                # The f-string allows us to insert variables inside curly braces. The "\n" represents a newline character.

            gene_name = line.split()[0][1:]
            # This line assigns the gene name to the variable.
            # It splits the line by whitespace and takes the first element, which is the header.
            # Then it slices off the first character, which is ">", and keeps the rest.
            sequence = ""
            # This line assigns the gene name to the variable.
            # It splits the line by whitespace and takes the first element, which is the header.
            # Then it slices off the first character, which is ">", and keeps the rest.
        else:
        # This else clause executes if the current line does not start with ">", which means it is a sequence line.
            sequence += line.strip()
            # This line adds the current line to the sequence variable after stripping off any whitespace characters from both ends.# This line adds the current line to the sequence variable after stripping off any whitespace characters from both ends
    if sequence.endswith("TGA"): # Check if the last sequence ends with the stop codon
        output_handle.write(f">{gene_name}\n{sequence}\n")
