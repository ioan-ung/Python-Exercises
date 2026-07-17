def operations(a, b):
    intersection = []
    union = []
    a_minus_b = []
    b_minus_a = []

    for x in a:
        if x in b and x not in intersection:
            intersection.append(x)

    for x in a:
        if x not in union:
            union.append(x)

    for x in b:
        if x not in union:
            union.append(x)

    for x in a:
        if x not in b:
            a_minus_b.append(x)

    for x in b:
        if x not in a:
            b_minus_a.append(x)

    return intersection, union, a_minus_b, b_minus_a


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(operations(a, b))