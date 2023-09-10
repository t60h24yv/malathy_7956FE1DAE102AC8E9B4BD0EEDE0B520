#Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.


year=int(input("Enter a Year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))


elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))