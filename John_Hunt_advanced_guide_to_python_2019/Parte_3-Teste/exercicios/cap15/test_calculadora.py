from calculadora import Calculadora
import pytest


@pytest.fixture()
def calculadora():
    """Retorna uma instância de Calculadora"""
    return Calculadora()


@pytest.mark.parametrize(
    "input1, input2, expected",
    [(1, 1, 2), (-1, 1, 0), (10, 10, 20)],
)
def test_soma(calculadora: Calculadora, input1, input2, expected):
    calculadora.operador = "+"
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    soma = calculadora.realizar_operacao()
    assert soma == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (1, 1, 0),
        (-1, 1, -2),
        (20, 10, 10),
        (10, 20, -10),
    ],
)
def test_sub(calculadora: Calculadora, input1, input2, expected):
    calculadora.operador = "-"
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    subtracao = calculadora.realizar_operacao()
    assert subtracao == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (1, 1, 1),
        (-1, 1, -1),
        (5, 5, 25),
        (0, 10, 0),
    ],
)
def test_mult(calculadora: Calculadora, input1, input2, expected):
    calculadora.operador = "*"
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    mult = calculadora.realizar_operacao()
    assert mult == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [(1, 1, 1), (-1, 1, -1), (10, 2, 5), (10, 0, None)],
)
def test_div(calculadora: Calculadora, input1, input2, expected):
    calculadora.operador = "/"
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    div = calculadora.realizar_operacao()
    assert div == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [(1, 1, 4), (-1, 1, 0), (10, 10, 40)],
)
def test_memo(calculadora: Calculadora, input1, input2, expected):
    calculadora.operador = "+"
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    soma = calculadora.realizar_operacao()
    calculadora.mudar_total(soma)
    calculadora.mudar_total(soma)
    assert calculadora.total == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [(1, 1, 0), (-1, 1, 0), (10, 10, 0)],
)
def test_limpar_memo(calculadora: Calculadora, input1, input2, expected):
    calculadora.operador = "+"
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    soma = calculadora.realizar_operacao()
    calculadora.mudar_total(soma)
    calculadora.limpar_total()
    assert calculadora.total == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [("a", 1, (None, 1)), (-1, "v", (-1, None)), (10, 10, (10, 10))],
)
def test_inputs(calculadora: Calculadora, input1, input2, expected):
    calculadora.valor1 = input1
    calculadora.valor2 = input2
    valor1, valor2 = calculadora.valor1, calculadora.valor2
    assert (valor1, valor2) == expected


@pytest.mark.parametrize(
    "operador, expected",
    [("+", "+"), ("-", "-"), ("*" "*"), ("/", "/"), ("a", None), ("%", None)],
)
def test_inputs_operadores(calculadora: Calculadora, operador, expected):
    calculadora.operador = operador
    assert calculadora.operador == expected
