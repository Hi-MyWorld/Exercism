def is_valid(isbn: str):

    # Remove all hyphens from the ISBN
    clean_isbn = list(isbn.replace("-", ""))

    # Check that the ISBN contains exactly 10 characters
    if len(clean_isbn) != 10:
        return False

    # Check that the first nine characters are digits
    numbers = "1234567890"
    for value in clean_isbn[:9]:
        if value not in numbers:
            return False

    # Check that the last character is either a digit or 'X'
    if (clean_isbn[-1] != "X") and (clean_isbn[-1] not in numbers):
        return False

    # Reverse the list to calculate the checksum from right to left
    clean_isbn.reverse()

    # it means "X" is exist or not
    if clean_isbn[0] in numbers:
        isbn_sum_values = sum(
            (place + 1) * int(digit) for place, digit in enumerate(clean_isbn)
        )
    else:
        isbn_sum_values = (
            sum((place + 2) * int(digit) for place, digit in enumerate(clean_isbn[1:]))
            + 10
        )

    if isbn_sum_values % 11 == 0:
        return True
    else:
        return False
