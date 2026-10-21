def power(x: int) -> int:
    return x * x


def square_root(number: int) -> int:
    if number < 0:
        raise ValueError("The number must be non-negative.")

    if number < 2:
        return number  # sqrt(0)=0, sqrt(1)=1

    x = number
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + number // x) // 2

    return x
