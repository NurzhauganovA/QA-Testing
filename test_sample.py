def func():
    x = [0, 2, 4, 6, 8]
    return x


def test_answer():
    assert func() == [i for i in range(10) if i % 2 == 0]