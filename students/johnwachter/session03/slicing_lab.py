#Title: slicing_lab.py
#Change Log: (Who, When, What)
#JWachter, 2019-01-26, Created File and finished exercise

def swap(string):
    first = string[0]
    last = string[-1]
    mid = string[1:-1]
    newstring = last + mid + first
    return newstring

swapped = swap("string")
print(swapped)
assert swap("flipped") == "dlippef"
print("Test passed")


def remove(tupl):
    newtupl = tupl[0:-1:2]
    print(newtupl)
mytupl = (1,2,3,4,5,6,7,8,9)
remove(mytupl)

def thirds(string):
    thirds = len(string)/3
    first = thirds

string = "string"
thirds = int(len(string)/3)
first = string[0:thirds]
print("first {}".format(first))
last = string[-thirds:]
print("last {}".format(last))
mid = string[thirds:thirds]
print("mid {}".format(mid))
