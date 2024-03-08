def fib(n):

    if n < 0:
        return -1

    fib_list = [0, 1]

    for i in range (0, n - 2):
        result = fib_list[i] + fib_list [i + 1]
        fib_list.append(result)

    return fib_list[-1]

n = 7
print(fib(n))
