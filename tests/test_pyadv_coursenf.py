from pyadv_coursenf import algos

def test_add_one():
    out = algos.add_one(1)
    assert out == 2

def test_add_two():
    out = algos.add_two(1)
    assert out == 3

def test_add_three():
    out = algos.add_three(1)
    assert out == 4
