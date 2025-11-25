from collections import deque

def get_computers(connections):
    computers = set()
    for comp0, comp1 in connections:
        computers.add(comp0)
        computers.add(comp1)
    return sorted(computers)


def get_adjacency(connections):
    adjacency = {}
    for comp0, comp1 in connections:
        adjacency[comp0] = adjacency.get(comp0, set())
        adjacency[comp1] = adjacency.get(comp1, set())
        adjacency[comp0].add(comp1)
        adjacency[comp1].add(comp0)

    return adjacency

def find_triplets(connections):
    adjacency = get_adjacency(connections)
    comp_list = get_computers(connections)
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

def max_connected(connections):
    computers = get_computers(connections)
    adjacency = get_adjacency(connections)

    available = set(computers)
    current = set()
    best = set()
    def dfs(comp):
        nonlocal best
        if comp not in available:
            return
        available.remove(comp)

        if all(comp1 in adjacency[comp] for comp1 in current):
            current.add(comp)
            if len(current) > len(best):
                best = set(current)
            for comp2 in adjacency[comp].intersection(available):
                dfs(comp2)
            current.remove(comp)

    for i, comp in enumerate(computers):
        available = set(computers[i:])
        dfs(comp)

    return sorted(best)
