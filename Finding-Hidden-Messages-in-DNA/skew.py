def skew(Genome: str) -> list[int]:
    """Computes a list describing the skew diagram, which indicates the concentration
    of #G - #C throughout the genome."""

    skewResult = [0]

    for i in range(len(Genome)):
        if Genome[i] == "G":
            skewResult.append(skewResult[i] + 1)
        elif Genome[i] == "C":
            skewResult.append(skewResult[i] - 1)
        else:
            skewResult.append(skewResult[i])

    return skewResult


def minimumSkew(dnaString: str) -> list[int]:
    """Computes the indexes where the skew diagram attains a minimum."""

    skewList = skew(dnaString)
    minimumValue = min(skewList)
    minimumIndexes = []

    for i in range(len(dnaString)):
        if skewList[i] == minimumValue:
            minimumIndexes.append(i)

    return minimumIndexes


def main() -> None:

    # Open file
    with open("datasets/skew.txt", "r") as file:
        dnaString = file.read().strip()

    # Create output file and write the result
    with open("results/skew.txt", "w") as output:
        results = minimumSkew(dnaString)

        for result in results:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()


if __name__ == "__main__":
    main()
