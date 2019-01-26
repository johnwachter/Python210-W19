#Title: Lab list_lab.py
#Change Log: (Who, When, What)
#JWachter, 2019-01-26, created file to explore the list data structure

#series 1
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
    if fruit[0] == 'P':
        print("P fruits: ".format(fruit))
