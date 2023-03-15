# Function - y = ab^x

def check_decimal(x):
    decimal_digits = len(str(x).split('.')[1])
    if decimal_digits > 5:
        return True
    else:
        return False

def exponential_function(base=float, exponent=float):
    if base == 0:
        return 0
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif 0 < exponent < 1:
        #TO CONTINUE
        return exponential_function(base, exponent/2)*exponential_function(base, exponent/2)
    elif exponent < 0:
        return exponential_function(1 / base, -exponent)
    elif exponent % 2 == 0:
        half_exp = exponential_function(base, exponent / 2)
        return half_exp * half_exp
    else:
        half_exp = exponential_function(base, (exponent - 1) / 2)
        return base * half_exp * half_exp

    # result = 1
    # if base > 0 and power > 0:
    #     for index in range(math.floor(power)):
    #         result = result * base
    #     decimal = power - int(power)
    #     fraction = decimal.as_integer_ratio()
    #     result = result + exp(log(base)/fraction[1])
    #     return result
    # if base > 0 and power < 0:
    #     for index in range(-power):
    #         result = result * base
    #     return result
    # if base < 0 and power > 0:
    #     for index in range(power):
    #         result = result * base
    #     return result
    # if base < 0 and power < 0:
    #     for index in range(power):
    #         result = result * base
    #     return result
    # if power == 0:
    #     return 1


x = exponential_function(2, 0.5)
print(x)
