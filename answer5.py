x = True					#This will be the switch that stops the counter
y= 20						#start at y=20 for the counter
while x == True:			#keep adding until all the constraints are met only need 10-20 because others are divisible
    y+=20
    if y%20==0 and y%19==0 and y%18==0 and y%17==0 and y%16==0 and y%15==0 and y%14==0 and y%13==0 and y%12==0 and y%11==0:
        x = False 
print y

