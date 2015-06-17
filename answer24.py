#There are 10 different objects to put in order
#if you hold 1 in place there is 9 different objects to order
#if you hold 0 at the first place the total amount of numbers is 9!
#9!= 362880, 9!*2= 725760, 1,000,000-725760=274240 (number must be below 1m)
#so must find the 274240th number where the first number is 2 (because already went through 0 and 1)
#8!=40320, 8!*6 = 241920 (the pattern repeats itself until we get to the difference being 0)
#1000000-725760-241920 = 32320 (the second number must be 7, because you use up the lowest 6 remaining numbers, leaving 7)
#7!=5040, 7!*6 = 30240
#1000000-725760-241920-30240=2080 (3rd number is 8, because use up lowest 6 remaining numbers)
#6!=720, 6!*2=1440
#1000000-725760-241920-30240-1440=640 (4th number is 3, because use up lowest 2 remaining numbers)
#5!=120, 5!*5 = 600
#1000000-725760-241920-30240-1440-600=40 (5th number is 9 use up lowest 5 remaining numbers)
#4!=24
#1000000-725760-241920-30240-1440-600-24=16 (6th number is 1, use up lowest remaining number)
#3!=6, 3!*2=12
#1000000-725760-241920-30240-1440-600-24-12=4 (7th number is 5, use up 2 lowest remaing numbers)
#2!=2, 2!*2=4
#1000000-725760-241920-30240-1440-600-24-12-4=0 (8th number is 4, and it solves it, so it must be the highest number that has a 4 in the 8th place, which is:)
#2783915460
print 2783915460