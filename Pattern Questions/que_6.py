#printing the diamonds in vertical line
rows=int(input("Enter the rows : "))
repeat=int(input("Enter the repetation : "))
for i in range(rows):
    for s in range(rows-i-1):
        print(" ",end="")
    for d in range(repeat):
        for star in range(i+1):
            print("* ", end="")
        for space in range((rows-i-1)*2):
            print(" ",end="")
    print()

#below is the same code i pasted for downward pyramid , just change only (range(rows-2,-1,-1)) 

for i in range(rows-2,-1,-1):
    for s in range(rows-i-1):
        print(" ",end="")
    for d in range(repeat):
        for star in range(i+1):
            print("* ", end="")
        for space in range((rows-i-1)*2):
            print(" ",end="")
    print()
    