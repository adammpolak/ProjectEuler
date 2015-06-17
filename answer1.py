x = 1								#check is number is divisible by 3 or 5 and add it to sum
sum = 0
while x < 1000:
	if x%3 == 0 or x%5 == 0:
		sum += x
	x+=1
print sum