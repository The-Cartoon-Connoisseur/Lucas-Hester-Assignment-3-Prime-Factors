#Test 1
import pytest
import prime

def test_not_integer_value_error():
    my_string = "string"
    my_float = 5.2
    with pytest.raises(ValueError):
        prime.generate_prime_factors(my_string)
    with pytest.raises(ValueError):
        prime.generate_prime_factors(my_float)

#Test 2
def test_prime_factors_empty_list_1():
    my_test_empty_list = []
    assert my_test_empty_list == prime.generate_prime_factors(1)