# WAP where user enter the year the output is that year is leap or not 
year= int(input("Enter the year you want to check if it is leap or not : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")