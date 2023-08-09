# the list with words from string
# please, do not modify it
some_iterable = input().split()
some_iterable_upper = []

for iterable in some_iterable:
    some_iterable_upper.append(iterable.upper())

iterable_dict = dict.fromkeys(some_iterable_upper)

for iterable in some_iterable_upper:
    iterable_dict[iterable] = iterable.lower()

print(iterable_dict)

# use dictionary comprehension to create a new dictionary
