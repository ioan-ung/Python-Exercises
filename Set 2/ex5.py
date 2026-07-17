from itertools import combinations

def get_combinations(x, k):
    return list(combinations(x, k))

x = [1, 2, 3, 4]
print(get_combinations(x, 3))