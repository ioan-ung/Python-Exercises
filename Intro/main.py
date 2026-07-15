def ex1():
    name = "Ioan"
    age = 20
    print(f"Hello, I am {name} and I am {age} years old!")

def ex2(a, b, c):
    return a + b + c

def ex3(a, b, c):
    return (a ** b) ** (1 / c)

def ex4(a, b, c):
    mean = (a + b + c) / 3
    geo = (a * b * c) ** (1 / 3)
    return mean, geo

def ex5():
    return len(str(2 ** 1024))

def ex6(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m

def ex7(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y

def ex8(n):
    s = str(n)
    return s == s[::-1]

def ex9(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def ex10(lst):
    for e in lst:
        print(e)

def ex11(lst):
    mn, mx = min(lst), max(lst)
    mean = (mn + mx) / 2
    geo = (mn * mx) ** 0.5
    return mean, geo

def ex12(lst):
    h = len(lst) // 2
    return max(lst[:h]), min(lst[h:])

def ex13(lst):
    return [n for n in lst if ex8(n) and len(str(abs(n))) % 2 == 0]

def ex14(lst):
    i = lst.index(min(lst))
    j = lst.index(max(lst))
    if i <= j:
        return lst[i:j + 1]
    return lst[j:i + 1]

def ex15(matrix):
    diag = [matrix[i][i] for i in range(len(matrix))]
    return sorted(diag, reverse=True)


def menu():
    while True:
        print("\n--- Menu (0 to exit) ---")
        choice = input("Choose exercise (1-15): ")
        match choice:
            case "0":
                break
            case "1":
                ex1()
            case "2":
                print(ex2(1, 2, 3))
            case "3":
                print(ex3(2, 4, 2))
            case "4":
                print(ex4(2, 4, 8))
            case "5":
                print(ex5())
            case "6":
                print(ex6(3, 9, 5))
            case "7":
                print(ex7(6, 3, "*"))
            case "8":
                print(ex8(121))
            case "9":
                print(ex9(17))
            case "10":
                ex10([1, 2, 3])
            case "11":
                print(ex11([4, 1, 9, 2]))
            case "12":
                print(ex12([3, 7, 1, 9, 2, 5]))
            case "13":
                print(ex13([11, 22, 121, 3443, 5]))
            case "14":
                print(ex14([3, 8, 1, 6, 9, 2]))
            case "15":
                print(ex15([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
            case _:
                print("Invalid choice.")

menu()