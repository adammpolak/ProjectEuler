full = []                                   #array where all numbers are stored
x= 100                                      #x and y will start at 100 to be 3 digits
y=100
while x < 1000:                             #go through every combination of x and y 
    while y <1000:                          #up to 999 and append to full
        current = x* y                      #results in full being an array of every combination
        full.append(current)
        y+=1
    x+=1
    y=x

z=0                                         
answer = 0                                  #now check to see which is the biggest palindrome number in full
while z < len(full):                        #go through entire array
    current = full[z]                       #current number checking for palindrome
    if str(current) == str(current)[::-1]:  #reverses string and checks if it is equal
        if current > answer:                #checks to see if palindrome is bigger than current answer
            answer = current
    z+=1
print answer
