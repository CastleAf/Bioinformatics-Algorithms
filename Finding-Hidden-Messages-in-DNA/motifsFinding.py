from mismatches import hammingDistance, neighbours


def motifEnumeration(DnaStrings: str, k: int, d: int) -> set[str]:
    """A bruteforce algorithm. Generates all possible kmer neighbours in a group of dna
    strings and checks which generated kmers are present (with hamming distance up to d)
    in all dna strings."""

    patterns: set[str] = set()
    allKmers: set[str] = set()

    # Generate all possible kmers with hamming distance d for all dna strings
    for dna in DnaStrings.split(" "):
        for i in range(0, len(dna) - k + 1):
            allKmers.update(neighbours(dna[i : i + k], d))

    # Test which kmers are present (with hamming distance up to d) in all dna strings
    for kmer in allKmers:
        isMatch = True

        for dna in DnaStrings.split(" "):
            found = False
            for i in range(0, len(dna) - k + 1):
                if hammingDistance(kmer, dna[i : i + k]) <= d:
                    found = True
                    break

            if not found:
                isMatch = False
                break

        if isMatch:
            patterns.add(kmer)

    return patterns


def main() -> None:

    # Open file
    with open("datasets/motifEnumeration.txt", "r") as file:
        params = file.readline().strip().split()
        dna = file.readline().strip()

    # Create output file and write the result
    with open("results/motifEnumeration.txt", "w") as output:

        results = motifEnumeration(dna, int(params[0]), int(params[1]))

        for result in results:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()


if __name__ == "__main__":
    main()
