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

abundantnumbers = []									
answer = 0
for x in range(1,28124):
	if sumoffactors(x) > x:
		abundantnumbers.append[x]
#the next line is the "trick". You can do a check if the current number (x) can be made from abundant numbers
#because it will not need the use of any abundant number that is larger than it, in this way you can do it as you go through the numbers
#you go through "y", which is going through every abundant number. This gets subtracted from the current number, and if the result is not in the abundantnumbers array
#then that number cannot be made by 2 abundantnumbers and it is added to the answer
	for y in abundantnumbers:
		if x - y not in abundantnumbers:
			answer += x
print answer