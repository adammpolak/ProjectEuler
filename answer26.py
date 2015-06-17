def isitnotaprime(value):						#this will return a 1 if the number has a factor
	x= 2																	
	while x*x <= value:
		if value%x == 0:				
			return 0
		x += 1

def findperiod(value):							#this is the "hard" part, this finds the length of the period
	current = value								#this is a quick and dirty long division calculation
	modulus = 10								#it repeats and keeps a coutner until it repeats
	counter = 1 								#you can tell when it repeats if moduls becomes 1 (which is how the division starts if you imagine long division)
	while modulus != 1:
		modulus = modulus*10
		modulus = (modulus%current)
		counter += 1
	return counter

biggestperiod = 0
answer = 0
x=10
while x < 1000:									#this goes through the numbers and searches the length of period
	if isitnotaprime(x) != 0 and findperiod(x)>biggestperiod:
		answer = x
		biggestperiod=findperiod(x)
	x+=1
print answer

