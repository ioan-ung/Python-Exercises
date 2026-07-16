def evaluate_polynomial(poly, x):
    poly = poly.replace("^", "**")
    poly = poly.replace("x", f"*({x})")

    return eval(poly)


polynomial = "3*x^3 + 5*x^2 - 2*x - 5"

print(evaluate_polynomial(polynomial, 1.2))