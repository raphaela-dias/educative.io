def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    elif n < 0:
        return -1
    result = n * factorial(n-1)
    return result

print(factorial(6))

