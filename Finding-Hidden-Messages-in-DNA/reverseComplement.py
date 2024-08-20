def reverseComplement(dnaString: str) -> str:
    """Calculates and returns the complementary strand of a DNA string."""

    substitutionDict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    complement = []

    for base in dnaString:
        complement.append(substitutionDict[base])

    return "".join(complement[::-1])


def main() -> None:

    print(reverseComplement("AGTCGCATAGT"))

    # Open file
    with open("datasets/reverseComplement.txt", "r") as file:
        dnaString = file.read().strip()

    # Create output file and write the result
    with open("results/reverseComplement.txt", "w") as output:
        output.write(reverseComplement(dnaString))


if __name__ == "__main__":
    main()
