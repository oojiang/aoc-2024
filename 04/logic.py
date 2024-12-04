from typing import List

DIRECTIONS = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
)

XMAS = "XMAS";

def count_xmas(wordsearch: List[List[str]]) -> int:
    num_rows = len(wordsearch)
    num_cols = len(wordsearch[0])


    valid = {
        'X': [[[True for _ in range(len(DIRECTIONS))] for _ in range(num_cols)] for _ in range(num_rows)],
        'M': [[[False for _ in range(len(DIRECTIONS))] for _ in range(num_cols)] for _ in range(num_rows)],
        'A': [[[False for _ in range(len(DIRECTIONS))] for _ in range(num_cols)] for _ in range(num_rows)],
        'S': [[[False for _ in range(len(DIRECTIONS))] for _ in range(num_cols)] for _ in range(num_rows)],
    }

    def set_valid(i, r, c):
        if not wordsearch[r][c] == XMAS[i]:
            return
        for d in range(len(DIRECTIONS)):
            dx, dy = DIRECTIONS[d]
            if num_rows > r + dx >= 0 and num_cols > c + dy >= 0:
                if wordsearch[r + dx][c + dy] == XMAS[i-1]:
                    if valid[XMAS[i-1]][r + dx][c + dy][d]:
                        valid[XMAS[i]][r][c][d] = True

    for i in range(1, len(XMAS)):
        for r in range(num_rows):
            for c in range(num_cols):
                set_valid(i, r, c)

    total_valid = 0
    for r in range(num_rows):
        for c in range(num_cols):
            total_valid += sum(valid['S'][r][c])

    return total_valid

X_MAS_DIRECTIONS = (
    (
        (-1, -1),
        ( 1,  1),
    ),
    (
        (-1,  1),
        ( 1, -1),
    ),
)

def count_x_mas(wordsearch: List[List[str]]) -> int:
    num_rows = len(wordsearch)
    num_cols = len(wordsearch[0])

    total = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if wordsearch[r][c] == 'A':
                count = 0
                for directions in X_MAS_DIRECTIONS:
                    ms_count = {}
                    for dx, dy in directions:
                        if num_rows > r + dx >= 0 and num_cols > c + dy >= 0:
                            if wordsearch[r+dx][c+dy] not in ms_count:
                                ms_count[wordsearch[r+dx][c+dy]] = 0
                            ms_count[wordsearch[r+dx][c+dy]] += 1
                    if 'M' in ms_count and 'S' in ms_count:
                        if ms_count['M'] == 1 and ms_count['S'] == 1:
                            count += 1
                if count == 2:
                    total += 1
    return total
