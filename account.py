balance = 5000
amount = int(input("Enter amount :"))
if amount > balance :
    print("Unsufficient balance ")

else :
    balance -= amount
    print("remaining balance :", balance)
    print("withdraw successful")