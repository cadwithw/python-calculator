# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, power

@pytest.mark.basic
def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

@pytest.mark.basic
def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1

@pytest.mark.basic
def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

@pytest.mark.basic
def test_divide():
    """Test division function."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

@pytest.mark.edge
def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.basic
def test_power():
    """Test power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9

@pytest.mark.edge
def test_power_edge_cases():
    """Test power function with edge cases."""
    assert power(0, 5) == 0
    assert power(1, 100) == 1
    assert power(10, -1) == 0.1

@pytest.mark.slow
def test_performance_large_numbers():
    """Test performance with large numbers."""
    assert add(10**6, 10**6) == 2 * 10**6
    assert multiply(1000, 1000) == 1000000
    assert power(2, 20) == 1048576

@pytest.mark.slow
def test_performance_multiple_operations():
    """Test performance with multiple sequential operations."""
    result = 0
    for i in range(1000):
        result = add(result, i)
    assert result == sum(range(1000))