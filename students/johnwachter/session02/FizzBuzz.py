#Title: Lab GridPrinterExercise.py
#Change Log: (Who, When, What)
#JWachter, 2019-01-19, created file and function, fizbuzz, to demonstrate 'if' and 'and' statements

def fizbuzz():
    """Return values on a list from 1-100 based on the divisibility of 3 and 5"""
    for i in range(1,100+1):
        if i%3 == 0 and i%5 ==0:
            print("FizzBuzz")
        elif i %3 == 0:
            print("Fizz")
        elif i %5 == 0:
            print("Buzz")
        else:
            print(i)
fizbuzz()
