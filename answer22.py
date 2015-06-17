#alphabet that gives the value of each letter
alphabet = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

#opens the text file
f = open('p022_names.txt')

#formats the text file into an array of names
namesarray=f.read().replace('"',"").split(",")


totalsum = 0									#this is the total sum we are looking for
position = 0									#this will be used to find the position in the sorted array of the current name
for x in sorted(namesarray):					#goes through the sorted array word by word
    position += 1 								#finds the position of the current word in the sorted array
    sumofword = 0 								#this is where we will store the score of the name
    for i in x: 								#goes through the word letter by letter
    	sumofword += alphabet[i] 				#finds the value of the letter and adds it to sumof word
    totalsum += sumofword * position 			#multiplies the position of the word against the score
print totalsum 									#prints answer