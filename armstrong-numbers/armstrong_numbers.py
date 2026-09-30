def is_armstrong_number(number):

    # calculate the number of digits
    n_digits = len(str(number))

    # Extract the individual digits
    digits = [int(x) for x in str(number)]

    # Calculate the sum of powered digits
    sum_digits = sum(value**n_digits for value in digits)

    if sum_digits == number:
        return True
    else:
        return False
