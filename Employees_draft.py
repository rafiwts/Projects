import sys
import re

employees = []
managers = []

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

class Employees:

    def __init__(self, employee_id, first_name, last_name, salary, street_name, zip_code, city, position, nationality):
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

    def promote(self, position, salary):
        self.position = position
        self.salary = salary

    def change_address(self, street_name, zip_code, city):
        self.street_name = street_name
        self.zip_code = zip_code
        self.city = city
    
    def change_lastname(self, last_name):
        self.last_name = last_name

class Managers(Employees):
    def __init__(self, employee_id, first_name, last_name, salary, street_name, zip_code, city, position, nationality, board):
        super().__init__(employee_id, first_name, last_name, salary, street_name, zip_code, city, position, nationality)
        self.board = board 
    
    def __add__(self, bonus):
        return self.salary + bonus

def show_positions(x):
    print("\n")
    ind = 1
    print("A list of positions with earnings:")
    for i in x:
        print(f"{ind} for {i} who earns {x[i]} PLN")
        ind += 1

def list_all_workers():
    print("\n")
    print("A list of all workers:")
    print("Employees:")
    if len(employees) == 0:
        print("No active employees")
    for i in employees:
        print(f"ID: {i.employee_id}: {i.first_name} {i.last_name}")
    print("Managers:")
    if len(managers) == 0:
        print("No active managers")
    for y in managers:
        print(f"ID: {y.employee_id}: {y.first_name} {y.last_name}")
    print("\n")

def show_all():
    print("\n")
    print("The list of managers:")
    if len(managers) == 0:
        print("No active managers")
    for i in managers:
        print(f"ID: {i.employee_id}\n{i.first_name} {i.last_name}\nHome Address: ul. {i.address()}\n\
E-mail Address: {i.mail()}\nPosition: {i.position}\nSalary: {i.salary} PLN\nBoard Member: {i.board}\n\
------------------------------------------------")
    print("\n")
    print("The list of employees:")
    if len(employees) == 0:
        print("No active managers")
    for i in employees:
        print(f"ID: {i.employee_id}\n{i.first_name} {i.last_name}\nHome Address: ul. {i.address()}\n\
E-mail Address: {i.mail()}\nPosition: {i.position}\nSalary: {i.salary} PLN\n\
------------------------------------------------")
    print('\n')
    input("Press any key to go back to menu: ")
    menu()

def show_managers():
    print("\n")
    print("The list of managers:")
    if len(managers) == 0:
        print("No active managers")
    for i in managers:
        print(f"ID: {i.employee_id}\n{i.first_name} {i.last_name}\nHome Address: ul. {i.address()}\n\
E-mail Address: {i.mail()}\nPosition: {i.position}\nSalary: {i.salary} PLN\nBoard Member: {i.board}\n\
------------------------------------------------")
    print('\n')
    input("Press any key to go back to menu: ")
    menu()  

def show_employees():
    print("\n")
    print("The list of employees:")
    if len(employees) == 0:
        print("No active managers")
    for i in employees:
        print(f"ID: {i.employee_id}\n{i.first_name} {i.last_name}\nHome Address: ul. {i.address()}\n\
E-mail Address: {i.mail()}\nPosition: {i.position}\nSalary: {i.salary} PLN\n\
------------------------------------------------")
    print("\n")
    input("Press any key to go back to menu: ")
    menu()       

def add_worker():
    print("\n")
    choice = input("To add a new manager press 'm' and to add a new employee press 'e': ").lower()
    if choice == 'm':
        print("Adding a new manager:")
        print("Managers's ID must consist of 4 digits. The initial digit is always '6'")
        employee_id = input("Insert manager's company ID: ")
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
            if 0 < choose_position <= 7:
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
        managers.append(Managers(employee_id, first_name, last_name, salary, street_name, zip_code, city, position, nationality, board))
        menu()
    elif choice == 'e':
        print("Adding a new employee:")
        print("Employee's ID must consist of 4 digits. The initial digit is always '3'")
        employee_id = input("Insert employee's company ID: ")
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
            if 0 < decision <= 7:
                position = list(positions_employees.keys())[decision - 1] 
                break
            else:
                print("Incorrect value! Try again.")
        salary = positions_employees[position]
        nationality = input("Insert nationality: ")

        employees.append(Employees(employee_id, first_name, last_name, salary, street_name, zip_code, city, position, nationality))
        menu()
    else:
        print("Invalid value. Try again")
        add_worker()

def delete_worker():
    list_all_workers()
    id = input("Type the ID of a worker to remove: ")
    for i in employees:
        if i.employee_id == id:
            employees.remove(i)
            print('A worker has been removed from the list.')
            menu()
    for y in managers:
        if y.employee_id == id:
            managers.remove(y)
            print('A worker has been removed from the list.')
            menu()
    print('A worker could not be found. Try again!')
    delete_worker()

