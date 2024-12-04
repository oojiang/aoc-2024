from typing import List

def read_input(filename: str = "input") -> List[List[str]]:
    wordsearch = []
    with open(filename, 'r') as file:
        for line in file:
            wordsearch.append(list(line))
    return wordsearch
