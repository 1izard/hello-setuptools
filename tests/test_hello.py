from greetpy import hello


def test_hello():
    assert hello.hello() == 'Hello!'
