from calculadora import Calculadora, increment


def test_initial_value():
    calc = Calculadora()
    assert calc.total == 0


def test_subtract_one():
    calc = Calculadora()
    calc.set(1)
    calc.sub()
    assert calc.total == -1


def test_add_one():
    calc = Calculadora()
    calc.set(1)
    calc.add()
    assert calc.total == 1


def test_add_one_and_one():
    calc = Calculadora()
    calc.set(1)
    calc.add()
    calc.set(1)
    calc.add()
    assert calc.total == 2
