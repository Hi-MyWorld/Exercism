def classify(number: int):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Find the proper divisors of the number
    proper_divisors = [
        value for value in range(1, number // 2 + 1) if number % value == 0
    ]

    # Calculate the sum of the divisors
    divisors_sum = sum(proper_divisors)

    # Classify the number as perfect, abundant, or deficient
    if divisors_sum == number:
        return "perfect"
    elif divisors_sum > number:
        return "abundant"
    else:
        return "deficient"
