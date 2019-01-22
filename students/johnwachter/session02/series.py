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


if __name__ == "__main__":
    # run tests to ensure funcs above are working properly
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # run tests on lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test if sumseries function with only the necessary argument == ficonacci series, which should be the case
    assert sumseries(5) == fibonacci(5)

    # test if sumseries function matched lucas. sumeries is called with all three arguments and matches the values in the lucas function, namely that the zero index value == 2 and the first index value == 1
    assert sumseries(5, 2, 1) == lucas(5)

    print("tests passed")

