#creating a pyramid using python pattern technique
n=int(input("Enter the number of rows : "))
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(end=" ")
    for j in range(0,i):
        print("*", end=" ")
    print()