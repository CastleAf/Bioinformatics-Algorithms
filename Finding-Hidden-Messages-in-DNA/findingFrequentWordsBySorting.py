from numberToPattern import numberToPattern
from patternToNumber import patternToNumber


def findingFrequentWordsBySorting(text: str, k: int) -> set[str]:
    """Finds the most frequent k-mers on a DNA string."""

    frequentPatterns = set()
    index = []
    counts = []

    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        index.append(patternToNumber(pattern))
        counts.append(1)

    # The index list will be sorted
    index.sort()

    for i in range(1, len(text) - k + 1):
        if index[i] == index[i - 1]:
            counts[i] = counts[i - 1] + 1

    maxCount = max(counts)

    for i in range(len(text) - k + 1):
        if counts[i] == maxCount:
            pattern = numberToPattern(index[i], k)
            frequentPatterns.add(pattern)

    return frequentPatterns


def main() -> None:

    text = "ACGTTTCACGTTTTACGG"
    k = 3

    print(findingFrequentWordsBySorting(text, k))
    print(findingFrequentWordsBySorting("AAGCAAAGGTGGG", 2))


if __name__ == "__main__":
    main()
