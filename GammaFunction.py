from HelperFunctions import truncate_value, multi_factorial, e_power_x
from ExponentialFunction import exponential_function


def gamma(n):
    if n == 0 or n == 1:  # Base case for gamma
        return 1

    if int(n) == n:  # Deal with integers
        if n > 0:
            return multi_factorial(n - 1, 1)  # Positive integers are just (x-1)!
        else:
            return "Error, Invalid Input"  # Negative integers are undefined.

    # set up constants
    denominator = 1
    whole_number = int(n)
    decimal_number = n - whole_number

    # estimated value of gamma for each fraction from 1/2 to 1/8
    gamma_value = [1.7724538509055160273,
                   2.6789385347077476337,
                   3.6256099082219083119,
                   4.5908437119988030532,
                   5.5663160017802352043,
                   6.5480629402478244377,
                   7.5339415987976119047]

    if n > 0:  # Deal with positive decimal numbers

        # estimate fraction
        if decimal_number >= 1 / 2:
            denominator = 2
        elif decimal_number >= 1 / 3:
            denominator = 3
        elif decimal_number >= 1 / 4:
            denominator = 4
        elif decimal_number >= 1 / 5:
            denominator = 5
        elif decimal_number >= 1 / 6:
            denominator = 6
        elif decimal_number >= 1 / 7:
            denominator = 7
        elif decimal_number >= 1 / 8:
            denominator = 8

        gamma_fraction = gamma_value[denominator - 2]

        # Calculate the value of gamma using the formula gamma(n+ 1/q) = gamma(1/q) * (qn - n-1)!(q) / q^(n)
        # Equation found here:
        # https://en.wikipedia.org/wiki/Particular_values_of_the_gamma_function#General_rational_argument
        result = gamma_fraction \
            * multi_factorial(((denominator * whole_number) - denominator - 1), denominator) \
            / exponential_function(denominator, whole_number)

        result = truncate_value(result)

        return result

    else:  # Deal with negative decimal numbers
        # Uses the property that gamma(n) = 1/n * gamma(n+1), for all non-integers n < 0
        # Source:
        # https://math.stackexchange.com/questions/2204020/definition-of-the-gamma-function-for-non-integer-negative-values
        return (1 / n) * gamma(n + 1)
