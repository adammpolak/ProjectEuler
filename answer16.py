#first get result and turn into string
string = str(2**1000)
sum = 0
for digit in string: #converts each character into integer than adds to sum
    sum += int(digit)
print sum

