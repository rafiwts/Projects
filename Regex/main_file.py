"""This program will create a table with people using data provided by the user
Main actions preformed by the program:
1. saving and validating data (using regular expressions)
2. sending the data to an excel file
3. sending this to my email account
In English - general comments to how the program functions
Po polsku - moje wątpliwości, pytania :)"""

import re, datetime
from excel_file import *
from email_file import *
from regular_expressions import *

dict_of_added_people = {} # czy dodawanie instancji klasy do słownika, który jest poza słownikiem ma sens, czy może lepiej utworzyć metodę klasy jakąś


class Person():
    count = 0

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
        id_number,
        passport_number,
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
        self.company_website = company_website
        self.id_number = id_number
        self.passport_number = passport_number
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        Person.count += 1

    def __repr__(self):
        return f'''
{Person.count} person: {self.name} {self.surname}:
Title: {self.title}
Name: {self.name}
Surname: {self.surname}
Gender: {self.gender}
Birthdate: {self.birthdate}
Profession: {self.profession}
Company: {self.company}
Company passport_number: {self.company_website}
E-mail: {self.email}
ID number: {self.id_number}
Passport number: {self.passport_number}
Issue date: {self.issue_date}
Expiration date: {self.expiration_date}
'''

    def list_of_attributes(self):
        return [
            self.title, 
            self.name, 
            self.surname, 
            self.gender,
            self.birthdate,
            self.profession,
            self.company,
            self.email,
            self.company_website,
            self.id_number,
            self.passport_number,
            self.issue_date,
            self.expiration_date
        ]
    

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
        print("Incorrect value. Try again.")
        choosing_title()


def choosing_gender():
    gender_choice = input("Choose an appropriate gender: Male (M) or Female (F): ").lower()
    if gender_choice == 'male' or gender_choice == 'm':
        return "Male"
    elif gender_choice == 'female' or gender_choice == 'f':
        return "Female"
    else:
        print("Incorrect value. Try again")
        choosing_gender()


def authentication_of_data(validation_pattern, user_choice): # this function uses regular expressions to see if the value is valid (see regular_expressions.py)
    while not re.match(validation_pattern, user_choice):
        user_choice = input("Incorrect value. Try again: ")
            
    return user_choice


def birthdate_authentication(validation_pattern):
    """The function validates the date of birth - if an inserted name
is in the future (see an if statement) then it is not valid"""
    current_date = datetime.date.today()

    while True:
        birthday_choice = input("Insert a valid date of birth (format: DD/MM/YYYY): ")
        birthday_validity = re.match(validation_pattern, birthday_choice)

        if birthday_validity:
            if current_date > datetime.date(int(birthday_validity.group(3)), int(birthday_validity.group(2)), int(birthday_validity.group(1))): # if an inserted date is in the future 
                break
            else:
                print("The date is in future. Try again.")
        else:
            print("Incorrect value. Try again.")
        
    return birthday_choice 


def id_number_authentication(birthdate):
    day, month, year = birthdate.split('/') # variables for the date of birth given by a user
    second_part_of_id_number = input("Insert a second part of an id nummer: ")

    if int(year) < 2000:
        first_part_of_id_number = year[2:] + month + day # a pattern for old id numbers (before 2000)
    else:
        first_part_of_id_number = year[2:] + str(int(month) + 20) + day # a pattern for new id numbers (since 2000)
    
    id_number = first_part_of_id_number + second_part_of_id_number # combining two parts of an id number
    
    return id_number


def adding_new_person():
    print("""Adding a person to the list
Please fill all data according to instuctions given.""")
    title = choosing_title()

    name_choice = input("Insert a first name: ")
    name = authentication_of_data(regex_string_value, name_choice)

    surname_choice = input("Insert a surname: ")
    surname = authentication_of_data(regex_string_value, surname_choice)

    gender = choosing_gender()
    birthdate = birthdate_authentication(regex_date_validation)
    
    profession_choice = input("Insert a profession: ")
    profession = authentication_of_data(regex_string_value, profession_choice)

    company_choice = input("Insert a company: ")
    company = authentication_of_data(regex_string_value, company_choice)

    email_choice = input("Insert an email adress: ")
    email = authentication_of_data(regex_email_validation, email_choice)

    company_website_choice = input("Insert a company website (format: https://.www.(url)): ")
    company_website = authentication_of_data(regex_website_validation, company_website_choice)

    id_number = id_number_authentication(birthdate)

    passport_number_choice = input("Insert a passport number: ")
    passport_number = authentication_of_data(regex_passport_number_validation, passport_number_choice)

    issue_date_choice = input("Insert a date of issue: ")
    issue_date = authentication_of_data(regex_date_validation, issue_date_choice)

    expiration_in_ten_years = int(issue_date.split('/')[2]) + 10
    expiration_date = issue_date[:6] + str(expiration_in_ten_years) # expiration date automatically in ten years

    new_person_object = Person(
        title, 
        name, 
        surname, 
        gender, 
        birthdate, 
        profession,
        company,
        email,
        company_website,
        id_number,
        passport_number,
        issue_date,
        expiration_date
    )

    dict_of_added_people[Person.count] = new_person_object # adding a new person to a dict
    print(new_person_object)
    

def main():
    while True:
        user_choice = input("Do you want to add a new person to the list?(y/n): ").lower()
        if user_choice == "y":
            adding_new_person()
        elif user_choice == "n":
            saving_to_excel(dict_of_added_people, excel_file) 
            sending_email(dict_of_added_people, email, email, excel_file)
            input('''Data has been saved to an excel file and send to your e-mail
Enter a random value to exit the program: ''')
            break
        else:
            print("Incorrect value. Try again.")
            continue


if __name__ == "__main__":
    main()