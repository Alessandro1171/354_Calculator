# Function - y = ab^x

def print_exp():
    print("this is from exponentialFunction class")

def truncate_value(value):
    # truncates value to 5 values after decimal point
    final_value = '%.5f' % value
    return final_value


def check_decimal(num):
    if num < 0.0001:
        return 0.0001
    decimal_digits = len(str(num).split('.')[1])
    if decimal_digits > 5:
        final_num = truncate_value(num)
        return float(final_num)
    else:
        return num


def exponential_function(base=float, exponent_a=float):
    # TODO: CUT THE NUMBER TO MAX OF 5 AFTER DECIMAL POINT
    array = str(exponent_a).split('.')
    if len(array) == 2:
        # values after decimal exists
        exponent = check_decimal(exponent_a)
    else:
        exponent = exponent_a
    if base == 0:
        return 0
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif 0 < exponent < 1:
        # TO CONTINUE
        #return exponential_function(base, exponent / 2) * exponential_function(base, exponent / 2)
        #return base**exponent_a
        pass
    elif exponent < 0:
        return exponential_function(1 / base, -exponent)
    elif exponent % 2 == 0:
        half_exp = exponential_function(base, exponent / 2)
        return half_exp * half_exp
    else:
        half_exp = exponential_function(base, (exponent - 1) / 2)
        return base * half_exp * half_exp


#x = exponential_function(2, 1.0002)
#print(x)