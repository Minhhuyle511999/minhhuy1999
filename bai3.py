size = 17
counter = 0
fib = [0] * (size)

for counter in range(0, size - 1 + 1, 1):
    if counter == 0 or counter == 1:
        fib[counter] = counter
    else:
        fib[counter] = fib[counter - 2] + fib[counter - 1]
    print(fib[counter])


