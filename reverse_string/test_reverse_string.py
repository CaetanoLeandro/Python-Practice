from reverse_string.reverse_string import FirstReverse


def test_reverse_leandro():
    assert FirstReverse('leandro') == 'ordnael'

def test_reverse_123456789():
    assert FirstReverse('123456789') == '987654321'
