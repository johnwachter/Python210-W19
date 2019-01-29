#Title: strformat_lab.py
#Change Log: (Who, When, What)
#JWachter, 1/28/2019, Created File

#task1
mytupl = (2, 123.4567, 10000, 12345.67)
print("file_00{0} :  {1}, {2:.2e}, {3:.2e}".format(mytupl[0], round(mytupl[1], 2), mytupl[2], mytupl[3]))

#task2
# Using your results from Task One, repeat the exercise, but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already).
print("The tuple contains {} items and the values are: {}, {}, {}, {}".format(len(mytupl),*mytupl))

#task3
def arbitrarylengthtupl():
    tupl = (2, 3, 4, 5, 6 ,7)
    tupllen = len(tupl)
    print("Tuple contains {} items which are ".format(tupllen) + ("{}, "*tupllen).format(*tupl))
arbitrarylengthtupl()

#task4
fiveelementtuple = (4, 30, 2017, 2, 27)
print("0{}, {}, {}, 0{}, {}".format(fiveelementtuple[3], fiveelementtuple[4], fiveelementtuple[2], fiveelementtuple[0], fiveelementtuple[1]))

#task5
fruitweightlist = ['oranges', 1.3, 'lemons', 1.1]
twentypercentincrease = 1.2
print(f"The weight of an {fruitweightlist[0].rstrip('s').upper()} is {fruitweightlist[1]*twentypercentincrease} and the weight of a {fruitweightlist[2].rstrip('s').upper()} is {fruitweightlist[3]*twentypercentincrease}")

#task6
data = [["NAME", "AGE", "COST"], ["Greg", "Barnold", "Jarvey"], ['27', '89', '62'], ["$100", "$40,000", "$8,500"]]
col_width = max(len(word) for row in data for word in row) + 2 # padding
for row in data:
    print("".join(word.ljust(col_width) for word in row))
