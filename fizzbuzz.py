print('fizz')

for i in range(1, 30+1) :
    #print('fizz') if i % 3 == 0 else print(i)
    if i % 3 == 0 or i % 5 == 0 :
        print('fizz' * (i%3==0) + 'buzz' * (i%5==0))
    else :
        print(i)