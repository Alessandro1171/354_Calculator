# Function - y = sinh(x)

def exponential_function2(self, x):
    e_approx = 2.7182818284590452353602874713527
    result = 1
    term = 1
    i = 1
    while term != 0:
        term *= x / i
        result += term
        i += 1
    return result
