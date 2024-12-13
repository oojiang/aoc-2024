from data_types import BlockCount, File
from typing import  List

FILE_ID = 0
BLOCK_COUNT = 1

FREE_SPACE = -1

def solution1(disk_map: List[BlockCount]) -> int:
    files = []
    is_free_space = False
    file_id = 0
    for block_count in disk_map:
        if block_count > 0:
            if is_free_space:
                files.append((FREE_SPACE, block_count))
            else:
                files.append((file_id, block_count))
                file_id += 1
        is_free_space = not is_free_space

    moved_files = move_files(files)

    return compute_checksum(moved_files)

def solution2(disk_map: List[BlockCount]) -> int:
    files = []
    is_free_space = False
    file_id = 0
    for block_count in disk_map:
        if block_count > 0:
            if is_free_space:
                files.append((FREE_SPACE, block_count))
            else:
                files.append((file_id, block_count))
                file_id += 1
        is_free_space = not is_free_space

    moved_files = move_files_whole(files)

    return compute_checksum(moved_files)


def move_files(files: List[File]) -> List[File]:
    moved_files = []

    files = list(files)
    while files:
        if files[0][FILE_ID] == FREE_SPACE and files[0][BLOCK_COUNT] == 0:
            files.pop(0)
        elif files[-1][FILE_ID] == FREE_SPACE:
            files.pop(-1)[BLOCK_COUNT]

        elif files[0][FILE_ID] == FREE_SPACE:
            assert files[-1][FILE_ID] != FREE_SPACE

            head_block_count = files[0][BLOCK_COUNT]
            tail_block_count = files[-1][BLOCK_COUNT]
            if head_block_count > tail_block_count:
                files[0] = (FREE_SPACE, head_block_count - tail_block_count)
                moved_files.append(files.pop(-1))
            elif head_block_count < tail_block_count:
                moved_files.append((files[-1][FILE_ID], head_block_count))
                files[-1] = (files[-1][FILE_ID], tail_block_count - head_block_count)
                files.pop(0)
            else:
                files.pop(0)
                moved_files.append(files.pop(-1))

        else:
            assert files[0][FILE_ID] != FREE_SPACE
            moved_files.append(files.pop(0))
            
    return moved_files

def move_files_whole(files: List[File]) -> List[File]:
    moved_files = list(files)

    i = len(moved_files) - 1
    while i > 0:
        i_file_id, i_block_count = moved_files[i]
        if i_file_id != FREE_SPACE:
            for j in range(i):
                j_file_id, j_block_count = moved_files[j]
                if j_file_id == FREE_SPACE and j_block_count >= i_block_count:
                    file = moved_files.pop(i)
                    moved_files.insert(i, (FREE_SPACE, i_block_count))
                     
                    moved_files.pop(j)
                    moved_files.insert(j, (FREE_SPACE, j_block_count - i_block_count))
                    moved_files.insert(j, file)
                    i += 1
                    break
        i -= 1
    return moved_files

def compute_checksum(files: List[File]) -> int:
    checksum = 0
    block_pos = 0
    for file in files:
        checksum += compute_checksum_for_file(file, block_pos)
        block_pos += file[BLOCK_COUNT]
    return checksum

def compute_checksum_for_file(file: File, block_pos: int) -> int:
    file_id, block_count = file
    if file_id == FREE_SPACE:
        return 0
    else:
        return file_id * (block_pos + block_pos + block_count - 1) * (block_count) // 2

def print_files(files: List[File]):
    for file in files:
        for _ in range(file[BLOCK_COUNT]):
            if file[FILE_ID] == FREE_SPACE:
                print('.', end='')
            else:
                print(file[FILE_ID], end='')
    print()


