#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
    if n >0:
        return str[0:3]*n
    else:
        return False

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
    return str[0::2]

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  if str:
    counter = 0
    string = ""
    while counter <= len(str):
      string += str[0:counter]
      counter +=1
    return string

#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(stri):
    if len(stri) < 2:
        return 0
    else:
        counter = 0
        try:
            target = stri[-2:]
            for i in range(len(stri) -2):
                sub = stri[i:i + 2]
                if sub == target:
                    counter += 1
        except TypeError as te:
            return ("error is {}".format(te))
        return counter

    
print(front_times('Chocolate', 2)) 
front_times('Chocolate', 3) 
front_times('Abc', 3) 

string_bits('Hello') 
string_bits('Hi') 
string_bits('Heeololeo')

string_splosion('Code') 
string_splosion('abc') 
string_splosion('ab')

last2('hixxhi')
last2('xaxxaxaxx')
last2('axxxaaxx')
