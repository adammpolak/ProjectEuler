#Generating a triangle number by keeping a counter of what number it is and adding it to the current number
#condition is if amount of 
current = 1                                     #current is the current triangle number being checked for factors, 1 is the first
counter = 2                                     #counter is the number being added current to make the new triangle number being checked
factors = 0                                     #amount of factors that current has
while factors <= 500:
    current += counter                          #add counter to current to make a new triangle number so first check is 3 (1+2)
    counter += 1                                #add 1 to counter to be ready for the next triangle
    x = 1                                       #x wil be used to check if a number is a factor
    factors = 0                                 #number of factors will be set to 0 with each number
    while x*x <= current:                       #will check each number till the square root of current whether it is a factor
        if current%x == 0 and x*x != current:
            factors += 2                        #add two factors because they come in pairs
        elif x*x == current:
            factors += 1                        #a square root only counts as 1 factor
        x+=1                                    #keep adding 1 to check every number whether factor till the square root
print current                                   #adds an extra counter when finished with loop