def promote():
    list_all_workers()
    promotion = input("Choose worker's ID to promote: ")
    for i in managers:
        if promotion == i.employee_id:
            new_key = list(positions_managers.keys()).index(i.position) + 1
            if 0 <= new_key < 7:
                i.promote(list(positions_managers.keys())[new_key], list(positions_managers.values())[new_key])
                print(f"The manager has been promoted! He is now a/an {list(positions_managers.keys())[new_key]} and earns {list(positions_managers.values())[new_key]} zł")
                menu()            
            elif new_key == 7:
                print("The manager is the CEO. He cannot be promoted.")
                menu()
            else:
                print("Incorrect value! Try again.")
                promote()        
                
    for y in employees:
        if promotion == y.employee_id:
            new_key = list(positions_employees.keys()).index(y.position) + 1
            if 0 <= new_key < 7:
                y.promote(list(positions_employees.keys())[new_key], list(positions_employees.values())[new_key])
                print(f"The employee has been promoted! He is now a/an {list(positions_employees.keys())[new_key]} and earns {list(positions_employees.values())[new_key]} zł")
                menu()   
            elif new_key == 7:         
                print("This employee has been moved to managers")
                manager_id = input("Choose the ID for a new manager: ")
                while True:
                    if re.match ("^[6][0-9][0-9][0-9]$", manager_id):
                        break
                    else:
                        print("Manager's company ID is incorrect. Try again!")
                        manager_id = input("Choose the ID for a new manager: ")
                decision = input("Board membership: Press y/n: ").lower()
                if decision == 'y':
                    board = "Yes"
                elif decision == 'n':
                    board = 'No'
                managers.append(Managers(manager_id, y.first_name, y.last_name, list(positions_managers.values())[0], y.street_name, y.zip_code, y.city, list(positions_managers.keys())[0], y.nationality, board))
                employees.remove(y)
                menu()
            else:
                print("Incorrect value! Try again.")
                promote() 
    print("Incorrect value. Try again")
    promote()

def personal_data():
    print("\n")
    print("Changing personal data:")
    print("Press 1 to change manager's/employee's home address")
    print("Press 2 to change manager's/employee's last name")
    print('\n')
    decision = input("Press an appropriate key: ")
    if decision == '1':
        list_all_workers()
        emp = input("Choose employee's ID: ")
        for i in managers + employees:
            if i.employee_id == emp:
                street_name = input("Insert new address (the name of the street): ")
                zip_code = input("Insert new address (zip code): ")
                while True:
                    if re.match ("^[0-9][0-9]-[0-9][0-9][0-9]$", zip_code):
                        break
                    else:
                        print("Zip code is incorrect. Try again!")
                        zip_code = input("Insert manager's address (zip code): ")
                city = input("Insert new address (city): ")
                i.change_address(street_name, zip_code, city)
                print("The home address has been changed.")
                input("Press any key to go back to menu: ")
                menu()
        print("No worker has been found. Try again!")
        personal_data()
    elif decision == '2':
        list_all_workers()
        emp = input("Choose employee's ID: ")
        for i in managers + employees:
            if i.employee_id == emp:
                last_name = input("Insert new last name: ")
                i.change_lastname(last_name)
                print("The last name has been changed.")
                input("Press any key to go back to menu: ")
                menu()
        print("No worker has been found. Try again!")
        personal_data()
    else:
        print("Invalid value. Try again!")
        personal_data()

def give_raise():
    print('\n')
    if len(managers) == 0:
        print("There are no active managers to give raise to")
        input("Press any key to go back to menu: ")
        menu()
    for y in managers:
        print(f"ID: {y.employee_id}: {y.first_name} {y.last_name}")
    print('\n')
    id = input("Choose manager's ID to give raise to: ")
    for i in managers:
        if id == i.employee_id:
            bonus = int(input("How much raise does the manager get?: "))
            i.salary = i.salary + bonus 
            print(f'{i.first_name} {i.last_name} earns {i.salary} PLN now')
            menu()
    print("Invalid value. Try again!")
    give_raise()

def menu():
    print("\n")
    print("Employee Management Tool")
    print("What do you want to do? Press a given number:")
    print("press 1 to display employees and managers")
    print("press 2 to display all managers")
    print("press 3 to display all emoloyees")
    print("press 4 to to add an emlpoyee/manager")
    print("press 5 to remove an employee/manager")
    print("press 6 to promote an emloyee/manager")
    print("press 7 to change emloyee's/manager's personal data")
    print("press 8 to give a bonus to a manager")
    print("press 9 to exit")

    try:
        press = int(input("Press a given number: "))
        if press == 1:
            show_all()
        elif press == 2:
            show_managers()
        elif press == 3:
            show_employees()
        elif press == 4:
            add_worker()
        elif press == 5:
            delete_worker()
        elif press == 6:
            promote()
        elif press == 7:
            personal_data()
        elif press == 8:
            give_raise()
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
