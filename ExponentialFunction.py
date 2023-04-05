from HelperFunctions import e_power_x, ln, power, truncate_value

# Constant defining how many rounds/terms to use for the infinite series. Increase this number for better accuracy.
ROUNDS = 100


def exponential_function(base, exponent):
    """ Calculates x^y by using the following property: x^y = e^(y * ln(x)) """

    int_part = int(abs(exponent))
    fractional_part = abs(exponent) - int_part

    calculated_value = e_power_x((fractional_part * ln(base, ROUNDS)), ROUNDS) * power(base, int_part)

    if base == 0:
        return 0
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent < 0:
        return truncate_value(1.0 / calculated_value)

    return truncate_value(calculated_value)
