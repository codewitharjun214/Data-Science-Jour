#and Both conditions true #
#or Either condition true #
#not Reverse the result #

a = 5 > 3 and 3 <5
print(a)

#or Either condition true #

a = 5 > 3 and 3 > 5
print(a)


#not Reverse the result #
a = not(5 > 3)
print(a)

#Check if a person aged 22 with 85% marks is eligible for a job
#(age≥21 and marks≥80)

age = int(input("what is your age? "))
marks =int(input("what is your marks? "))
print(age >= 21 and marks >= 80)


#Discount Eligibility: Check if a customer with ₹2500 purchase on a weekend gets
#15% discount (purchase≥2000 or weekend=True)

purchase = int(input("What is your purchase amount? "))
weekend = input("Is it weekend today? (yes/no): ")

print(purchase >= 2000 or weekend == "yes")



#Login System: Validate username="admin" and password="12345" or
#recovery_email=True

username = input("What is your username? ")
password = int(input("What is your password? "))
recovery_email = "admin@gmail.com"
print(username=="admin" and password == 12345 or recovery_email == "admin@gmail.com" )

#Grade Check: Student passes if (attendance≥75 and marks≥40) or
#medical_excuse=True

attendance = int(input("What is your attendance? "))
marks = int(input("What is your marks? "))
excuse = (input("You Have medical excuse? (yes/no):"))
print(attendance >= 75 and marks >= 40 or excuse == "yes" )

#Triangle Validator: Check if sides 7, 10, 5 can form a triangle (sum of any two >
#third)

a = 7
b = 10
c = 5

print(a + b > c and a + c > b and b + c > a)

