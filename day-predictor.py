# Day Finder Program

def find_day(day, month, year):
    # If month is January or February
    if month < 3:
        month = month + 12
        year = year - 1

    k = year % 100
    j = year // 100

    # Zeller's Formula
    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    return days[h]


# Taking input from user
day = int(input("Enter Day: "))
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

result = find_day(day, month, year)
print("The day is:", result)