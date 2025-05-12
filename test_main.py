import pytest
from main import hello


def test_hello():
    assert hello() == "Hello, GitHub Actions!"


def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI!"


def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)
