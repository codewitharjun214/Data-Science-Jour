num = int(input("enter the number"))
if num >= 40 :
    print("pass")

else :
    print("not pass")

#q2

num = int(input("enter the number"))

if num % 3 == 0 and num % 7 == 0 :
    print("multiple of both 3 and 7")

else:
    print("not multiple of both 3 and 7")

#q3

year = int(input("enter the year:"))

if year % 4 == 0:

    # Check if the year is divisible by 100
    if year % 100 == 0:

        # Check if the year is divisible by 400
        if year % 400 == 0:

            # Divisible by 400, it is a leap year
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

#9
char = input("enter the character: ").lower()
vowel = ('a','e','i','o','u')

if char in vowel:
    print("vowel")
else:
    print("not vowel")


#10

age = int(input("enter the age:"))
if age >= 60 :
    print("senior citizen")

else :
    print("not senior citizen")

