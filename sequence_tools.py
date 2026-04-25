# sequence_tools.py

def gc_content(sequence):
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    total = len(sequence)

    if total == 0:
        return 0

    return ((g + c) / total) * 100


def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        name = None
        seq = []

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if name:
                    sequences[name] = ''.join(seq)
                name = line[1:]
                seq = []
            else:
                seq.append(line)

        if name:
            sequences[name] = ''.join(seq)

    return sequences


def analyze_fasta(file_path):
    sequences = read_fasta(file_path)

    for name, seq in sequences.items():
        gc = gc_content(seq)
        print(f"Sequence: {name}")
        print(f"Length: {len(seq)}")
        print(f"GC Content: {gc:.2f}%")
        print("-" * 30)


if __name__ == "__main__":
    file_path = input("Enter FASTA file path: ")
    analyze_fasta(file_path)
