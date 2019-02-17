from os import path
from mailroom4 import createreport
from mailroom4 import displayreport
from mailroom4 import tylettertxt
from mailroom4 import adddonation
from mailroom4 import donorlist

test2db = {}
test3db = {}
test4db = {'testdonor': 1}
test5db = {'testdonor': 1, 'testdonor2': 2}

fullpath1 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Me Myself_letter.txt"
fullpath2 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Jeff Bezos_letter.txt"
fullpath3 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Mark Zuckerberg_letter.txt"
fullpath4 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\Paul Allen_letter.txt"
fullpath5 = r"C:\\Users\\John\\Python210-W19\\students\\johnwachter\\mailroom\\William Gates, III_letter.txt"

def test_1():
    """Tests if the files that the function is supposed to create actually exist"""
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
    """Tests if the function that adds donors and amounts to the database works"""
    assert adddonation("Me Myself", "900", database = test2db) == {"Me Myself":['900']}
    print("Test_2 passed")

def test_3():
    """Assert not is used to check if the database is empty"""
    assert not donorlist(test3db)
    print("Test_3 passed")

def test_4():
    """Checks if the donorlist function will return a list of donors that is passed to it"""
    assert donorlist(test4db) == ['testdonor']
    print("Test_4 passed")

def test_5():
    assert donorlist(test5db) == ['testdonor', 'testdonor2']
    print("Test_5 passed")
    
test_1()
test_2()
test_3()
test_4()
test_5()



