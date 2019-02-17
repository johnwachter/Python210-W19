from os import path
from mailroom4 import createreport
from mailroom4 import displayreport
from mailroom4 import tylettertxt
from mailroom4 import adddonation

testdb = {}

fullpath1 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Me Myself_letter.txt"
fullpath2 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Jeff Bezos_letter.txt"
fullpath3 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Mark Zuckerberg_letter.txt"
fullpath4 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Paul Allen_letter.txt"
fullpath5 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\William Gates, III_letter.txt"

def test_1():
    assert path.exists(fullpath1)
    print("The file ending with {} does exist | Pass".format(fullpath1[-20:]))
    assert path.exists(fullpath2)
    print("The file ending with {} does exist | Pass".format(fullpath2[-20:]))
    assert path.exists(fullpath3)
    print("The file ending with {} does exist | Pass".format(fullpath3[-20:]))
    assert path.exists(fullpath4)
    print("The file ending with {} does exist | Pass".format(fullpath4[-20:]))
    assert path.exists(fullpath5)
    print("The file ending with {} does exist | Pass".format(fullpath5[-20:]))

def test_2():
    assert adddonation("Me Myself", "900", database = testdb) == {"Me Myself":['900']}
    print("passed")

test_1()
test_2()





