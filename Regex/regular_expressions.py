""""This program will create a table with people using datas provided by the user
Main actions preformed by the program:
1. gathering data - using regex
2. sending the data to excel - separate py-file for it
3. changing an excel into a pdf file which should be saved accordingly - separate py-file for it
4. sending this to my email account - separate py-file for it"""

import re


class Person():
    """the class was created to make it easier for me 
to add a new person to a dictionary but is it really
necesary in this case??"""
    def __init__(
        self,
        title,
        name,
        surname,
        gender,
        birthdate,
        profession,
        company,
        email,
        company_website,
        marital_status,
        id_nummer,
        passport_nummer,
        issue_date,
        expiration_date
    ):
        self.title = title
        self.name = name
        self.surname = surname
        self.gender = gender
        self.birthdate = birthdate
        self.profession = profession
        self.company = company
        self.email = email
        self.company_website = company_website,
        self.martial_status = marital_status,
        self.id_nummer = id_nummer,
        self.passport_nummer = passport_nummer,
        self.issue_date = issue_date,
        self.expiration_date = expiration_date


def choosing_title():
    titles = {
        0: " ",
        1: "lic.",
        2: "inż.",
        3: "mgr",
        4: "dr",
        5: "dr hab.",
        6: 'prof.',
    }
    print("""Choose a possible title from the list:
0. No academic title
1. Licencjat
2. Inżynier
3. Magister
4. Doktor
5. Doktor habilitiowany
6. Profesor""")
    chosen_number = int(input("Press an appropriate key: "))
    if 0 <= chosen_number <= 6:
        return titles[chosen_number]
    else:
        choosing_title()
 # TODO: Pytest przeprowadzić - czy rzeczywiście wartość się zgadza

def new_person():
    person = {}
    print("""Adding a person to the list
Please fill all data according to instuctions given.""")
    title = choosing_title()




def main():
    while True:
        adding_new_person = input("Do you want to add a new person to the list?(y/n): ").lower()
        if adding_new_person == "y":
            new_person()
        elif adding_new_person == 'n':
            break
        else:
            print("Incorrect value. Try again.")
            continue

main()
