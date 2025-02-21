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
def test_prime_factors_1_list():
    my_test_empty_list = []
    assert my_test_empty_list == prime.generate_prime_factors(1)

#Test 3
def test_prime_factors_2_list():
    my_test_list = [2]
    assert my_test_list == prime.generate_prime_factors(2)