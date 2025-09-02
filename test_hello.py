from hello import say_hello, add, multiply

def test_say_hello():
    assert (
        say_hello("Annie")
        == "Hello, Annie, welcome to Data Engineering Systems (IDS 706)!"
    )


def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(5,10)==50