import pytest
import time
from main import hello


def test_hello():
    assert hello() == "Hello, John Doe!"


def test_hello_custom_name():
    assert hello("Jane", "Smith") == "Hello, Jane Smith!"


def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123, "Smith")


def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("Jane", "Smith")
    duration = time.time() - start
    assert duration < 1
