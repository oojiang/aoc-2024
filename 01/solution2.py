def similarity_score(list1: [int], list2: [int]) -> int:
    # count the number of appearances of each number in list2
    counts = {}
    for i in list2:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1

    def score(i: int) -> int:
        if i not in counts:
            counts[i] = 0
        return i * counts[i]

    # compute the similarity scores
    scores = map(score, list1)

    # sum the similarity scores
    total_score = sum(scores)

    return total_score
