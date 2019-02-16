#tle: MailroomPart3.py
#Change Log: (Who, When, What)
#JWachter, 2019-02-10, Created File
#JWachter, 2019-02-10, put in some error handling
#JWachter, 2019-02-10, looked to use list comprehension, didn't find a good spot



import sys

donor_db = {"William Gates, III": [653772.32, 12.17],
                        "Jeff Bezos": [877.33],
                        "Paul Allen": [663.23, 43.87, 1.32],
                        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
                        "Me Myself": [100]}
user_prompt = "\n".join(("Welcome to your Donor Database", "Please choose an option: ", "1 - Create One 'Thank You' Letter", "2 - Create a Report", "3 - Create Thank You letters for all donors", "4 - Quit\n"))

def sendthankyou():
    user_input = ""
    while user_input != "Main Menu":
        try:
            user_input = input("Let's send some Thank You letters.\nType 'list' to see a list of donors, or input the donors full name to add a gift and send a Thank You letter. To return to the main menu, type 'Main Menu': ")
            if user_input in donor_db:
                amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
                donor_db[user_input].append(amtdonated)
                thankyouletterdict = {"Name": user_input, "Amount": amtdonated}
                print("+"*45 + "\nNice!\n Thanks, {Name} for the ${Amount}!\n\nSincerely, me\n".format(**thankyouletterdict) + "+"*45)
            elif user_input == 'list':
                for donor in donor_db:
                    print(donor + "\n")
            elif user_input not in donor_db and user_input != 'Main Menu':
                donor_db[user_input] = []
                print("Great, {} has been added to the donor database.".format(user_input))
                amtdonated = int(input("Please enter the amount donated by {}: ".format(user_input)))
                donor_db[user_input].append(amtdonated)
                thankyouletterdict = {"Name": user_input, "Amount": amtdonated}
                print("+" * 45 + "\nNice! Thanks, {Name} for the ${Amount}!\n\nSincerely, me\n".format(
                    **thankyouletterdict) + "+" * 45)
        except ValueError as ve:
            print('please enter a valid number', type(ve))
def createreport():
    print("        Here is your report\n" + "="*65)
    print("Donor Name          |  Total Given  | Num Gifts | Average Gift")
    print("---------------------------------------------------------------")
    for donor in donor_db:
        try:
            avg = sum(donor_db[donor])/len(donor_db[donor])
            print("{:20} |".format(donor), "${0:10,.2f}|".format(sum(donor_db[donor])), "{:>4} {:<4}|".format(len(donor_db[donor]),"gifts"), "${0:<10,.2f}".format(avg))
        except ZeroDivisionError:
            print("{} has not given any gifts.".format(donor))
    main()
    print("\n")
def donorcategory():
    for donor in donor_db:
        if int(sum(donor_db[donor])) < 10000:
            return 'measly'
        else:
            return 'generous'

def createthankyouletters():
    for donor in donor_db:
        with open('/Users/John/Python210-W19/students/johnwachter/mailroom/{}_letter.txt'.format(donor), 'w') as donorletter:
            donorletter.write("+"*45 + "\nNice!\n\nThanks, {} for the ${}! You have given ${} since you started donating.\n\nSincerely, me\n".format(donor, donor_db[donor][-1], sum(donor_db[donor])) + "+"*45)
    print("Letters generated.\n")


def quitprogram():
    print("Goodbye")
    sys.exit()

def responsedict(choice):
    data = {'1': sendthankyou, '2': createreport, '3': createthankyouletters, '4': quitprogram}
    return data.get(choice)()
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
