
# ex first

def countdown(n):
    if n == 0:
        print("Done")
        return
    print(n)
    countdown(n-1)

countdown(10)





# ex second

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1) # n = 5 aahe ani fact(n-1 he starting la 4 hoil nantar 3 hoil nantar 2 hoil nanter 1 hoil)

print(fact(5))



