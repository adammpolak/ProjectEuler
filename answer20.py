#input number so can find answer to different numbers
value = input("Will find sum of digits of X!, X=")
product = value 				#this initializes the first number to be multiplied as the given value
sum = 0							#this will be used to sum the digits of the factorial product
for x in range(1,value): 		#goes from 1 to value-1
	product *= value - x 		#multiplies the number until value-x=1
for y in str(product):			#goes through the digits and adds them to sum
	sum += int(y)
print sum