#!/usr/bin/python3

'''
    yield uses for generate a uniqo function,
    it can generate a value step by step
    when running to yield, function will stop, and return the yeild value
    when invoke the function by next() or for loop, function will run continue
    and stop when meet the next yield
'''
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# generate generator
gen = countdown(5)

# get value
print(next(gen))
print(next(gen))
print(next(gen))

# using for loop
for value in gen:
    print(value)

print("---------------------------------")
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)       # generator
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        print("")
        break
