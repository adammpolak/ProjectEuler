fibonacci = [1,2] #started with two numbers already for implicity
#fibonacci is an array storing fibonacci numbers
#y is the position in the fibonacci array
y = 0
sum = 2 #started with the sum of the only even number in the current array
while fibonacci[y] + fibonacci[y+1] < 4000000: #while next fibonacci number (progress) is less than <4000000
    progress = fibonacci[y] + fibonacci[y+1]
    fibonacci.append(progress)
    y += 1
    if progress%2==0: #if it is even add it to sum
         sum += progress
flength = len(fibonacci) #the amount of fibonacci numbers <4000000
print flength
print sum 
