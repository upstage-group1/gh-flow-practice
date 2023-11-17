for i in range(1, 30 + 1):
    result = 'fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0)
    print(result if result else i)

