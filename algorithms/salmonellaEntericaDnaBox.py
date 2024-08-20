from mismatches import fasterFrequentWordsWithMismatches
from skew import minimumSkew


def main() -> None:

    # Open file (containing Salmonella Enterica genome)
    with open("datasets/skew.txt", "r") as file:
        dnaString = file.read().strip().replace("\n", "")

    # Create output file and write the result
    with open("results/skew.txt", "w") as output:
        results = minimumSkew(dnaString)

        for result in results:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()

    # Result was 3818639 3818641. I'll use 3818640 as the middle point for finding ori.
    # I'll consider a window L = 100 and window of L = 300 on the second test

    # Test 1: L = 100
    text = dnaString[3818640 - 50 : 3818640 + 50]
    print(fasterFrequentWordsWithMismatches(text, 9, 1, True))
    # {'TGCGTGGCA', 'GTGGGGGAT', 'GGCGTGGCG', 'TGGCGTGGC', 'CGTGCGTGG', 'GCGTGGCAG', 'CGTGGCGAA', 'CCTGAGCGG', 'CCTTATCGG', 'CTGGCGTGG', 'CGTGGCAGA', 'GCGTGGCGA', 'GTGCCGGAT', 'GTGCGTGGC'}

    # Test 2: L = 300
    text = dnaString[3818640 - 150 : 3818640 + 150]
    print(fasterFrequentWordsWithMismatches(text, 9, 1, True))
    # {'GCTGGGACA', 'GCTGGGGCT', 'CAACTACCA', 'TGCTGGGGC'}


if __name__ == "__main__":
    main()
