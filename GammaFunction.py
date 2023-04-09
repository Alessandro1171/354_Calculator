from HelperFunctions import truncate_value, multi_factorial
from ExponentialFunction import exponential_function


# TODO: FIX bug when working with decimals (causes error)
def gamma(n):
    if n == 0 or n == 1:  # Base case for gamma
        return 1

    if n.is_integer():  # Deal with integers
        if n > 0:
            return multi_factorial(n - 1, 1)  # Positive integers are just (x-1)!
        else:
            return "Error, Invalid Input"  # Negative integers are undefined.

    # set up constants
    denominator = 1
    denominator_digits = 1
    sqrtPI = 1.77245

    if n > 0:  # Deal with positive decimal numbers

        truncate_value(n)  # Truncate to have 5 decimals

        if n < 1:
            return sqrtPI

        for i in range(0, 5, 1):

            if n.is_integer():
                denominator_digits = i
                break
            else:
                n = 10
                denominator = 10

        return sqrtPI * multi_factorial(((denominator * n) - denominator - 1), denominator) / exponential_function(
            denominator, n)

    else:  # Deal with negative decimal numbers

        return (1 / n) * gamma(n + 1)
