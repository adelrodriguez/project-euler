fib = [1, 2]
index = 1
result = 2

while True:
    new_fib = fib[index - 1] + fib[index]

    if new_fib < 4000000:
        if new_fib % 2 == 0:
            result += new_fib

        fib.append(new_fib)

        index += 1
    else:
        break

print(f'The result is: {result}')
