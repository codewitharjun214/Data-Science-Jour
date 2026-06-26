"""#if we want to use a thing repeat and repeat then we use for looop

for i in range(1,101):
    print(i)

for i in range(101,0,-1):
    print(i)"""

total = 0
num = 1

while num <= 10:
    total = total + num
    num = num + 1

print("Total sum is:", total)



for i in range(0,10):
    if i == 3 :
        break
    print(i)


for i in range(0,10):
    if i == 3 :
        continue
    print(i)

for i in range(0,10):
    if i == 3 :
        pass 
    print(i)



