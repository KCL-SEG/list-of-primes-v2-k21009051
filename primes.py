"""List of prime numbers generator."""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"{number_of_primes} needs to be a positive number!")

    list = []
    testing_number = 2

    while len(list) < number_of_primes:
        prime = True

        for i in range(2,(testing_number//2)+1):
            if testing_number % 1 == 0:
                prime = False
                break

        if prime == True:
            list.append(testing_number)
        testing_number += 1

    return list
