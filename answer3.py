z = 600851475143                        #main number in the problem
factorlist = []                         #array that will store all the factors of z
x = 1                                   #starting number to find if is factor of z

while x*x <= z:                         #until get to square root of z stop looking
    if z%x == 0:                        #if it is a factor
        pair = z/x                      #the complimentary factor is pair
        factorlist.append(x)            #append x
        factorlist.append(pair)         #append pair
    x += 1

answer = 0                              #where the answer will be stored
y=0                                     #y is current position in factorlist
while y < len(factorlist):              #going through factorlist array
    current = factorlist[y]             #current is the factor of z in y position 
    x = 2                               #start to check if current is divisible by 2 to see if prime
    prime = True                        #initially assume that the factor is a prime
    while x*x <= current:               #goes until square root of current
        if current%x == 0:              #checks if current is divisible by x (if prime)
            prime = False               #if it is divisible than prime is set to false
        x += 1                          #if it is not divisible x increases by 1
    if prime == True:                   #once it goes through all of x checks if prime is still true
        if current > answer:            #if current is larger than current answer it is stored
            answer = current
    y += 1                              #goes to the next factor of z
print answer
