from ExponentialFunction import *

def log(x, base):

    rounds = int(x * 6)
    
    result = ln(x, rounds) / ln(base, 1000)
    final_result = truncate_value(result)
    return final_result

