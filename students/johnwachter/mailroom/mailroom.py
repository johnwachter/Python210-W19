#Title: mailroom.py
#Change Log: (Who, When, What)
#JWachter, 1/19/2019, creating file to upload to github
#JWachter, 1/28/2019, built donor database

import sys

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Me Myself": [100]}
user_prompt = "\n".join(("Welcome to your Donor Database", "Please choose an option: ", "1 - Send a Thank You", "2 - Create a Report", "3 - Quit\n"))

def sendthankyou():
    user_input = input(
        "Let's send some Thank You letters.\nType 'list' to see a list of donors, or\ninput the donors full name: ")
    for record in donor_db:
        for name in record:
            if user_input in name:
                amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
                amtdonated
                user_input_index = int(name.index(user_input))
                print("###{}".format(user_input_index))
                donor_db[4].insert(user_input_index, amtdonated)
                print(donor_db)
            elif user_input == 'list':
                print(record[0])
            elif user_input not in name:
                print("k")

# def sendthankyou():
#     user_input = input(
#         "Let's send some Thank You letters.\nType 'list' to see a list of donors, or\ninput the donors full name: ")
#     for record in donor_db:
#         for name in record:
#             # print(name)
#             # if 'Me Myself' in record:
#             #     print("true")
#             # else: print("false")
#             if user_input in name:
#                 #print("true")
#                 amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
#                 amtdonated
#                 user_input_index = int(name.index(user_input))
#                 print("###{}".format(user_input_index))
#                 donor_db[4].insert(user_input_index, amtdonated)
#                 print(donor_db)
#             elif user_input == 'list':
#                 print(record[0])
#             elif user_input not in name:
#                 print("k")

def createreport():
    print("Great, let's create a report")
    for record in donor_db:
        for name in record:
            print(name)

def quitprogram():
    print("Goodbye")
    sys.exit()

def main():
    while True:
        response = input(user_prompt)
        if response == "1":
            sendthankyou()
        elif response == "2":
            createreport()
        elif response == "3":
            quitprogram()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
