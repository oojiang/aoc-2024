from typing import Tuple

def read_input(filename: str="input") -> Tuple[Tuple, Tuple]:
    locks = []
    keys = []
    with open(filename, 'r') as file:
        while True:
            lock_key = [0,0,0,0,0]
            flag = fetch_next_lock_key(file, lock_key)
            if flag == 1:
                locks.append(tuple(lock_key))
            elif flag == -1:
                keys.append(tuple(lock_key))
            else:
                break

    return (locks, keys)

def fetch_next_lock_key(file, lock_key):
    return_val = 0
    line_num = 0
    while (line := file.readline()) not in ['', '\n']:
        if line_num == 0 and line.strip() == '#####':
            return_val = 1
        elif line_num == 6 and line.strip() == '#####':
            return_val = -1
        else:
            for i, c in enumerate(line.strip()):
                lock_key[i] += (c == '#')
        line_num += 1
    return return_val



