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
print("Swap String")
print(swapped)
assert swap("flipped") == "dlippef"
print("Test passed")
print("="*45)

def remove(tupl):
    newtupl = tupl[0:-1:2]
    return newtupl
mytupl = (1,2,3,4,5,6,7,8,9)
removeditems = remove(mytupl)
print("Remove every other item")
print(removeditems)
assert remove("123456789") == "1357"
asserttupltest = (1, 2, 3, 4)
assert remove(asserttupltest) == (1, 3)
print("Tests passed")
print("="*45)

def remove4everyother(string):
    return string[4:-4:2]
everyother4 = (1,2,3,4,5,'dontshow','show', 'dontshow', 'show', 6,7,8,9)
print("first 4 and the last 4 items removed, and then every other item in the remaining sequence")
print(remove4everyother(everyother4))
assert remove4everyother("0000123450000") == "135"
print("Test passed")
print('='*45)

def thirds(string):
    thirds = int(len(string)/3)
    first = string[0:thirds]
    last = string[-thirds:]
    mid = string[thirds:-thirds]
    return last + first + mid
newthirds = thirds("111222333")
print("last third, then first third, then the middle third in the new order")
print(newthirds)
assert thirds("123") == "312"
print("Test passed")
print("="*45)

def reverse(string):
    return string[::-1]
reversedstring = reverse("reverse this string")
print("Reverse a string")
print(reversedstring)
assert reverse("racecars") == "sracecar"
print("Test passed")
print("="*45)
