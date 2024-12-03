def read_input(filename: str = "input") -> str:
    with open(filename, 'r') as file:
        return file.read()
