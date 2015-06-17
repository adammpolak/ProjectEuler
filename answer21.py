
#this function finds the sum of all the proper factors of value
def sumoffactors(value):
	x= 2												#start with 2 to check if it is a factor
	factorssum=0										#this is where we save the sum of the factors
	while x*x <= value:
		if value%x == 0 and x*x != value:				#add the total of the factor pair to the sum
			factorssum += x + (value/x) 
		elif x*x == value:								#add only 1 number if it is a square root
			factorssum += x
		x += 1
	return(factorssum+1)								#add 1 because 1 is included but the actual number is not

current = 3
answer = 0
while current < 10000:									#checks that they are amicable numbers, prime numbers don't count, and that numbers like 6 don't count
	if (sumoffactors(sumoffactors(current))==current != 1) and sumoffactors(current) != sumoffactors(sumoffactors(current)):
		answer += current
	current += 1
print answer