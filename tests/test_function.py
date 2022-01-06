from app.function import func


def test_func():
    assert 0 == func(0)
    assert 1 == func(1)
    assert 1 == func(-1)
    assert 4 == func(2)
    assert 9 == func(-3)


