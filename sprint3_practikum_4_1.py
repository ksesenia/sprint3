def fibonacci(n) -> int:
    numbers = [0]*n
    numbers[0] = 0
    yield numbers[0]
    numbers[1] = 1
    yield numbers[1]
    for i in range(2, n):
        numbers[i] = (numbers[i-1] + numbers[i-2])
        yield numbers[i]


sequence = fibonacci(10)
for number in sequence:
    print(number)
