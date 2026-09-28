"""def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            return True
filter1=filter(prime,range(10))
print(list(filter1))
"""
# map()
def square(x):
    return x*x
numbers=[1,2,3,4,5,6,7,8,9,10]
listsquare=map(square,numbers)
print(list(listsquare))