rows = []														#opens problem18data
f = open('problem18data')										#saves as f
for line in f:													#
	rows.append([int(i) for i in line.split(" ")])

numberofrows = len(rows)										#total amount of rows in the triangle


for y in range(1,len(rows)+1):									#goes through the rows 1-total amount of rows (had to add 1 because range is exclusive)
	currentrow = rows[numberofrows-y]							#this starts with the bottom most row. Then shifts up and ends at 2nd most row
	aboverow = rows[numberofrows-y-1]							#aboverow row is the always one above the current row
	for x in range(0,len(currentrow)-1):						#goes through the amount of elements in the currentrow minus one
		aboverow[x]+= max(currentrow[x:x+2])					#takes 2 array slices of currentrow and adds the higher value to the above row
print rows[0]													#prints the answer