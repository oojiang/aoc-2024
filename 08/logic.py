import itertools
from typing import List, Tuple, Set, Dict
from data_types import AntennaMap, Coordinate

def solution1(antenna_map: AntennaMap) -> int:
    antennas = get_antennas(antenna_map)
    antinodes = map(get_antinodes_all, antennas)
    unioned_antinodes = set().union(*antinodes)
    filtered_antinodes = filter_antinodes(antenna_map, unioned_antinodes)
    return len(filtered_antinodes)

def get_antennas(antenna_map: AntennaMap) -> List[List[Coordinate]]:
    antenna_groups = {}
    for r in range(len(antenna_map)):
        for c in range(len(antenna_map[0])):
            symbol = antenna_map[r][c]
            if symbol != ".":
                if symbol not in antenna_groups:
                    antenna_groups[symbol] = []
                antenna_groups[symbol].append((r, c))
    return list(antenna_groups.values())

def get_antinodes_all(antennas: List[Coordinate]) -> Set[Coordinate]:
    antinodes = set()
    pairs = itertools.combinations(antennas, 2)
    for antenna1, antenna2 in pairs:
        antinodes.update(get_antinode_pair(antenna1, antenna2))
    return antinodes

def get_antinode_pair(
        antenna1: Coordinate,
        antenna2: Coordinate,
    ) -> Tuple[Coordinate, Coordinate]:
    r1, c1 = antenna1
    r2, c2 = antenna2
    r12, c12 = (r1 - r2, c1 - c2)
    r21, c21 = (r2 - r1, c2 - c1)
    antinode1 = (r1 + r12, c1 + c12)
    antinode2 = (r2 + r21, c2 + c21)
    return antinode1, antinode2
        

def filter_antinodes(antenna_map: AntennaMap, antinodes: Set[Coordinate]) -> Set[Coordinate]:
    return set(filter(lambda antinode: in_bounds(antenna_map, antinode), antinodes))

def in_bounds(antenna_map: AntennaMap, coor: Coordinate) -> bool:
    r, c = coor
    return len(antenna_map) > r >= 0 and len(antenna_map[0]) > c >= 0
