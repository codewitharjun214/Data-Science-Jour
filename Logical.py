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

age = (input("what is your age? "))
marks = (input("what is your marks? "))
a = (age > '21' and marks > '80')
print("You are eligible for Job" )

#Discount Eligibility: Check if a customer with ₹2500 purchase on a weekend gets
#15% discount (purchase≥2000 or weekend=True)

