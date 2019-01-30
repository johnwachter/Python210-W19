#Title: mailroom.py
#Change Log: (Who, When, What)
#JWachter, 2019-01-28, Created File
#JWachter, 2019-01-28, built donor database
#JWachter, 2019-01-28, imported ordered dictionary to update info in dictionary
#JWachter, 2019-01-28, realized I don't need an ordered dictionary, no longer importing
#JWachter. 2019-01-29, adding while loop to get user input and not return to the main menu until specified

import sys

donor_db = {"William Gates, III" : [653772.32, 12.17],
                        "Jeff Bezos": [877.33],
                        "Paul Allen": [663.23, 43.87, 1.32],
                        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
                        "Me Myself": [100]}
user_prompt = "\n".join(("Welcome to your Donor Database", "Please choose an option: ", "1 - Send a Thank You", "2 - Create a Report", "3 - Quit\n"))

def sendthankyou():
    user_input = ""
    while user_input != "Main Menu":
        user_input = input("Let's send some Thank You letters.\nType 'list' to see a list of donors, or input the donors full name to add a gift and send a Thank You letter. To return to the main menu, type 'Main Menu': ")
        if user_input in donor_db:
            amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
            donor_db[user_input].append(amtdonated)
            print("+"*45 + "\nNice! Thanks for the ${}, {}!\n\nSincerely, me\n".format(amtdonated, user_input) + "+"*45)
        elif user_input == 'list':
            for donor in donor_db:
                print(donor + "\n")
        elif user_input not in donor_db and user_input != 'Main Menu':
            donor_db[user_input] = []
            print("Great, {} has been added to the donor database.".format(user_input))
            amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
            donor_db[user_input].append(amtdonated)


def createreport():
    print("        Here is your report\n" + "="*45)
    print("Donor Name          |  Total Given  | Num Gifts | Average Gift")
    print("--------------------------------------------------------")
    l = max(len(donor) for donor in donor_db)
    for donor in donor_db:
        avg = sum(donor_db[donor])/len(donor_db[donor])
        print("{:20} |".format(donor), "${0:10,.2f}|".format(sum(donor_db[donor])), "{:>4} {:<4}|".format(len(donor_db[donor]),"gifts"), "${0:<10,.2f}".format(avg))
    main()
    print("+++++++++++++++++++++")

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
