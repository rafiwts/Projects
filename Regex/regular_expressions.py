""""This program will create a table with people using datas provided by the user
Main actions preformed by the program:
1. gathering data - using regex
2. sending the data to excel - separate py-file for it
3. changing an excel into a pdf file which should be saved accordingly - separate py-file for it
4. sending this to my email account - separate py-file for it"""

import re, datetime

person = {}


class Person():
    """the class was created to make it easier for me 
to add a new person to a dictionary but is it really
necesary in this case??"""
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
Company website: {self.company_website}
E-mail: {self.email}
ID number: {self.id_number}
Passport number: {self.passport_number}
Issue date: {self.issue_date}
Expiration date: {self.expiration_date}
'''
    

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
 # TODO: Pytest przeprowadzić - czy rzeczywiście wartość się zgadza


def choosing_gender():
    gender_choice = input("Choose an appropriate gender: Male (M) or Female (F): ")
    if gender_choice.lower() == 'male' or gender_choice.lower() == 'm':
        return "Male"
    elif gender_choice.lower() == 'female' or gender_choice.lower() == 'f':
        return "Female"
    else:
        print("Incorrect value. Try again")
        choosing_gender()


def birthdate_authentication():
    current_date = datetime.date.today()
    regex_birthday_validation = re.compile(
        r'(3[0-1]|[1-2]\d|0[1-9])/' # day
        r'(0[1-9]|1[0-2])/' # month
        r'(19\d{2}|20\d{2})' # year 
    )

    while True:
        birthday_choice = input("Insert a valid date of birth (format: DD/MM/YYYY): ")
        birthday_validity = re.match(regex_birthday_validation, birthday_choice)

        if birthday_validity:
            if current_date > datetime.date(int(birthday_validity.group(3)), int(birthday_validity.group(2)), int(birthday_validity.group(1))):
                break
            else:
                print("The date is in future. Try again.")
        else:
            print("Incorrect value. Try again.")
        
    return birthday_choice 

def email_authentication():
    regex_email_validation = re.compile(
        r'^([A-Z0-9]+|[A-Z0-9][A-Z0-9\.-]+[A-Z0-9])' # cannot start with '.' and '-'  
        r'@'
        r'([A-Z0-9]+|[A-Z0-9][A-Z0-9\.-]+[A-Z0-9])' # cannot start with '.' and '-'
        r'(\.[A-Z]{2,6})$', re.IGNORECASE)
    
    while True:
        email_choice = input("Insert a valid e-mail address: ")
        
        if re.match(regex_email_validation, email_choice):
            break
        else:
            print("Incorrect value. Try again")

    return email_choice

    #TODO: Oczywiście należy zrobić pytest dla tego regexa


def company_website_authentication():
    regex_website_validation = re.compile(
        r'^(https?://)'  # http:// or https:// are necessary
        r'(www\.([A-Z0-9]{1,62}|[A-Z0-9][A-Z0-9\.-]{1,60}[A-Z0-9])\.[A-Z]{2,6}|'  # url comain 
        r'localhost|'  # or a 'localhost' but it will not be necessary here (just for practice)
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # or ip - also not necessary (just for practice)
        r'(?::\d+)?'  # optional port - not necessary (just for practice)
        r'(?:/?|[/?]\S+/?)$', re.IGNORECASE)
    
    while True:
        passport_number_choice = input("Insert a vaild website: ")
    
        if re.match(regex_website_validation, passport_number_choice):
            break
        else:
            print("Incorrect value. Try again")
           
    return passport_number_choice
    #TODO: Oczywiście należy zrobić pytest dla tego regexa


def id_number_authentication(birthdate):
    day, month, year = birthdate.split('/') # variables for a date of birth given by a user
    second_part_of_id_number = input("Insert a second part of an id nummer: ")

    if int(year) < 2000:
        first_part_of_id_number = year[2:] + month + day # old id numbers
    else:
        first_part_of_id_number = year[2:] + str(int(month) + 20) + day # new id numbers (since 2000)
    
    id_number = first_part_of_id_number + second_part_of_id_number
    
    return id_number
    #TODO: dokończyć funkcję - podając datęurodzenia


def passport_number_authentication():
    regex_number_validation = re.compile(
        r'^[A-Z]{2}\s[0-9]\s[0-9]{6}$'
    )

    while True:
        passport_number_choice = input("Insert a vaild passport number: ")
    
        if re.match(regex_number_validation, passport_number_choice):
            break
        else:
            print("Incorrect value. Try again")
    #TODO: Oczywiście należy zrobić pytest dla tego regexa
    
    return passport_number_choice

def passport_dates():
    regex_date_validation = re.compile(
        r'(3[0-1]|[1-2]\d|0[1-9])/' # day
        r'(0[1-9]|1[0-2])/' # month
        r'(19\d{2}|20\d{2})' # year 
    )

    while True:
        issue_date_choice = input("Insert a valid date of birth (format: DD/MM/YYYY): ")
        if re.match(regex_date_validation, issue_date_choice):
            break
        else:
            print("Incorrect value. Try again")
    #TODO: Oczywiście należy zrobić pytest dla tego regexa

    return issue_date_choice


def new_person():
    print("""Adding a person to the list
Please fill all data according to instuctions given.""")
    title = choosing_title()
    name = input("Insert a first name: ").capitalize()
    surname = input("Insert a surname: ").capitalize()
    gender = choosing_gender()
    birthdate = birthdate_authentication()
    profession = input("Insert a profession: ")
    company = input("Insert a company: ")
    email = email_authentication()
    company_website = company_website_authentication()
    id_number = id_number_authentication(birthdate)
    passport_number = passport_number_authentication()
    issue_date = passport_dates()
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
    print(new_person_object)


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

#TODO: naprawić funkcję, która zwraca none jak się za pierwszym razem żle wpisze
#TODO: dodać do słownika wywołania, żeby zapisywało to
#TODO: w drugim pliki zacząć plik dodawania do excela