def my_zip(*lists):
    result = []

    max_len = max(len(lst) for lst in lists)

    for i in range(max_len):
        t = ()

        for lst in lists:
            if i < len(lst):
                t += (lst[i],)
            else:
                t += (None,)
        result.append(t)

    return result