#combined the two equations through algebra to make searching for the answer easier

f= 1
g= 1
while f < 1000:
    while g < 1000:
        if 1000000 - 2000*f - 2000*g + 2*f*g == 0:
            answer1 = f
            answer2 = g
        g+=1
    f+=1
    g=f

answer3 = 1000 -answer1 - answer2

print answer1*answer2*answer3

