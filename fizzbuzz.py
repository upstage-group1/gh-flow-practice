for i in range(1, 30+1):
    if i % 3 == 0 or i % 5 == 0:
        print('fizzbuzz')

    elif i % 3 == 0:
        print('fizz')

    elif i % 5 == 0:
        print('buzz')

    else:
        print(i)