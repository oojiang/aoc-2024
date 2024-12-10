from data_types import AntennaMap

def read_input(filename: str = "input") -> AntennaMap:
    antenna_map = []
    with open(filename, 'r') as file:
        for line in file:
            antenna_map.append(list(line.strip()))
    return antenna_map
