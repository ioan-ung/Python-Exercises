def appears_x_times(x, *lists):
    freq = {}

    for lst in lists:
        for elem in set(lst):
            freq[elem] = freq.get(elem, 0) + 1

    return [elem for elem, count in freq.items() if count == x]


print(appears_x_times(
    2,
    [1,2,3],
    [2,3,4],
    [4,5,6],
    [7,1,"test"]
))