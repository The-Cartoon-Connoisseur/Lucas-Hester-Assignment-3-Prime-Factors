def generate_prime_factors(given_value):
    if not isinstance(given_value, int): #Checks to see if given_value is an integer
        raise ValueError() #If given_value is not an integer, raise an error