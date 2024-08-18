import pytest
import time
import source.fn_functions as fn_functions

def test_add():
    assert fn_functions.add(2, 3) == 5

def test_subtract():
    assert fn_functions.subtract(5, 3) == 2

def test_multiply():
    assert fn_functions.multiply(2, 3) == 6

def test_divide():
    assert fn_functions.divide(6, 3) == 2.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        fn_functions.divide(6, 0)

def test_invalid_operation():
    with pytest.raises(TypeError):
        fn_functions.add(2, '3')

@pytest.mark.slow
def test_very_slow_operation():
    time.sleep(10)
    result = fn_functions.divide(6, 3)
    assert result == 2.0

@pytest.mark.skip(reason="this feature is currently broken")
def test_skipped_operation():
    assert False

@pytest.mark.xfail(reason="divide by zero")
def test_zero_divide_operation():
    fn_functions.divide(1, 0)