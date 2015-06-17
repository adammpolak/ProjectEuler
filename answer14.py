#The counter array is the total amount of "moves" needed to reach 1 from that specific number
#The location in the counter array indicates what number is being tracked

counterarray= [0,1,2] + [0]*1000001

#the count will increase for other numbers even when beginning with a different number to
#save computing time. But must make sure no numbers are skipped, so "minimum" is the
#initial number started on the journey.

minimum = 3

#"current" will be the current number in the journey. This will change with every
#operation.

#the hotarray is the current numbers hit on the journey
hotarray = []

answer = 0


while minimum <= 1000000:
    current = minimum
    hotarray.append(current)
    while current != 1:
        if current%2==0:
            current = current/2
            hotarray.append(current)
        else:
            current = current*3 + 1
            hotarray.append(current)

    counterarray[minimum] = len(hotarray)           
    hotarray = []
    minimum += 1


#scan through counter array to find highest count


for i in range(len(counterarray)):
    if counterarray[i] > answer:
        answer = counterarray[i]
        maxIndex = i



print maxIndex