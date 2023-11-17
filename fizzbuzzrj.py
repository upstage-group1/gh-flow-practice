for i in range(1,16+1):
	if i%15 == 0:
		print('fizzbuzz')
	elif i%3 == 0 or i%5 == 0:
		print('fizz' if i% 3 == 0 else 'buzz')
	else:
		print(i)
