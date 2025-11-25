from calculadora import Calculadora
import pytest


@pytest.fixture()
def calculadora(valor1, valor2):
    """Retorna uma instância de Calculadora"""
    return Calculadora(valor1, valor2)


def test_soma():
    resultado = calculadora(operador="+")
    assert resultado == 2


def test_sub():
    resultado = calculadora(operador="-")
    assert resultado == 0


def test_mult():
    resultado = calculadora(operador="*")
    assert resultado == 1


def test_div():
    resultado = calculadora(operador="/")
    assert resultado == 1
