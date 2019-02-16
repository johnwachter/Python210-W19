#Title: MailroomPart4.py
#Change Log: (Who, When, What)
#JWachter, 2019-02-16, Created File
#JWachter, 2019-02-16, Updated create report function to split data processing and data presentation. Now have 2 funcs
#JWachter, 2019-02-10, looked to use list comprehension, didn't find a good spot


import sys

donor_db = {"William Gates, III": [653772.32, 12.17],
                        "Jeff Bezos": [877.33],
                        "Paul Allen": [663.23, 43.87, 1.32],
                        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
                        "Me Myself": [100]}
user_prompt = "\n".join(("Welcome to your Donor Database", "Please choose an option: ", "1 - Create One 'Thank You' Letter", "2 - Create a Report", "3 - Create Thank You letters for all donors", "4 - Quit\n"))

def sendthankyou(database = donor_db):
    user_input = ""
    donorlist = []
    while user_input != "Main Menu":
        try:
            user_input = input("Let's send some Thank You letters.\nType 'list' to see a list of donors, or input the donors full name to add a gift and send a Thank You letter. To return to the main menu, type 'Main Menu': ")
            if user_input in donor_db:
                amtdonated = int(input("Please enter the amount donated: "))
                database[user_input].append(amtdonated)
                thankyouletterdict = {"Name": user_input, "Amount": amtdonated}
                print("+"*45 + "\nNice!\n Thanks, {Name} for the ${Amount}!\n\nSincerely, me\n".format(**thankyouletterdict) + "+"*45)
            elif user_input == "list":
                for donor in database:
                    donorlist.append(donor)
                    print(donor + "\n")
            elif user_input not in database and user_input != 'Main Menu':
                database[user_input] = []
                print("Great, {} has been added to the donor database.".format(user_input))
                amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
                database[user_input].append(amtdonated)
                thankyouletterdict = {"Name": user_input, "Amount": amtdonated}
                print("+" * 45 + "\nNice! Thanks, {Name} for the ${Amount}!\n\nSincerely, me\n".format(**thankyouletterdict) + "+" * 45)
        except ValueError as ve:
            print('please enter a valid number', type(ve))

def createreport(database = donor_db):
    try:
        reportstring = str("        Here is your report\n" + "="*65 + "\n" + "Donor Name          |  Total Given  | Num Gifts | Average Gift\n" +
        "---------------------------------------------------------------" + "\n")
        for donor in database:
            avg = sum(database[donor])/len(database[donor])
            reportstring += "{:20} | ${:10,.2f}| {:>4} {:<4}| ${:<10,.2f} \n".format(donor, sum(database[donor]), len(database[donor]), "gifts", avg)
    except ZeroDivisionError as zde:
        print("{} has not given any gifts.".format(donor))
    return reportstring

def displayreport():
    print(createreport(donor_db))
    print("\n")

def tylettertxt():
    for donor in donor_db:
        txt = "+"*45 + "\nNice!\n\nThanks, {} for the ${}! You have given ${} since you started donating.\n\nSincerely, me\n".format(donor, donor_db[donor][-1], sum(donor_db[donor])) + "+"*45
    return txt

def createthankyouletters(txt = tylettertxt()):
    for donor in donor_db:
        with open('/Users/John/Python210-W19/students/johnwachter/mailroom/{}_letter.txt'.format(donor), 'w') as donorletter:
            donorletter.write(txt)
    print("Letters generated.\n")


def quitprogram():
    print("Goodbye")
    sys.exit()

def responsedict(choice):
    casedict = {'1': sendthankyou, '2': displayreport, '3': createthankyouletters, '4': quitprogram}
    if casedict.get(choice) == "1":
        return casedict.get(choice)
    else:
        return casedict.get(choice)()
    main()

def main():
    while True:
        response = input(user_prompt)
        try:
            responsedict(response)
        except TypeError as te:
            print('Please enter 1 2 or 3', type(te))

if __name__ == "__main__":
    main()
