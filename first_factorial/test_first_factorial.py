from first_factorial.first_factorial import FirstFactorial


def test_factorial_4():
    assert FirstFactorial(4) == 24


def test_factorial_5():
    assert FirstFactorial(5) == 120


def test_factorial_6():
    assert FirstFactorial(6) == 720