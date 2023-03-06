# uwagi - linijka 120, (155, 211)
# Klasa - firma??
# co z dodaniem na git huba - jako nowa gałąź
# myslales o tym, zeby moze zrobic jeszcze klase, ktora przedstawi firme?
# mialaby tam swoich pracowników i większość tych metod, krore zdefiniowałeś byłoby
# jej częścią?


import sys
import re

employees = {}
managers = {}

positions_employees = {
    "Intern": 3000,
    "Junior": 5000,
    "Junior Specialist": 7000,
    "Specialist": 10000,
    "Senior Specialist": 13000,
    "Expert": 16000,
    "Team Leader": 20000
}

positions_managers = {
    "Supervisor": 25000,
    "Senior Supervisor": 30000,
    "Coordinator": 35000,
    "Director": 50000,
    "Global Director": 60000,
    "Board Member": 80000,
    "CEO": 150000
}


class Employee:
    def __init__(
        self, 
        employee_id, 
        first_name, 
        last_name, 
        salary, 
        street_name, 
        zip_code, 
        city, 
        position,
        nationality
    ):

        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.street_name = street_name
        self.zip_code = zip_code
        self.city = city
        self.position = position
        self.nationality = nationality

    def mail(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@developer.com"
    
    def address(self):
        return f"{self.street_name}, {self.zip_code}, {self.city}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def display_worker(self):
        return f"{self.first_name} {self.last_name}\nHome Address: ul. {self.address()}\n\
E-mail Address: {self.mail()}\nPosition: {self.position}\nSalary: {self.salary} PLN\n\
------------------------------------------------"

    def promote(self, position, salary):
        self.position = position
        self.salary = salary

    def change_address(self, street_name, zip_code, city):
        self.street_name = street_name
        self.zip_code = zip_code
        self.city = city
    
    def change_lastname(self, last_name):
        self.last_name = last_name


class Manager(Employee):
    def __init__(
        self, 
        employee_id, 
        first_name, 
        last_name, 
        salary, 
        street_name, 
        zip_code, 
        city, 
        position, 
        nationality, 
        board
    ):
        super().__init__(
            employee_id, 
            first_name, 
            last_name, 
            salary, 
            street_name, 
            zip_code, 
            city, 
            position, 
            nationality
        )
        self.board = board 
    
    def give_raise(self, bonus):
        self.salary = self.salary + bonus


def show_positions(workers):
    print("""
A list of positions with earnings:""")
    for Worker_No, worker in enumerate(workers):
        print(f"{Worker_No + 1} for {worker} who earns {workers[worker]} PLN")


def id_and_names(employee_type):
    print("""
A list of all workers""")
    # The list of {employee_type.__name__}) pomyśleć nad tym 
    if len(employee_type) == 0:
        print("No active workers")
    for value,key in employee_type.items():
        print(f"ID: {value}: {key.full_name()}")


def show_managers():
    print("""
The list of managers:""")
    if len(managers) == 0:
        print("No active managers")
    for value, key in managers.items():
        print(f"ID: {value}\n{key.display_worker()}")


def show_employees():
    print("""
The list of employees:""")
    if len(employees) == 0:
        print("No active employees")
    for value,key in employees.items():
        print(f"ID: {value}\n{key.display_worker()}")
    

def show_all():
    show_managers()
    show_employees()
    

def create_manager():
    print("""Adding a new manager:
Managers's ID must consist of 4 digits. The initial digit is always '6'""")
    employee_id = input("Insert manager's company ID: ")
    #pomyśleć nad zmianami i jak to dodać w funkcję zip_code, id i jeszcze coś
    while True:
        if re.match ("^[6][0-9][0-9][0-9]$", employee_id):
            break
        else:
            print("Manager's company ID is incorrect. Try again!")
            employee_id = input("Insert manager's company ID: ")
    first_name = input("Insert manager's first name: ")
    last_name = input("Insert manager's last name: ")
    street_name = input("Insert manager's address (the name of the street): ")
    zip_code = input("Insert manager's address (zip code): ")
    while True:
        if re.match ("^[0-9][0-9]-[0-9][0-9][0-9]$", zip_code):
            break
        else:
            print("Zip code is incorrect. Try again!")
            zip_code = input("Insert manager's address (zip code): ")
    city = input("Insert manager's address (city): ")
    print('\n')
    show_positions(positions_managers)
    print('\n')
    while True:
        choose_position = int(input("Choose an appropriate position by pressing a given number: "))
        if choose_position in range(7):
            position = list(positions_managers.keys())[choose_position - 1] 
            break
        else:
            print("Incorrect value! Try again.")
            continue
    salary = positions_managers[position]
    nationality = input("Insert nationality: ")
    decision = input("Board membership: Press y/n: ").lower()
    if decision == 'y':
        board = "Yes"
    elif decision == 'n':
        board = 'No'

    managers[employee_id] = Manager(
        employee_id, 
        first_name, 
        last_name, 
        salary, 
        street_name, 
        zip_code, 
        city, 
        position, 
        nationality, 
        board,
        )
    menu()


def create_employee():
    print("""Adding a new employee:
Employee's ID must consist of 4 digits. The initial digit is always '3'""")
    employee_id = input("Insert employee's company ID: ")
    #pomyśleć nad zmianami i jak to dodać w funkcję zip_code, id i jeszcze coś
    while True:
        if re.match ("^[3][0-9][0-9][0-9]$", employee_id):
            break
        else:
            print("Employee's company ID is incorrect. Try again!")
            employee_id = input("Insert employee's company ID: ")
    first_name = input("Insert employee's first name: ")
    last_name = input("Insert employee's last name: ")
    street_name = input("Insert employee's address (the name of the street): ")
    zip_code = input("Insert employee's address (zip code): ")
    while True:
        if re.match ("^[0-9][0-9]-[0-9][0-9][0-9]$", zip_code):
            break
        else:
            print("Zip code is incorrect. Try again!")
            zip_code = input("Insert employee's address (zip code): ")
    city = input("Insert employee's address (city): ")
    print('\n')
    show_positions(positions_employees)
    print('\n')
    while True:
        decision = int(input("Choose an appropriate position by pressing a given number: "))
        if decision in range(7):
            position = list(positions_employees.keys())[decision - 1] 
            break
        else:
            print("Incorrect value! Try again.")
    salary = positions_employees[position]
    nationality = input("Insert nationality: ")

    employees[employee_id] = Employee(employee_id, first_name, last_name, salary, street_name, zip_code, city, position, nationality)
    menu()


def delete_worker():
    id_and_names(managers)
    id_and_names(employees)
    id = input("Type the ID of a worker to remove: ")
    if re.match("^[3][0-9][0-9][0-9]$", id):
        print(f'A worker with id {id} has been removed from the list.')
        del employees[id]  
        menu()
    elif re.match("^[6][0-9][0-9][0-9]$", id):
        print(f'A worker with id {id} has been removed from the list.')
        del managers[id]  
        menu()
    else:
        print('A worker could not be found. Try again!')
        menu()


def promote():
    id_and_names(managers)
    id_and_names(employees)
    id_promotion = input("Choose worker's ID to promote: ")
    if id_promotion in managers:
        new_position = list(positions_managers.keys()).index(managers[id_promotion].position) + 1
        if new_position in range(len(positions_managers)):
            managers[id_promotion].promote(
                list(positions_managers.keys())[new_position],
                list(positions_managers.values())[new_position],
            )
            print(f"""The manager has been promoted!
He is now a/an {list(positions_managers.keys())[new_position]} and earns {list(positions_managers.values())[new_position]} zł""")
            input("Press any key to go back to menu: ")
            menu()
        else:
            print("The manager is the CEO. He cannot be promoted.")
            input("Press any key to go back to menu: ")
            menu()
    elif id_promotion in employees:
        new_position = list(positions_employees.keys()).index(employees[id_promotion].position) + 1
        if new_position in range(len(positions_employees)):
            employees[id_promotion].promote(
                list(positions_employees.keys())[new_position],
                list(positions_employees.values())[new_position],
            )
            print(f"""The employee has been promoted!
He is now a/an {list(positions_employees.keys())[new_position]} and earns {list(positions_employees.values())[new_position]} zł""")
            input("Press any key to go back to menu: ")
            menu()
        else:
            print("This employee has been moved to managers")
            manager_id = input("Choose the ID for a new manager: ")
            while True:
                if re.match("^[6][0-9][0-9][0-9]$", manager_id):
                    break
                else:
                    print("Manager's company ID is incorrect. Try again!")
                    manager_id = input("Choose the ID for a new manager: ")
            decision = input("Board membership: Press y/n: ").lower()
            if decision == "y":
                board = "Yes"
            elif decision == "n":
                board = "No"
            managers[manager_id] = Manager(
                manager_id, 
                employees[id_promotion].first_name, 
                employees[id_promotion].last_name, 
                list(positions_managers.values())[0],
                employees[id_promotion].street_name, 
                employees[id_promotion].zip_code, 
                employees[id_promotion].city, 
                list(positions_managers.keys())[0], 
                employees[id_promotion].nationality, 
                board
                )
            del employees[id_promotion]
            input("Press any key to go back to menu: ")
            menu()
    else:
        print("Incorrect value. Try again")
        input("Press any key to go back to menu: ")
        menu()


def home_address():
    id_and_names(managers)
    id_and_names(employees)
    id = input("Choose employee's ID: ")
    if id in managers or id in employees:
        street_name = input("Insert new address (the name of the street): ")
        zip_code = input("Insert new address (zip code): ")
        while True:
            if re.match ("^[0-9][0-9]-[0-9][0-9][0-9]$", zip_code):
                break
            else:
                print("Zip code is incorrect. Try again!")
                zip_code = input("Insert manager's address (zip code): ")
        city = input("Insert new address (city): ")
        if id in managers:
            managers[id].change_address(street_name, zip_code, city)
        else:
            employees[id].change_address(street_name, zip_code, city)
        print("The home address has been changed.")
        input("Press any key to go back to menu: ")
        menu()
    

def employees_name():
        id_and_names(managers)
        id_and_names(employees)
        id = input("Choose employee's ID: ")
        if id in managers:
            last_name = input("Insert a new last name: ")
            managers[id].change_lastname(last_name)
            print("The last name has been changed.")
            input("Press any key to go back to menu: ")
            menu()
        elif id in employees:
            last_name = input("Insert a new last name: ")
            managers[id].change_lastname(last_name)
            print("The last name has been changed.")
            input("Press any key to go back to menu: ")
            menu()
        else:
            print("Invalid value")
            input("Press any key to go back to menu: ")
            menu()


def manager_raise(id_manager, bonus):
    if id_manager in managers:
        managers[id_manager].give_raise(bonus)
        print(f'{managers[id_manager].full_name()} received {bonus} raise and earns {managers[id_manager].salary} zł now')
        print("")
        input("Press any key to go back to menu: ")
        menu()
    else:
        print("""Incorrect value!
        """)
        input("Press any key to go back to menu: ")
        menu()
    

def menu():
    print("""
Employee Management Tool
What do you want to do? Press a given number:
press 1 to display employees and managers
press 2 to display all managers
press 3 to display all emoloyees
press 4 to add a/an emlpoyee/manager
press 5 to remove a/an employee/manager
press 6 to promote a/an emloyee/manager
press 7 to change emloyee's/manager's personal data
press 8 to give a bonus to a manager
press 9 to exit""")

    try:
        press = int(input("Press a given number: "))
        if press == 1:
            show_all()
            input("Press any key to go back to menu: ")
            menu()
        elif press == 2:
            show_managers()
            input("Press any key to go back to menu: ")
            menu()
        elif press == 3:
            show_employees()
            input("Press any key to go back to menu: ")
            menu()
        elif press == 4:
            choice = input("To add a new manager press 'm' and to add a new employee press 'e': ").lower()
            if choice == 'm':
                create_manager()
            elif choice == "e":
                create_employee()
            else:
                print("Incorrect value!")
                menu()
        elif press == 5:
            delete_worker()
        elif press == 6:
            promote()
        elif press == 7:
            print("""
Changing personal data:
Press 1 to change manager's/employee's home address
Press 2 to change manager's/employee's last name
""")        
            decision = input("Press an appropriate key: ")
            if decision == '1':
                home_address()
            elif decision == '2':
                employees_name()
            else:
                print("Incorrect value!")
                menu()
        elif press == 8:
            id_and_names(managers)
            id_manager = input("Type the ID of a worker to remove: ")
            bonus = int(input("How much raise will the manager get?: "))
            manager_raise(id_manager, bonus)
        elif press == 9:
            print("Exit")
            sys.exit(0)
        else:
            print("Incorrect value! Try again.")
            menu()
    except ValueError:
        print("Incorrect value! Try again.")
        menu()

menu()