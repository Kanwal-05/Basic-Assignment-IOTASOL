# PASCAL TRIANGLE USING RECURSION
def pascal(n,r):
    if r==0 or r==n:
        return 1
    return pascal(n-1,r-1)+pascal(n-1,r)

rows=int(input("enter the number of rows : "))
for i in range(rows):
    for space in range(rows-i):
        print("",end=" ")
    for j in range(i+1):
        print(pascal(i,j), end=" ")
    print()