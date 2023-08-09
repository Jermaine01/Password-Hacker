# put your python code here
def multiply(*args):
    product = 1
    if len(args) == 1:
        return args[0]
    else:
        for value in args:
            product *= value
    return product
