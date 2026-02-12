# Pattern Creation
# 1
# 1 1
# 1 1 2
# 1 1 2 2
# 1 1 2 2 3
# 1 1 2 2 3 3

rows= int(input("Enter the number of Rows : "))

for i in range (1,rows+1):
    for j in range(1,i+1):
        print((j+1)//2, end=" ")   
    print() 
