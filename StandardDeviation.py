from array import array


def square_root_calculator(squared_number):
    """calculates the square root of the number"""
    if squared_number == 0 or squared_number == 1:
        return squared_number
    two_number_parts = str(float(squared_number)).split('.')
    before_decimal = two_number_parts[0]
    pairs_after_decimal = []
    pairs_before_decimal = pair_part1(before_decimal)
    # divides number into pairs of two numerals
    if len(two_number_parts) >= 2:
        after_decimal = two_number_parts[1]
        pairs_after_decimal = pair_part2(after_decimal)
    else:
        pairs_after_decimal = None

    root = 0
    main_number = ""
    # calculates square root for numbers before the decimal
    for pair in pairs_before_decimal:
        main_number = str(main_number) + pair
        temp = get_highest_divider((root * 2), int(main_number))
        subtractor = "" + str((root * 2)) + str(temp)
        subtractor = int(subtractor) * temp
        main_number = int(main_number) - subtractor
        root = "" + str(root) + str(temp)
        root = int(root)
    # return square root if the number is a prefect square
    if main_number == 0 and pairs_after_decimal is None:
        return float(root)
    else:
        root_decimal = ""
        # calculates square root for numbers after the decimal
        if pairs_after_decimal:
            for pair in pairs_after_decimal:
                main_number = str(main_number) + pair
                temp_divider = "" + str(root) + str(root_decimal)
                temp_divider = int(temp_divider) * 2
                temp = get_highest_divider(temp_divider, int(main_number))
                subtractor = "" + str(temp_divider) + str(temp)
                subtractor = int(subtractor) * temp
                main_number = int(main_number) - subtractor
                root_decimal = "" + str(root_decimal) + str(temp)
            if main_number == 0 or len(root_decimal) >= 5:
                return float((str(root) + "." + root_decimal))

        next_pair = "00"
        # calculates square root until 5 decimal accuracy
        while main_number != 0 and len(root_decimal) < 5:
            main_number = str(main_number) + next_pair
            temp_divider = "" + str(root) + root_decimal
            temp_divider = int(temp_divider) * 2
            temp = get_highest_divider(temp_divider, int(main_number))
            subtractor = "" + str(temp_divider) + str(temp)
            subtractor = int(subtractor) * temp
            main_number = int(main_number) - subtractor
            root_decimal = "" + str(root_decimal) + str(temp)
        return float((str(root) + "." + root_decimal))


def get_highest_divider(current_divider, current_number):
    """find the largest number you can divide from the current number"""
    if current_number < 1:
        return 0
    counter = 1
    subtracking_value = 1.00
    while subtracking_value < current_number:
        temp = "" + str(current_divider) + str(counter)
        temp = int(temp)
        subtracking_value = temp * counter
        counter = counter + 1
    counter = int(counter) - 2
    return counter


def pair_part1(before_decimal):
    """divides all the numerals for the given number into pairs of two adds zero at the end for even"""
    array_of_pairs = []
    # adds zero at the start if the number is odd
    if len(before_decimal) % 2 != 0:
        first_character = "0" + before_decimal[: 1]
        before_decimal = before_decimal[1:]
        array_of_pairs.append(first_character)
    else:
        first_two_character = before_decimal[: 2]
        before_decimal = before_decimal[2:]
        array_of_pairs.append(first_two_character)
    while before_decimal != "":
        character_pair = before_decimal[: 2]
        before_decimal = before_decimal[2:]
        array_of_pairs.append(character_pair)
    return array_of_pairs


def pair_part2(after_decimal):
    """divides all the numerals for the given number into pairs of two adds zero at the end for odd"""
    array_of_pairs = []

    while len(after_decimal) > 1:
        character_pair = after_decimal[: 2]
        after_decimal = after_decimal[2:]
        array_of_pairs.append(character_pair)
    # adds zero at the end if the number is odd
    if len(after_decimal) == 1:
        array_of_pairs.append((after_decimal + "0"))
    return array_of_pairs


def check_decimal(x):
    """checks as number has less than 5 decimals"""
    decimal_digits = len(str(x).split('.')[1])
    if decimal_digits > 5:
        return True
    else:
        return False


def standard_deviation(standard_deviation_input: array):
    """gets the standard deviation of a given array of numbers"""
    n = len(standard_deviation_input)
    mean = 0.0
    # gets mean of arrays
    for x in standard_deviation_input:
        mean += float(x)
    total_sum = 0.0
    mean = float(mean) / len(standard_deviation_input)
    # gets sum of all values (xi - mean)
    for x in standard_deviation_input:
        temp = (float(x) - mean)
        total_sum += (temp * temp)
    standard_deviation_value = total_sum / n
    standard_deviation_value = square_root_calculator(standard_deviation_value)
    if check_decimal(standard_deviation_value):
        standard_deviation_value = round(standard_deviation_value, 5)
    return standard_deviation_value

