#creating 3 diamonds in vertical line using python pattern technique
rows=int(input("Enter the number of rows : "))
repeat=int(input("Enter the number of repetation : "))
for i in range(0,repeat):
    def diamond(rows):
        for i in range(rows):
            print(" "*(rows-i-1)+"* "*(i+1))
        for j in range(rows-1,0,-1):
            print(" "*(rows-j)+"* "*(j))
        print()

    diamond(rows)