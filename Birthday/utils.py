def factorial(n : int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# comb(n, k) = n! / (k! * (n - k)!)
def combinations(n : int, k : int) -> int:
    combination = factorial(n) / (factorial(k) * factorial(n - k))
    return combination

# var(n, k) = n! / (n - k)!
def variations(n : int, k : int) -> int:
    variation = factorial(n) / factorial(n - k)
    return variation