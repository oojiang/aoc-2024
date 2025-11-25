def find_triplets(connections):
    computers = set()
    adjacency = {}
    for comp0, comp1 in connections:
        adjacency[comp0] = adjacency.get(comp0, set())
        adjacency[comp1] = adjacency.get(comp1, set())
        adjacency[comp0].add(comp1)
        adjacency[comp1].add(comp0)

        computers.add(comp0)
        computers.add(comp1)

    comp_list = list(computers)
    triplets = set()
    for i in range(len(comp_list)):
        for j in range(i + 1, len(comp_list)):
            comp0 = comp_list[i]
            comp1 = comp_list[j]
            if comp1 in adjacency[comp0]:
                comp2s = adjacency[comp0].intersection(adjacency[comp1])
                for comp2 in comp2s:
                    triplets.add(tuple(sorted([comp0, comp1, comp2])))

    return triplets

def filter_for_chief(triplets):
    return set(filter(
        lambda triplet: any(comp[0] == 't' for comp in triplet),
        triplets
    ))
