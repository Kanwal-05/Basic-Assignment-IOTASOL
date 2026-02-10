#creating 4 pyramids in a line using python pattern techniques
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