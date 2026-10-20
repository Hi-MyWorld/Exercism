def steps(number):

    # example when argument is zero or a negative integer
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    # define a counter for steps
    counter = 0

    while number != 1:  # until the number doesn't equal to 1, run the task
        if number % 2 == 0:  # determine it is odd or even(in this condition is 'even')
            number = number / 2
        else:  # this is show the number is odd
            number = number * 3 + 1

        counter += 1

    return counter
