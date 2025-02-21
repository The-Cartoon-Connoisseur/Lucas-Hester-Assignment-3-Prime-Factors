def generate_prime_factors(given_value):
    if not isinstance(given_value, int): #Checks to see if given_value is an integer
        raise ValueError() #If given_value is not an integer, raise an error

    if given_value == 1: #If given_value is 1, return an empty list.
        prime_factors_list = []
        return prime_factors_list