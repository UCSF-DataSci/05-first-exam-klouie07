import random
import sys

def gen_random_dna_sequence(length):
    # Make ramdon DNA sequence using inputted length
    # Return: for x length, append new choice from 'ACGT' to generated sequence
    return ''.join(random.choice('ACGT') for _ in range(length))

def save_file_fasta(sequence, filename):
    # Save DNA sequence to designated file destination
    with open(filename, 'w') as fasta_file: 
        fasta_file.write(">Original" + "\n") # Setting a line header with title
        # To make lines of 80 characters using the sequence
        for i in range(0, len(sequence), 80): # Range is length of sequence, with subsets of 80 as the cutoff
            fasta_file.write(sequence[i:i+80] + '\n') # Translate sequence to file using cutoff numbers as new line commands

def main():
    # The sequence length should be entered with command
    try:
        sequence_length = int(sys.argv[1])
        if sequence_length <= 0:
            raise ValueError("Sequence length must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except IndexError as e:
        print(f"Error: Must enter sequence length to be generated.")
        sys.exit(1)

    # Use fuction to generate random DNA sequence of the inputted length
    random_dna_sequence = gen_random_dna_sequence(sequence_length)

    # Push the output to the data directory (assuming the setup_project was run first and correctly)
    output_file = "data/random_sequence.fasta"

    # Save sequence to file
    save_file_fasta(random_dna_sequence, output_file)

    # Did code run? Confirmation line
    print(f"Random DNA sequence generated and saved to {output_file}")

if __name__ == '__main__':
    # Time to run the file ..
    main()
