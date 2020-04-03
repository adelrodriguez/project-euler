nums = [num for num in range(1000) if num % 3 == 0 or num % 5 == 0]

result = sum(nums)

print(f'The result is: {result}')
