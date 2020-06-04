def fib(number):
    """This comment is the header for the functions documentation 
    
    The first line is a header, than we put a blank line and anything
    in this section is part of the description
    """
    i, j = 1,2
    while i <= number:
        print(i, end=', ')
        i,j = j, i+j
    print()

fib(13)

print(fib.__doc__)

f = fib

f(5)

def buildFib(number):
    result = []
    i, j = 1,2
    while i <= number:
        result.append(i)
        i, j = j, i+j
    return result

fibList = buildFib(121)

print(fibList)