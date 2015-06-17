#self explanatory

counter = 1
fibonacci1 = 1
fibonacci2 = 2
while len(str(fibonacci2)) < 1000:
	fibonacci2 += fibonacci1
	fibonacci1 = fibonacci2 - fibonacci1
	counter += 1
print counter+2