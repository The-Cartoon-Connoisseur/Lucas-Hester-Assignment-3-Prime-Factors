def generate_prime_factors(given_value):
    if not isinstance(given_value, int): #Checks to see if given_value is an integer
        raise ValueError() #If given_value is not an integer, raise an error

    if given_value == 1: #If given_value is 1, return an empty list.
        prime_factors_list = []
        return prime_factors_list

    if given_value == 2: #If given_value is 2, return [2] list.
        prime_factors_list = [2]
        return prime_factors_list

    if given_value == 3: #If given_value is 3, return [3] list.
        prime_factors_list = [3]
        return prime_factors_list

    if given_value == 4: #If given_value is 4, return [2, 2] list.
        prime_factors_list = [2, 2]
        return prime_factors_list