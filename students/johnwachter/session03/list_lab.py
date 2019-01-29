#Title: Lab list_lab.py
#Change Log: (Who, When, What)
#JWachter, 2019-01-26, created file to explore the list data structure
#JWachter, 2019-01-28, completed exercises and checkd my work

#Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)
user_fruit = input("Enter a fruit: ")
fruit_list.append(user_fruit)
print(fruit_list)
user_index = int(input("Give me a number between 1 and {}: ".format(len(fruit_list))))
fruittodisplay = int(user_index-1)
print("Your number was {} and the fruit is {}".format(user_index, fruit_list[fruittodisplay]))
fruit_list = [input("Enter another fruit: ")] + fruit_list
print(fruit_list)
fruit_list.insert(0, 'Cherry')
print(fruit_list)
for fruit in fruit_list:
    if fruit.startswith('P'):
        print(fruit)

#series 2
print("Series 2: {}".format(fruit_list))
fruit_list.pop(-1)
print(fruit_list)
user_delete = input("Which fruit would you like to delete? ")
if user_delete in fruit_list:
    fruit_list.remove(user_delete)
print(fruit_list)

#series 3
reversedfruitlist = fruit_list[::-1]
for fruit in reversedfruitlist:
    yes_or_no = input("Do you like {}".format(fruit.lower()))
    if yes_or_no == 'no':
        fruit_list.remove(fruit)
    while yes_or_no != 'yes' and yes_or_no != 'no':
        print("Please enter yes or no: ")
        yes_or_no = input("Do you like {}".format(fruit.lower()))
        if yes_or_no == 'no':
            fruit_list.remove(fruit)
print(fruit_list)

#series4
fruit_list_reversed = []
for fruit in fruit_list:
    reversefruit = fruit[::-1]
    fruit_list_reversed.append(reversefruit)
fruit_list.pop(-1)
print("Original Fruit List with last removed {}".format(fruit_list))
print("Copy of List, with items reversed {}".format(fruit_list_reversed))
