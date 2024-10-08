import pytest
from src.ejercicio01_def import introduce_nombre

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("     fwasd","fwasd"),
        ("gh    ","gh"),
        ("      hh    ","hh")
    ]
)

def test_mombre_params(input_x, expected):
    assert introduce_nombre(input_x) == expected