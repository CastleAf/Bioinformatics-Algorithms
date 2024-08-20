def patternMatchIndex(pattern: str, dnaString: str) -> list[int]:
    """Finds the indexes where a pattern is identified on a DNA string."""

    indexes = []

    for i in range(len(dnaString) - len(pattern) + 1):
        if dnaString[i : i + len(pattern)] == pattern:
            indexes.append(i)

    return indexes


def main() -> None:

    # Open file
    with open("datasets/patternMatchIndex.txt", "r") as file:
        pattern = file.readline().strip()
        dnaString = file.readline().strip()

    # Create output file and write the result
    with open("results/patternMatchIndex.txt", "w") as output:

        results = patternMatchIndex(pattern, dnaString)

        for result in results:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()


if __name__ == "__main__":
    main()
