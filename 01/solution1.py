def total_distance(list1: [int], list2: [int]) -> int:
    assert(len(list1) == len(list2))

    # sort the lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    # pair up the elements
    pairs = zip(sorted_list1, sorted_list2)

    # compute the pairwise distances
    distances = map(lambda pair: abs(pair[0] - pair[1]), pairs)

    # sum up the distances
    total_distance = sum(distances)

    return total_distance
