#Write a program to show the calendar of week requested.
import calendar
year= int(input("Enter the year : "))
month= int(input("Enter the Month : "))
week= int(input("Enter the week : "))
result= calendar.monthcalendar(year, month)[week-1]
print(result)