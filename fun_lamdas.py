def increment(n):
    return lambda x : x + n

one = increment(42)
print(one(2))

thiry = increment(100)
print(thiry(30))

