# Program to check for leap year
year = int(input("Enter a year: "))

# Year divisible by 100 --> the year is centuary
# Year divisible by 400 --> the year is a leap year
if (year % 100 == 0) and (year % 400 == 0):
   print ("{0} is a leap year".format(year))

# not divisible by 100 --> not a centuary
# year divisbible by 4 --> leap year
elif (year % 4 == 0) and (year % 100 != 0):
   print ("{0} is a leap year".format(year))
else:
   print ("{0} is not a leap year".format(year))
