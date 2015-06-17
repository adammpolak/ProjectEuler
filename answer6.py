wholesum = 0							#self explanatory
squaresum = 0							#whole sum is added for every number and then squared at the end
x = 0									#square sum is the square of every number
while x < 101:
    wholesum += x
    squaresum += x*x
    x += 1
answer = squaresum - wholesum**2
print answer
