def count_unique_pairs(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            count += fits(lock, key)
    return count

def fits(lock, key):
    return all(l + k < 6 for l, k in zip(lock, key))
