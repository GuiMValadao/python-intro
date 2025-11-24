# from calculadora import Calculadora, increment


# def test_initial_value():
#     calc = Calculadora()
#     assert calc.total == 0


# def test_subtract_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.sub()
#     assert calc.total == -1


# def test_add_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.add()
#     assert calc.total == 1


# def test_add_one_and_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.add()
#     calc.set(1)
#     calc.add()
#     assert calc.total == 2

from typing import Literal
import pytest
from calculadora import Calculadora


@pytest.fixture(scope="session", autouse=True)
def session_scope_fixture():
    print("\nsession_scope_fixture")
    yield
    print("exiting session fixture")


@pytest.fixture(scope="module", autouse=True)
def module_scope_fixture():
    print("module_scope_fixture")
    yield
    print("exiting module fixture")


@pytest.fixture(scope="class", autouse=True)
def class_scope_fixture():
    print("class_scope_fixture")
    yield
    print("exiting class fixture")


@pytest.fixture()
def calculadora():
    """Retorna uma instância de Calculadora"""
    print("calculadora fixture")
    return Calculadora()


def test_initial_value(calculadora: Calculadora):
    print("\ninitial_value")
    assert calculadora.total == 0


def test_add_one(calculadora: Calculadora):
    print("\nadd_one")
    calculadora.set(1)
    calculadora.add()
    assert calculadora.total == 1


def test_subtract_one(calculadora: Calculadora):
    print("\nsubtract_one")
    calculadora.set(1)
    calculadora.sub()
    assert calculadora.total == -1


def test_add_one_and_one(calculadora: Calculadora):
    print("\nadd_one_and_one")
    calculadora.set(1)
    calculadora.add()
    calculadora.set(1)
    calculadora.add()
    assert calculadora.total == 2


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (3, 1, 4),
        (3, 2, 5),
    ],
)
def test_calculadora_add_operacao(
    calculadora: Calculadora,
    input1: Literal[3],
    input2: Literal[1] | Literal[2],
    expected: Literal[4] | Literal[5],
):
    calculadora.set(input1)
    calculadora.add()
    calculadora.set(input2)
    calculadora.add()
    assert calculadora.total == expected


@pytest.mark.skip(reason="not implemented yet")
def test_calculator_multiply(calculadora: Calculadora):
    calculadora.multiply(2, 3)
    assert calculadora.total == 6
