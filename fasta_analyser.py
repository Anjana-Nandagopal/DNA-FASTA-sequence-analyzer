
# DNA FASTA Sequence Analyser
# This program reads DNA sequences from a FASTA file
# and calculates some basic sequence statistics.

# Function to read sequences from a FASTA file

def read_fasta(filename):

    sequences = {}
    current_name = ""

    file = open(filename, "r")

    for line in file:

        line = line.strip()

        if line.startswith(">"):
            current_name = line[1:]
            sequences[current_name] = ""

        else:
            if current_name != "":
                sequences[current_name] += line.upper()

    file.close()

    return sequences


# Function to analyse a DNA sequence

def analyse_sequence(sequence):

    length = len(sequence)

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_count = g_count + c_count

    valid_bases = "ATGC"
    invalid_bases = []

    for base in sequence:
        if base not in valid_bases:
            if base not in invalid_bases:
                invalid_bases.append(base)

    total_valid = a_count + t_count + g_count + c_count

    if total_valid > 0:
        gc_percentage = (gc_count / total_valid) * 100
    else:
        gc_percentage = 0

    if len(invalid_bases) == 0 and length > 0:
        status = "Valid"
    else:
        status = "Invalid"

    return length, a_count, t_count, g_count, c_count, gc_percentage, invalid_bases, status


# Main program

print("DNA FASTA SEQUENCE ANALYSER")
print("---------------------------")

filename = input("Enter FASTA filename: ")

sequences = read_fasta(filename)

for name, sequence in sequences.items():

    print("\nSequence ID:", name)
    print("Sequence:", sequence)

    results = analyse_sequence(sequence)

    length = results[0]
    a_count = results[1]
    t_count = results[2]
    g_count = results[3]
    c_count = results[4]
    gc_percentage = results[5]
    invalid_bases = results[6]
    status = results[7]

    print("Sequence length:", length)

    print("A count:", a_count)
    print("T count:", t_count)
    print("G count:", g_count)
    print("C count:", c_count)

    print("GC percentage:", round(gc_percentage, 2), "%")

    if len(invalid_bases) > 0:
        print("Invalid characters:", invalid_bases)
    else:
        print("Invalid characters: None")

    print("Sequence status:", status)

print("\nAnalysis completed!")
