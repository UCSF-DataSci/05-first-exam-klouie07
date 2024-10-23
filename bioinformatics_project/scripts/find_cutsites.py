import sys

def read_file(filename):
    # Use the original code document and make a single line (also in dna_operations.py)
    # Sets the DNA sequence to variable without whitespace
    dna_sequence = []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                dna_sequence.append(line.strip()) # Append each new line to the list (this assumes that the file has only ONE DNA sequence)
    dna_total = ''.join(dna_sequence) # Combine all sequences to one line

    return dna_total

def find_cutsites(sequence, cutsite):
    # Find all occurrences of cute site in DNA sequence (which should be specified in the command-line argument later)
    # Note: Remember the cutsite will be entered as "XX|XXXX"
    cutsite = str(cutsite.replace('|', ''))  # Remove | from the string text
    cutsite_num = [] # Set up to store WHERE the cutsites would ~be
    num = sequence.find(cutsite) # Use new cut site variable (no pipe) to find matches in sequence
    
    while num != -1:
        cutsite_num.append(num) # Add to list
        num = sequence.find(cutsite, num + 1) # Continue searching past where the last site was found
    
    return cutsite_num

def find_pairs(cutsite_num, min_distance, max_distance):
    # Set pairs based on distances between cuts
    pairs = []
    length = len(cutsite_num) # Maximum iterations

    for i in range(length):
        min_x = cutsite_num[i] + min_distance # Range must be at least this value for cut site gaps
        max_x = cutsite_num[i] + max_distance # Range cannot be over this value for cut site gaps

        for j in range(i + 1, length): 
            # Now iterate through the i value and the next value following to find the difference between the two
            if cutsite_num[j] >= min_x: # Check if falls in minimum
                if cutsite_num[j] > max_x: # Check if second value falls within maximum
                    break  # No fall in range = do not continue
                pairs.append((cutsite_num[i], cutsite_num[j])) # Add pairs to known pairs

    return pairs

def save_summary(cutsite, num_cuts_total, matched_pairs, pair_file, filename):
    # Add cuts to designated file
    try:
        with open(filename, 'w') as f:
            f.write(f"Analyzing cut site: {cutsite}\n")
            f.write(f"Total cut sites found: {num_cuts_total}\n")
            f.write(f"Cut site pairs 80-120 kbp apart: {matched_pairs}\n")
            f.write("All pairs:\n")
            for set, pair in enumerate(pair_file, 1):
                f.write(f"{set}. {pair[0]} - {pair[1]}\n")
        print(f"Summary saved to {filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 3: # Check components are there
        print("Usage: python <~/.../find_cutsites.py> <FASTA_file> <cut_site>")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    cutsite = sys.argv[2]

    if not fasta_file.endswith('.fasta'):
        print(f"Error: '{fasta_file}' was inputted. Please provide a .fasta file.")
        sys.exit(1)

    # Read DNA sequence from .fasta
    dna_sequence = read_file(fasta_file)

    if dna_sequence is None:
        print("Error: No data found. Please check .fasta file.")
        sys.exit(1)

    # Find cut site points
    cut_positions = find_cutsites(dna_sequence, cutsite)
    total_cut_sites = len(cut_positions)

    # Locate pairs within goal range (in this case it is 80,000 to 120,000)
    pairs = find_pairs(cut_positions, 80000, 120000)
    total_pairs = len(pairs)

    # Save results
    save_summary(cutsite, total_cut_sites, total_pairs, pairs, "results/cutsite_summary.txt")

    # Print the results
    print(f"Analyzing cut site: {cutsite}")
    print(f"Total cut sites found: {total_cut_sites}")
    print(f"Cut site pairs 80-120 kbp apart: {total_pairs}")
    print("First 5 pairs:")
    for set, pair in enumerate(pairs[:5], 1):
        print(f"{set}. {pair[0]} - {pair[1]}")

if __name__ == '__main__':
    main()
