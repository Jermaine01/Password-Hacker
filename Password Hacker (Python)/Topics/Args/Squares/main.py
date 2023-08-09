def sq_sum(*args):
    sum_squares = 0
    for number in args:
        sum_squares += number ** 2
    return sum_squares
