#mgoes through the date as a number YYYYMMDD so if want to ask other questions like mondays on the 3rd it will be easy to answer

currentdate = 19010106 							#start on the first sunday of the year, if change what day start on must change counter to 1 day before the first day if 1=monday
numberofsundays = 0 							#counter for amount of sundays on the 1st
counter = 6										#this is the counter that checks what day of the week it is 7 is sunday
while currentdate <= 20010101:					#treat date as a number YYYYMMDD
	counter += 1 								#every iteration increases the day of the week
	year = int(str(currentdate)[:4])			#year is the year as an integer
	month =  int(str(currentdate)[4:6])			#month is month as an integer
	day =  int(str(currentdate)[6:8])			#day is day as an integer
	if counter == 7 and day == 1:				#if it is sunday (7), and first of month, add to counter and reset day of week counter to 0
		numberofsundays += 1
		counter = 0
	elif counter == 7:							#if it is sunday, reset counter back to 0
		counter  = 0
#first go through if end of month or year then lastly just add 1 for every other case

#first go through and check if it is a leap year and it is february 28th, if it is, then go to february 29th
	if (day == 28 and month == 2 and year%4 == 0 and year%100 != 0) or (day ==28 and month == 2 and year%400 ==  0):
		currentdate += 1
#if it is the 29th (in case of leap year) or 28th of february, the date switches to March 1st
	elif (day == 29 and month == 2) or (day == 28 and month ==2):
		currentdate = int(str(currentdate)[:4]+"0301")
#if it is the 30th and it is one of the 4 months that has 30 days, increase the month by 1 and change currentdate
	elif (day == 30 and month == 9) or (day == 30 and month == 4) or (day == 30 and month == 6) or (day == 30 and month == 11):
		month += 1
		if month <10:														#this is to deal with 1 digit or 2 digit months to retain MM formating
			currentdate = int(str(currentdate)[:4]+"0"+str(month)+"01")
		else:
			currentdate = int(str(currentdate)[:4]+str(month)+"01")
#this is to check if it is the end of the year, to increase the year by 1
	elif day == 31 and month ==12:
		year += 1
		currentdate = int(str(year)+"0101")
#if the day is the 31st, increase the month by 1 and change the current date
	elif day == 31:
		month += 1
		if month <10:
			currentdate = int(str(currentdate)[:4]+"0"+str(month)+"01")
		else:
			currentdate = int(str(currentdate)[:4]+str(month)+"01")
#in all other cases just increase the day by 1
	else:
		currentdate += 1
print numberofsundays

