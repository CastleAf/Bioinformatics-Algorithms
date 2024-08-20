from numberToPattern import numberToPattern
from patternToNumber import patternToNumber


def computingFrequencies(text: str, k: int) -> list[int]:
    """Computes an array of frequencies for each possible kmer combinations.
    The returning list is sorted lexicographically."""

    # Initialize array of zeros
    frequencyArray = [0] * (4**k)

    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        j = patternToNumber(pattern)
        frequencyArray[j] += 1

    return frequencyArray


def fasterFrequentWords(text: str, k: int) -> set[str]:
    """Finds the most frequent k-mers on a DNA string."""

    frequentPatterns = set()

    frequencyArray = computingFrequencies(text, k)
    maxCount = max(frequencyArray)

    for i in range(4**k):
        if frequencyArray[i] == maxCount:
            pattern = numberToPattern(i, k)
            frequentPatterns.add(pattern)

    return frequentPatterns


def main() -> None:

    text = "ACGTTTCACGTTTTACGG"
    k = 3

    print(fasterFrequentWords(text, k))

    # Exercise
    fullInput = "CTTGGAAATTCTTGGAAATTTGTGTTAATAATTGCCTGCTGCGATCCGATTGCCTGCTGCGATCCGATTGCCTGCTGTGTTAATAATTGCCTGCTGCGATCCGTGCGATCCGTGCGATCCGCTTGGAAATTATTGCCTGCTGTGTTAATACGCCATCGCGCCATCGATTGCCTGCCTTGGAAATTCGCCATCGTGTGTTAATATGTGTTAATATGTGTTAATAATTGCCTGCATTGCCTGCTGCGATCCGCGCCATCGATTGCCTGCTGCGATCCGCGCCATCGTGTGTTAATATGCGATCCGCGCCATCGCTTGGAAATTCTTGGAAATTCTTGGAAATTCGCCATCGTGTGTTAATATGCGATCCGTGTGTTAATACTTGGAAATTATTGCCTGCCTTGGAAATTTGCGATCCGCTTGGAAATTCGCCATCGATTGCCTGCATTGCCTGCCGCCATCGCTTGGAAATTATTGCCTGCATTGCCTGCTGCGATCCGCTTGGAAATTTGTGTTAATAATTGCCTGCCGCCATCGCTTGGAAATTTGTGTTAATACTTGGAAATTCTTGGAAATTTGTGTTAATATGCGATCCGTGCGATCCGCTTGGAAATTCTTGGAAATTCGCCATCGTGCGATCCGATTGCCTGCCTTGGAAATTATTGCCTGCTGTGTTAATACTTGGAAATTTGCGATCCGTGCGATCCGTGTGTTAATACGCCATCGTGTGTTAATACGCCATCGCGCCATCGCTTGGAAATTCTTGGAAATTCTTGGAAATTTGTGTTAATAATTGCCTGCATTGCCTGCCTTGGAAATTCGCCATCGCTTGGAAATTTGTGTTAATATGCGATCCGTGCGATCCGATTGCCTGCATTGCCTGCCTTGGAAATTATTGCCTGCCTTGGAAATTCTTGGAAATTCGCCATCGCTTGGAAATTCTTGGAAATTTGCGATCCGATTGCCTGC"

    print(fasterFrequentWords(fullInput, 12))


if __name__ == "__main__":
    main()
