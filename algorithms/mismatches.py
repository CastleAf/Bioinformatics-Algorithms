from numberToPattern import numberToPattern
from patternToNumber import patternToNumber
from reverseComplement import reverseComplement


def hammingDistance(p: str, q: str) -> int:
    """Computes the hamming distance (number of mismatches) between two
    DNA strings of equal length."""

    mismatches = 0

    if len(p) != len(q):
        raise ValueError(
            "To compute the Hamming Distance both strings must have an equal length."
        )

    for i in range(len(p)):
        if p[i] != q[i]:
            mismatches += 1

    return mismatches


def approximatePatternMatching(pattern: str, dnaString: str, d: int) -> list[int]:
    """Finds the indexes where a similar pattern of maximum Hamming Distance d
    is identified on a DNA string."""

    indexes = []

    for i in range(len(dnaString) - len(pattern) + 1):
        if hammingDistance(dnaString[i : i + len(pattern)], pattern) <= d:
            indexes.append(i)

    return indexes


def approximatePatternCount(pattern: str, dnaString: str, d: int) -> int:
    """Finds the number of times where a similar pattern of maximum
    Hamming Distance d is identified on a DNA string."""

    indexes = approximatePatternMatching(pattern, dnaString, d)
    return len(indexes)


def immediateNeighbours(pattern: str) -> set:
    """Generates the immediate neighbourhood (Hamming distance of 1, i.e., 1 mismatch)
    for a given pattern."""

    nucleotides = {"A", "C", "G", "T"}
    neighbourhood = {pattern}

    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in nucleotides:
            if nucleotide != symbol:
                neighbour = list(pattern)
                neighbour[i] = nucleotide

                # Add to neighbourhood the pattern with the substituted nucleotide
                neighbourhood.add("".join(neighbour))

    return neighbourhood


def neighbours(pattern: str, d: int) -> set:
    """Generates the neighbours of a pattern with a hamming distance of up to d."""

    if d == 0:
        return {pattern}

    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    neighbourhood = set()
    nucleotides = {"A", "C", "G", "T"}
    suffixNeighbours = neighbours(pattern[1:], d)

    for text in suffixNeighbours:
        if hammingDistance(pattern[1:], text) < d:
            for nucleotide in nucleotides:
                neighbourhood.add(nucleotide + text)
        else:
            neighbourhood.add(pattern[0] + text)

    return neighbourhood


def computingFrequenciesWithMismatches(
    text: str, k: int, d: int, reverse: bool = False
) -> list[int]:
    """Computes an array of frequencies considering up to d mismatches for each
    possible kmer combinations. The returning list is sorted lexicographically.
    In case param reverse is True then it will also consider the reverse complements."""

    # Initialize array of zeros
    frequencyArray = [0] * (4**k)

    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        if reverse:
            neighbourhood = neighbours(reverseComplement(pattern), d)
        else:
            neighbourhood = neighbours(pattern, d)

        for approximatePattern in neighbourhood:
            j = patternToNumber(approximatePattern)
            frequencyArray[j] += 1

    return frequencyArray


def fasterFrequentWordsWithMismatches(
    text: str, k: int, d: int, reverse: bool = False
) -> set[str]:
    """Finds the most frequent k-mers with up to d mismatches on a DNA string.
    In case param reverse is True then it will also consider the reverse complements."""

    frequentPatterns = set()
    frequencyArray = computingFrequenciesWithMismatches(text, k, d)

    if reverse:
        complementFrequency = computingFrequenciesWithMismatches(text, k, d, True)
        finalFrequencies = [a + b for a, b in zip(frequencyArray, complementFrequency)]
        frequencyArray = finalFrequencies

    maxCount = max(frequencyArray)

    for i in range(4**k):
        if frequencyArray[i] == maxCount:
            pattern = numberToPattern(i, k)
            frequentPatterns.add(pattern)

    return frequentPatterns


def findingFrequentWordsWithMismatchesBySorting(text: str, k: int, d: int) -> set[str]:
    """Finds the most frequent k-mers (considering patterns with up to d mismatches)
    on a DNA string ."""

    frequentPatterns = set()
    neighbourhoods = []
    index = []
    counts = []

    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        neighbourhoods.append(neighbours(pattern, d))

    # Transforms list of sets into list containing all neighbours
    neighbourhoodArray = [value for subset in neighbourhoods for value in subset]

    for i in range(len(neighbourhoodArray)):
        pattern = neighbourhoodArray[i]
        index.append(patternToNumber(pattern))
        counts.append(1)

    index.sort()

    for i in range(len(neighbourhoodArray) - 1):
        if index[i] == index[i + 1]:
            counts[i + 1] = counts[i] + 1

    maxCount = max(counts)

    for i in range(len(neighbourhoodArray)):
        if counts[i] == maxCount:
            pattern = numberToPattern(index[i], k)
            frequentPatterns.add(pattern)

    return frequentPatterns


def main() -> None:

    # Hamming Distance Test #
    with open("datasets/hammingDistance.txt", "r") as file:
        p = file.readline().strip()
        q = file.readline().strip()

    with open("results/hammingDistance.txt", "w") as output:
        output.write(str(hammingDistance(p, q)))

    # Approximate Pattern Matching Test #
    with open("datasets/approximatePatternMatching.txt", "r") as file:
        pattern = file.readline().strip()
        dna = file.readline().strip()
        distance = int(file.readline().strip())

    with open("results/approximatePatternMatching.txt", "w") as output:
        results = approximatePatternMatching(pattern, dna, distance)

        for result in results:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()

    # Approximate Pattern Count Test #
    with open("datasets/approximatePatternCount.txt", "r") as file:
        pattern = file.readline().strip()
        dna = file.readline().strip()
        distance = int(file.readline().strip())

    with open("results/approximatePatternCount.txt", "w") as output:
        output.write(str(approximatePatternCount(pattern, dna, distance)))

    # Neighbours test
    with open("datasets/neighbours.txt", "r") as file:
        pattern = file.readline().strip()
        distance = int(file.readline().strip())

    with open("results/neighbours.txt", "w") as output:
        res = neighbours(pattern, distance)

        for result in res:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()

    # Faster Frequent Words with Mismatches test
    with open("datasets/fasterFrequentWordsWithMismatches.txt", "r") as file:
        text = file.readline().strip()
        params = file.readline().strip().split()

    with open("results/fasterFrequentWordsWithMismatches.txt", "w") as output:
        output.write(
            str(fasterFrequentWordsWithMismatches(text, int(params[0]), int(params[1])))
        )

    # Faster Frequent Words with Mismatches and Reverse Complement test
    with open("datasets/fasterFrequentWordsWithMismatchesAndReverse.txt", "r") as file:
        text = file.readline().strip()
        params = file.readline().strip().split()

    with open("results/fasterFrequentWordsWithMismatchesAndReverse.txt", "w") as output:
        res = fasterFrequentWordsWithMismatches(
            text, int(params[0]), int(params[1]), True
        )

        for result in res:
            output.write(f"{result} ")

        # Remove the last space
        output.seek(output.tell() - 1)
        output.truncate()


if __name__ == "__main__":
    main()
