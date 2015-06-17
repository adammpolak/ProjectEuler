numberones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8} #number of letters 1-19
numbertens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6} #number of letters 20, 30 40, etc
#hundred has 7 letters
#and has 3 letters

sum = 11 #number of letters in one thousand

for x in range(1,1000):
    numberofdigits = len(str(x)) #can tell if 1,2 or 3 digit number
    xarray = str(x) #puts number into array so can look at digits individually for evaluation
    if numberofdigits == 1: #1-9
        sum += numberones[x]
    elif numberofdigits == 2 and int(xarray[0]) == 1: #10-19
        sum += numberones[x]
    elif numberofdigits == 2: #20-99
        sum += numbertens[int(xarray[0])] + numberones[int(xarray[1])] #looks at first digit then second digit
    elif numberofdigits == 3 and int(xarray[1]) < 2 and x%100 != 0: #three digit number whose last 2 digits <20
        sum += numberones[int(xarray[0])] + 7 + 3 + numberones[int(xarray[1]+xarray[2])]
    elif numberofdigits == 3 and x%100 != 0:
        sum += numberones[int(xarray[0])] + 7 + 3 + numbertens[int(xarray[1])] + numberones[int(xarray[2])]
    elif numberofdigits == 3:
        sum += numberones[int(xarray[0])] + 7

print sum
