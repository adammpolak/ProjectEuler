primes = [2,3,5,7,11,13]			#this is the array of all prime numbers not necessary but interesting, included first 6
x=15								#starting with 15 to see if it is a prime number
counter = 6							#total amount of prime numbers currently counted
while counter < 10001:				#this is the counter of total prime numbers found
    z = 3							#first number to check if the x is a prime number, 2 and 1 don't matter
    prime = True					#will assume it is a prime number
    while z*z <= x:					#will check until the square for possible factors
        if x%z == 0:
            prime = False			#if a factor is found prime is no longer true
        z += 2						#continue checking odd numbers until it is the square of x
    if prime == True:				#if found that it is a prime add to the counter
        counter += 1
    x += 2
print x