#Program to find fibonnaci series
# n = int(input("Enter the number of terms: "))
# a=0
# b=1
# print("Fibonnaci Series is : ")
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b


# Python program to display the Fibonacci sequence using recursion 
def fibonnaci(n):
   if n <= 1:
       return n
   else:
       return fibonnaci(n-1) + fibonnaci(n-2)
   
n = int (input("Enter the Number for Fibonnaci series : "))
for i in range(n):
       print(fibonnaci(i), end=" ")
   