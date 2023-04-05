# This file contains re-usable helper functions that were create to facilitate the creation of the special functions

def truncate_value(value):
    # truncates value to 5 values after decimal point
    if value.is_integer():
        return int(value)
    else:
        return float("{:.5f}".format(value))


def abs(value):
    if value < 0:
        return -value

    return value


def floor(x):
    if x >= 0:
        return int(x)
    else:
        return int(x) - 1


def ln(x, rounds):
    """Calculate ln(x)

    ln(x) = 2 [ (x-1)/(x+1)  + (1/3)( (x-1)/(x+1) )^3 + (1/5) ( (x-1)/(x+1) )^5 + (1/7) ( (x-1)/(x+1) )^7 + ... ]
    source: http://math2.org/math/expansion/log.htm

    """

    result = 0
    term_constant = (x - 1) / (x + 1)

    for i in range(1, rounds, 2):
        result += ((power(term_constant, i)) * (1 / i))

    return 2 * result


def power(base, exponent):
    result = 1

    for i in range(abs(exponent)):
        result *= base

    if exponent < 0:
        result = 1.0 / result

    return result


def e_power_x(x, rounds):
    """Calculate e^x

    We use the Taylor series approximation eˣ = 1 + x + x²/2! + x³/3! + ...
    Add more terms to get a better approximation
    source: https://www.omnicalculator.com/math/e-power-x

    """
    result = 1.0
    factorial = 1.0

    for i in range(1, rounds):
        factorial *= i
        term = power(x, i) / factorial
        result += term

    return result
