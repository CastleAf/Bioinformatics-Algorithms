def patternCount(text: str, pattern: str) -> int:
    """Count the number of times a pattern appears in a text (counting overlaps as well)."""

    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count += 1

    return count


def main() -> None:

    with open("patternCountTest.txt") as file:
        data = file.read().split("\n")

    if len(data) > 1:
        input = data[0]
        patt = data[1]
        print(patternCount(input, patt))

    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()
