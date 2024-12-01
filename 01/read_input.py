def read_input(filename: str = "input"):
    list1 = []
    list2 = []
    with open(filename, 'r') as file:
        for line in file:
            int1, int2 = map(int, line.split())
            list1.append(int1)
            list2.append(int2)
    return list1, list2
