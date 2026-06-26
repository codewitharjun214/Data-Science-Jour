"""for i in range(5):
    print(*)

for i in range(5):
    print("*",end="")

n = 5

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))



# Upper pyramid
for i in range(1,6):
    print(" " * (6 - i) + "*" * (2 * i - 1))

# Lower pyramid
for i in range(6,1,-1):
    print(" " * (6 - i) + "*" * (2 * i - 1))

for i in range(1,5):

    n = 5

    for i in range(1, n + 1):
        for j in range(1, n + 2):
            if j == n-i+1 or j == n+i-1 or  i==n:
                print("*",end="")

            else:
                print(" ",end="")
                print()

"""
from numpy.array_api import square

numbers = [ i for i in range(0,10) ]
print(numbers)

square=[ i*i for i in range(0,10) ]
print(square)

even=[i for i in range(0,10) if i % 2 == 0]
print(even)