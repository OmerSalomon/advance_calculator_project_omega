import pytest
from main import evaluate_exp, get_operator_dict

@pytest.mark.parametrize(
    'input_n, expected',
    [
        ('5+5', 10),
        ('3*3', 9),
        ('5-2', 3),
        ('555##', 6),
        ('3+-3^2', )
    ]
)
def test_evaluate_exp(input_n, expected):
    op_dict = get_operator_dict()
    assert evaluate_exp(input_n, op_dict) == expected
