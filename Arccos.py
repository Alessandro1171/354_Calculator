from HelperFunctions import truncate_value, abs,square_root_calculator

def arccos(x):
    if x > 1 or x < -1:
        return float("nan")  # Return NaN for out-of-bounds inputs
    else:
        negate = float(x < 0)
        x = abs(x)
        ret = -0.0187293
        ret = ret * x
        ret = ret + 0.0742610
        ret = ret * x
        ret = ret - 0.2121144
        ret = ret * x
        ret = ret + 1.5707288
        ret = ret * square_root_calculator(1.0 - x)
        ret = ret - 2 * negate * ret

        return truncate_value(negate * 3.14159265358979 + ret)
