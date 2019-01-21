#Title: Lab GridPrinterExercise.py
#Change Log: (Who, When, What)
#JWachter, 1/19/2019, creating fibonacci series

def fibonacci(n):
    """Return the nth value in the fibonacci series, starting with zero index"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
nterms = 8
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        print(fibonacci(i))


def lucas(n):
    """Return the nth value in the Lucas numbers, starting with 2, then 1, then 3, 4, 5....n"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
iterms = 9
if iterms <= 0:
    print("Please enter a positive integer")
else:
    print("Lucas Numbers: ")
for i in range(iterms):
   print(lucas(i))


def sumseries(n, n1=0, n2=1):
    """
    Return the nth value of a list, based on adding the two previous items in the list to get the next item, in a recursive fashion.
    :param n: nth item in the list
    :param n1: 0th value in the list
    :param n2: 1st value in the list
    :return: the value of the nth item in the list
    """
    if n == 0:
        return n1
    elif n == 1:
        return n2
    else:
        return sumseries(n - 1, n1, n2) + sumseries(n - 2, n1, n2)

iterms = 4
if iterms <= 0:
    print("Please enter a positive integer")
else:
    print("Sumseries: ")
for i in range(iterms):
    print(sumseries(i, 2, 1))

