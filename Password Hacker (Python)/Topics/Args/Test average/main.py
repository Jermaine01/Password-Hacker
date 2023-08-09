def average_mark(*args):
    total = 0
    for number in args:
        total += number
    mean = round(total/len(args), 1)
    return mean
