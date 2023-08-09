# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
test_list = list(test_dict)
dict_list = []

for value in test_dict:
    dict_list.append(test_dict[value])

index_min = dict_list.index(min(dict_list))
index_max = dict_list.index(max(dict_list))

print(f'min: {test_list[index_min]}')
print(f'max: {test_list[index_max]}')
