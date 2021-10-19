# Auf Schaltjahr teste :

year = int(input("Enter a year after 1582 to find out if it was a leap year: "))

if year >= 1582 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(year, "was a leap year")

else:
    print(year, "was not leap year")   