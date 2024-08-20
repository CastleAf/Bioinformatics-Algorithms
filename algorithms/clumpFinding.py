from fasterFrequentWords import computingFrequencies
from numberToPattern import numberToPattern
from patternToNumber import patternToNumber


def clumpFinding(Genome: str, k: int, L: int, t: int) -> set[str]:
    """Find patterns forming clumps in a DNA String.\n
    A k-mer is defined as a "clump" if it appears many times within a short interval
    of the genome. More formally, given integers L and t, a k-mer Pattern forms an
    (L,t)-clump inside a (longer) string Genome if there is an interval of Genome
    of length L in which this k-mer appears at least t times."""

    frequentPatterns: set[str] = set()
    clump = [0] * (4**k)

    # Slide a window through Genome, calculate different clumps that appear
    for i in range(len(Genome) - L + 1):
        text = Genome[i : i + L]
        frequencyArray = computingFrequencies(text, k)

        for j in range(4**k):
            if frequencyArray[j] >= t:
                clump[j] = 1

    for i in range(4**k):
        if clump[i] == 1:
            pattern = numberToPattern(i, k)
            frequentPatterns.add(pattern)

    return frequentPatterns


def betterClumpFinding(Genome: str, k: int, L: int, t: int) -> set[str]:
    """Find patterns forming clumps in a DNA String.\n
    A k-mer is defined as a "clump" if it appears many times within a short interval
    of the genome. More formally, given integers L and t, a k-mer Pattern forms an
    (L,t)-clump inside a (longer) string Genome if there is an interval of Genome
    of length L in which this k-mer appears at least t times."""

    frequentPatterns: set[str] = set()
    clump = [0] * (4**k)

    text = Genome[0:L]
    frequencyArray = computingFrequencies(text, k)

    # Initial update of frequency array
    for i in range(4**k):
        if frequencyArray[i] >= t:
            clump[i] = 1

    # Dynamically keep updating frequency array
    # (decrement first element, increment last element)
    for i in range(len(Genome) - L + 1):
        firstPattern = Genome[i : i + k]
        index = patternToNumber(firstPattern)
        frequencyArray[index] -= 1

        lastPattern = Genome[i + L - k + 1 : i + L + 1]
        index = patternToNumber(lastPattern)
        frequencyArray[index] += 1

        if frequencyArray[index] >= t:
            clump[index] = 1

    for i in range(4**k):
        if clump[i] == 1:
            pattern = numberToPattern(i, k)
            frequentPatterns.add(pattern)

    return frequentPatterns


def main() -> None:

    # Open file
    with open("datasets/clumpFinding.txt", "r") as file:
        genome = file.readline().strip()
        params = file.readline().strip().split()

    # Create output file and write the result
    with open("results/clumpFinding.txt", "w") as output:

        results = betterClumpFinding(
            genome, int(params[0]), int(params[1]), int(params[2])
        )

        for result in results:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()


if __name__ == "__main__":
    main()
