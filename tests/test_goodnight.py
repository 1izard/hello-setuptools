from greetpy import goodnight


def test_goodnight():
    assert goodnight.goodnight() == 'Good night...'
