#creating a 3 pyramid in vertical direction using python pattern technique 
n=int(input("Enter the number of rows : "))
repeat=int(input("enter the number of repetation : "))
for rep in range(0,repeat):
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print(end=" ")
        for j in range(0,i):
            print("*", end=" ")
        print()
    print()