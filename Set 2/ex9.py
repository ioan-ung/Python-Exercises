def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[1][2])


lst = [('abc', 'bcd'), ('abc', 'zza')]
print(sort_tuples(lst))