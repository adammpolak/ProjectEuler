array = [0] * 2000000					#if there there is a 1 in the array it implies that it is not a prime number, array represents every number to 2m
sum = 2									#sum of all the prime numbers, started at 3 because counted 2
current = 3								#current number that we are checking, starting with 3
while current < 2000000:				#goes through every number until 2000000 
    if array[current] == 0:				#checks to see if current number has a 0 or 1, 1 means it has a factor that has already been looped through
    	sum += current					#if has 0 means no factor was multiplied to get to this number and so can be added
    	i = current						#takes this number and adds it over and over to itself and switches the numbers in the array to 1, because they are not primes because that number is a factor
    	while i < 2000000:
    		array[i] = 1
    		i += current
    current += 2
print sum