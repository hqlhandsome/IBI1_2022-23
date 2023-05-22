# Define the function to determine if a DNA sequence is protein-coding or not
def is_protein_coding(dna):
  # Convert the dna sequence to upper case
    dna = dna.upper()
  # Find the first start codon ATG
    start = dna.index("ATG")
  # Find the last  stop codon TGA
    try:
        stop = dna.rindex("TGA")
  # If rindex() raises a ValueError exception, print an error message and return (0, "invalid")

    except ValueError:
        print("Error: The DNA sequence does not have a valid stop codon TGA.")
        return (0, "invalid")
  # Calculate the length of the coding region between the start and stop codons
    coding_length = stop - start + 3
  # Check if the coding length is a multiple of 3
    if coding_length % 3 != 0:
    # Print a warning message
        print("Warning: The coding region is not a multiple of 3, it might be wrong.")
  # Calculate the percentage of the coding region in the total sequence
    coding_percentage = coding_length / len(dna) * 100
  # Initialize an empty string for the label
    label = ""
  # If the coding percentage is more than 50%, label it as protein-coding
    if coding_percentage > 50:
        label = "protein-coding"
  # If the coding percentage is less than 10%, label it as non-coding
    elif coding_percentage < 10:
        label = "non-coding"
  # Otherwise, label it as unclear
    else:
        label = "unclear"

      # Return the coding percentage and the label as a tuple
    return (coding_percentage, label)

  # Create an example of calling the function with a sample DNA sequence
dna = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCacTGACTA"
  # Call the function and store the result in a variable
result = is_protein_coding(dna)
  # Print the result in a formatted way
print(f"The DNA sequence {dna} has {result[0]}% of coding region and is {result[1]}.")
dna = input('DNA=')
result = is_protein_coding(dna)
print(f"The DNA sequence {dna} has {result[0]}% of coding region and is {result[1]}.")
