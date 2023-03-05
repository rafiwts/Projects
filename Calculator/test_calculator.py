from calculator import *
import pytest

@pytest.fixture
def class_object():
    return Calculator(10)


@pytest.fixture
def calculator_minus_ten():
    class_object = Calculator(-10)
    return class_object.number


@pytest.fixture
def calculator_minus_five():
    class_object = Calculator(-5)
    return class_object.number


@pytest.fixture
def calculator_zero():
    class_object = Calculator()
    return class_object.number


@pytest.fixture
def calculator_five():
    class_object = Calculator(5)
    return class_object.number


@pytest.fixture
def calculator_ten():
    class_object = Calculator(10)
    return class_object.number


def test_addition(
        calculator_minus_ten,
        calculator_minus_five,
        calculator_zero,
        calculator_five,
        calculator_ten
    ):  

    assert calculator_five + 20 == 25
    assert calculator_minus_five + 3 == -2
    assert calculator_zero + 22 == 22
    assert calculator_minus_ten + 10 == 0
    assert calculator_ten + 50 == 60


def test_subtraction(
        calculator_minus_ten,
        calculator_minus_five,
        calculator_zero,
        calculator_five,
        calculator_ten
    ):  

    assert calculator_five - 50 == -45
    assert calculator_minus_five - 7 == -12
    assert calculator_zero - 10 == -10
    assert calculator_minus_ten - 20 == -30
    assert calculator_ten -5 == 5


def test_multiplication(
        calculator_minus_ten,
        calculator_minus_five,
        calculator_zero,
        calculator_five,
        calculator_ten
    ):  

    assert calculator_five * 50 == 250
    assert calculator_minus_five * 3 == -15
    assert calculator_zero * 110 == 0
    assert calculator_minus_ten * 2.5 == -25
    assert calculator_ten * 7.5 == 75


def test_division(
        calculator_minus_ten,
        calculator_minus_five,
        calculator_zero,
        calculator_five,
        calculator_ten
    ):  

    assert calculator_five / 5 == 1
    assert calculator_minus_five / 2 == -2.5
    assert calculator_zero / 40 == 0
    assert calculator_minus_ten / 10 == -1
    assert calculator_ten / 5 == 2


def test_division_by_zero(calculator_five):
    with pytest.raises(ZeroDivisionError):
        calculator_five / 0


def test_list_of_values(class_object):
    class_object + 10
    class_object - 10
    class_object / 10
    class_object * 10
    class_object + 20
    class_object - 20
    class_object / 20
    class_object * 20
    class_object + 50
    class_object - 50
    class_object / 50
    class_object * 50
    class_object + 100
    class_object - 100
    class_object / 100
    class_object * 100

    assert class_object.list_of_values == [
        20,
        0,
        1,
        100,
        30,
        -10,
        0.5,
        200,
        60,
        -40,
        0.2,
        500,
        110,
        -90,
        0.1,
        1000
    ]


def test_dict_of_values(class_object):
    class_object + 30
    class_object - 30
    class_object / 10
    class_object * 30
    class_object + 60
    class_object - 60
    class_object / 5
    class_object * 60

    assert class_object.dict_of_values == {
        1: 40,
        2: -20,
        3: 1,
        4: 300,
        5: 70,
        6: -50,
        7: 2,
        8: 600
    }


def test_sum_and_count_calls(class_object):
    class_object + 30
    class_object - 30
    class_object / 10
    class_object * 30
    class_object + 60
    class_object - 60
    class_object / 5
    class_object * 60

    assert class_object.sum == 943
    assert class_object.count_calls == 8










