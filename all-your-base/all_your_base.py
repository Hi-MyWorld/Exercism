def rebase(input_base: int, digits: list, output_base: int):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not digits or all(d == 0 for d in digits):
        return [0]

    number = sum(
        digit * input_base**power for power, digit in enumerate(reversed(digits))
    )
    
    power = 0
    while output_base**power <= number:
        power += 1

    limit = power - 1
    result = []
    while limit > 0:
        # calculate the quotient
        real_part = number // output_base**limit
        result.append(real_part)
        # calculate the remainder
        number = number % output_base**limit
        limit -= 1
    result.append(number)
    return result
