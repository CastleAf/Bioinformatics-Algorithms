def numberToPattern(index: int, k: int) -> str:
    """Maps an index to a certain pattern based on to its index
    position when ordered lexicographically with all possible nucleotide
    patterns of the same 'k' length."""

    lastSymbol = ["A", "C", "G", "T"]

    if k == 1:
        return lastSymbol[index]

    prefixIndex = index // 4
    remainder = index % 4

    symbol = lastSymbol[remainder]
    prefixPattern = numberToPattern(prefixIndex, k - 1)

    return prefixPattern + symbol


def main() -> None:

    print(numberToPattern(11, 3))
    print(numberToPattern(9904, 7))
    print(numberToPattern(5437, 7))
    print(numberToPattern(5437, 8))


if __name__ == "__main__":
    main()
