"""Czy taka forma pytestu jest dobra?
Na co można zwrócić uwagę przy tworzeniu pytestu, jeżeli chodzi o "program"
który sworzyłem tutaj? :D"""
from main_file import *
import pytest


@pytest.fixture
def class_object():
    return Person(
        "mgr", 
        "Rafał", 
        "Krupiński", 
        "M", 
        "08/04/1995", 
        "Developer", 
        "DXC", 
        "rafiwts@gmail.com", 
        "https://www.dxc.com", 
        "95040810719", 
        "AX 2 213123",
        "10/09/2019",
        "10/09/2029"
    )


def test_checking_class_object(class_object):
    assert class_object.title == "mgr"
    assert class_object.name == "Rafał"
    assert class_object.surname == "Krupiński"
    assert class_object.gender == "M"
    assert class_object.birthdate == "08/04/1995"
    assert class_object.profession == "Developer"
    assert class_object.company == "DXC"
    assert class_object.email == "rafiwts@gmail.com"
    assert class_object.company_website == "https://www.dxc.com"
    assert class_object.id_number == "95040810719"
    assert class_object.passport_number == "AX 2 213123"
    assert class_object.issue_date == "10/09/2019"
    assert class_object.expiration_date == "10/09/2029"


def test_checking_class_method(class_object):
    assert class_object.list_of_attributes() == ["mgr", "Rafał", "Krupiński", "M", "08/04/1995", "Developer", "DXC", "rafiwts@gmail.com", "https://www.dxc.com", "95040810719", "AX 2 213123", "10/09/2019", "10/09/2029"]


def test_validating_dates():
    dates = [
        "31/08/1944",
        "01/10/1984", 
        "10/12/2011", 
        "02/02/2000", 
        "31/10/1936", 
        "09/05/1999", 
        "11/01/1977",
        "31/03/2003", 
        "09/11/2021", 
        "30/11/2022", 
        "22/04/1966", 
        "25/10/1988", 
        "04/08/2008",
        "31/12/2022",
        "02/01/1971"
    ]

    for date in dates:
        assert re.match(regex_date_validation, date) 


def test_validateint_emails():
    emails = [
        "rohan.singh99@example.at",
        "ra3ke5sh@example.com",
        "rsingh100@example.de",
        "rakeshs@example.com",
        "rakeshs@example.it",
        "another.example@example.pl",
        "will@gcflearnfree.org",
        "bhubbard511@yahoo.com",
        "jane-smith@gpa.com",
        "JohnS@contose.pl",
        "N.I.Ramesh@gre.ac.uk",
        "T.Ackroyd@gre.ac.uk",
        "Jeremy@moonyguitars.com",
        "bernie-reeder@yesware.pl.com",
        "h.reich321@widget.net"
    ]

    for email in emails:
        assert re.match(regex_email_validation, email)


def test_validating_websites():
    websites = [
        "https://www.somewebsite.org",
        "https://www.quackit.com",
        "http://www.google.com",
        "http://www.another-example.org",
        "http://www.computer-hope.com.uk",
        "https://www.paypal.account-update.mybank.net",
        "https://www.yoursite.com",
        "http://www.blog.hubspot.com",
        "https://www.this.is-example.pl.com",
        "http://www.abcnews.go.com"
    ]    

    for website in websites:
        assert re.match(regex_website_validation, website)


def test_passport_number_validation():
    passport_numbers = [
        "AX 2 321316",
        "BG 5 723476",
        "PQ 3 123133",
        "LL 0 413244",
        "ZA 0 421010",
        "AZ 1 013220",
        "XC 6 593211",
        "WF 9 392139",
        "YT 4 783219",
        "QW 9 310210",
        "VC 3 123111",
        "UI 1 900312",
        "PO 5 756753",
        "GF 8 804327",
        "SY 4 092349"
    ]

    for passport_number in passport_numbers:
        assert re.match(regex_passport_number_validation, passport_number)