from patternCount import patternCount


def frequentWords(text: str, k: int) -> set:
    """Finds the most frequent k-mers on a string."""

    count = []
    frequentWords = set()

    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        count.append(patternCount(text, pattern))

    maxCount = max(count)
    for i in range(len(text) - k + 1):
        if count[i] == maxCount:
            frequentWords.add(text[i : i + k])

    return frequentWords


def main() -> None:

    input = "ACGTTTCACGTTTTACGG"
    k = 3

    print(frequentWords(input, k))


if __name__ == "__main__":
    main()
