import sys

def complement(sequence): # Returns complement of DNA sequence 
    
    # Create dictionary for uppercase and lowercase inputs; make result all capital if not already
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                       'a': 'T', 't': 'A', 'c': 'G', 'g': 'C'}
    
    complement_sequence = []
    
    # For each letter in the DNA sequence, use complement_dict to append to new list what the new value is
    for base in sequence: 
        complement_sequence.append(complement_dict.get(base, base))
    
    return ''.join(complement_sequence) # Make all together one string

def reverse(sequence): # Returns reverse of DNA sequence
    return sequence[::-1] # No join bc alreay in line

def reverse_complement(sequence): # Returns reverse complement of DNA sequence.
    # Stacks the complement (A to T, T to A, etc) and reverse (backwards) sequences
    return reverse(complement(sequence))

def main():
    # Inputs must be python run this code, and the attached fasta file
    try:
        dna_file = len(sys.argv[1])
        if dna_file != 2:
            print("Usage: python <.py file> <FASTA_file>")
    except IndexError as e:
        print(f"Error: {e}. Must specify arg path to .fasta file for analysis.")
        sys.exit(1)

    # Use DNA sequence from command line
    dna_file = sys.argv[1]
    dna_sequence = []
    with open(dna_file, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                dna_sequence.append(line.strip()) # Append each new line to the list (this assumes that the file has only ONE DNA sequence)
    dna_sequence = ''.join(dna_sequence) # Combine all sequences to one line

    # Save original, complement, reverse, and reverse complement sequences to respective variables using the defined functions
    original = dna_sequence
    comp = complement(original)
    rev = reverse(original)
    rev_comp = reverse_complement(original)

    # Print results to terminal
    print(f"Original sequence: {original}")
    print(f"Complement: {comp}")
    print(f"Reverse: {rev}")
    print(f"Reverse complement: {rev_comp}")
        
    # Save results to new FASTA file
    output_fasta_file = f"data/.converted_sequence.fasta"

    try:
        with open(output_fasta_file, 'w') as fasta_file:
            fasta_file.write(">Original" + "\n") # Setting a line header with title
            for i in range(0, len(original), 80): # Setting line breaks to 80 like before
                fasta_file.write(original[i:i+80] + "\n") # Writing in the sequence with line breaks

            fasta_file.write(">Complement" + "\n") # Repeat above for complement DNA
            for i in range(0, len(comp), 80):
                fasta_file.write(comp[i:i+80] + "\n")

            fasta_file.write(">Reverse" + "\n") # Repeat for Reverse
            for i in range(0, len(rev), 80):
                fasta_file.write(rev[i:i+80] + "\n")

            fasta_file.write(">Reverse-Complement" + "\n") # Repeat for reverse complement
            for i in range(0, len(rev_comp), 80):
                fasta_file.write(rev_comp[i:i+80] + "\n")
                
    except Exception as e:
        print(f"Error writing to FASTA file: {e}")

    print(f"Transformed DNA sequences saved to {output_fasta_file}")

if __name__ == '__main__':
    main()
