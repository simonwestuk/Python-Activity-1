from Python_Activity_1 import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    # For testing expected exceptions with pytest, use pytest.raises
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    # If you are handling division by zero within the divide function and returning 'Error: Division by Zero'
    assert divide(10, 0) == 'Error: Division by Zero'
