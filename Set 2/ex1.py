def generalized_fibonacci(num_terms, n):
    sequence = [0] * (n - 1) + [1]

    while len(sequence) < num_terms:
        sequence.append(sum(sequence[-n:]))

    return sequence[:num_terms]

print(generalized_fibonacci(10, 5))
