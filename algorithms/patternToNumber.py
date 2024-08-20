def patternToNumber(pattern: str) -> int:
    """Maps a certain pattern to an index which corresponds to its
    position when ordered lexicographically with all possible nucleotide
    patterns of the same length."""

    lastSymbolVal = {"A": 0, "C": 1, "G": 2, "T": 3}

    if len(pattern) == 0:
        return 0

    symbolVal = lastSymbolVal[pattern[-1]]
    prefix = pattern[:-1]

    return 4 * patternToNumber(prefix) + symbolVal


def main() -> None:

    print(patternToNumber("AGT"))
    print(patternToNumber("ATGCAA"))
    print(patternToNumber("GCGGTAA"))


if __name__ == "__main__":
    main()
