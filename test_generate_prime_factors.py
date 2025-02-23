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

#Test 4
def test_prime_factors_3_list():
    my_test_list = [3]
    assert my_test_list == prime.generate_prime_factors(3)

#Test 5
def test_prime_factors_4_list():
    my_test_list = [2, 2]
    assert my_test_list == prime.generate_prime_factors(4)

#Test 6
def test_prime_factors_6_list():
    my_test_list = [2, 3]
    assert my_test_list == prime.generate_prime_factors(6)

#Test 7
def test_prime_factors_8_list():
    my_test_list = [2, 2, 2]
    assert my_test_list == prime.generate_prime_factors(8)

#Test 8
def test_prime_factors_9_list():
    my_test_list = [3, 3]
    assert my_test_list == prime.generate_prime_factors(9)