import pytest
from Employees import *

@pytest.fixture
def class_object_employee():
    return Employee(
       "3435",
       "Rafał",
       "Krupiński",
       25000,
       "Modra 42/5",
       "54-151",
       "Wrocław",
       "Developer",
       "PL"
    )

@pytest.fixture
def class_object_manager():
    return Manager(
       "6435",
       "Maciek",
       "Bakowicz",
       150000,
       "Bierutowska 42/5",
       "50-121",
       "Wrocław",
       "Senior Developer",
       "PL",
       "Yes"
    )


def test_employee(class_object_employee):
    assert class_object_employee.employee_id == "3435"
    assert class_object_employee.first_name == "Rafał"
    assert class_object_employee.last_name == "Krupiński"
    assert class_object_employee.salary == 25000
    assert class_object_employee.street_name == "Modra 42/5"
    assert class_object_employee.zip_code == "54-151"
    assert class_object_employee.city == "Wrocław"
    assert class_object_employee.position == "Developer"
    assert class_object_employee.nationality == "PL"


def test_manager(class_object_manager):
    assert class_object_manager.employee_id == "6435"
    assert class_object_manager.first_name == "Maciek"
    assert class_object_manager.last_name == "Bakowicz"
    assert class_object_manager.salary == 150000
    assert class_object_manager.street_name == "Bierutowska 42/5"
    assert class_object_manager.zip_code == "50-121"
    assert class_object_manager.city == "Wrocław"
    assert class_object_manager.position == "Senior Developer"
    assert class_object_manager.nationality == "PL"
    assert class_object_manager.board == "Yes"


def test_mail(class_object_employee, class_object_manager):
    assert class_object_employee.mail() == "rafał.krupiński@developer.com"
    assert class_object_manager.mail() == "maciek.bakowicz@developer.com"


def test_adress(class_object_employee, class_object_manager):
    assert class_object_employee.address() == "Modra 42/5, 54-151, Wrocław" 
    assert class_object_manager.address() == "Bierutowska 42/5, 50-121, Wrocław"


def test_full_name(class_object_employee, class_object_manager):
    assert class_object_employee.full_name() == "Rafał Krupiński"
    assert class_object_manager.full_name() == "Maciek Bakowicz"


def test_promotion(class_object_employee, class_object_manager):
    class_object_employee.promote("Mid-Developer", 100000)
    class_object_manager.promote("Manager", 200000)

    assert class_object_employee.position == "Mid-Developer"
    assert class_object_employee.salary == 100000
    assert class_object_manager.position == "Manager"
    assert class_object_manager.salary == 200000


def test_change_address(class_object_employee, class_object_manager):
    class_object_employee.change_address("Bema 9/18", "50-265", "Warszawa")
    class_object_manager.change_address("Biskupia 2", "55-212", "Gdańsk")

    assert class_object_employee.street_name == "Bema 9/18"
    assert class_object_employee.zip_code == "50-265"
    assert class_object_employee.city == "Warszawa"
    assert class_object_employee.address() == "Bema 9/18, 50-265, Warszawa"
    assert class_object_manager.street_name == "Biskupia 2"
    assert class_object_manager.zip_code == "55-212"
    assert class_object_manager.city == "Gdańsk"
    assert class_object_manager.address() == "Biskupia 2, 55-212, Gdańsk"


def test_change_lastname(class_object_employee, class_object_manager):
    class_object_employee.change_lastname("Bakowicz")
    class_object_manager.change_lastname("Krupiński")

    assert class_object_employee.last_name == "Bakowicz"
    assert class_object_manager.last_name == "Krupiński"


def test_salary_bonus(class_object_manager):
    class_object_manager.give_raise(100000)

    assert class_object_manager.salary == 250000