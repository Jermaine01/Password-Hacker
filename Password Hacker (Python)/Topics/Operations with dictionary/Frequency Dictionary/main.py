# put your python code here
string = input()
string_lower = string.lower()
string_list = string_lower.split()
reduced_string = []

for word_one in string_list:
    if reduced_string.__contains__(word_one):
        pass
    else:
        reduced_string.append(word_one)

string_dictionary = dict.fromkeys(string_list, 0)
for word_two in string_list:
    string_dictionary[word_two] += 1

for amount in string_dictionary:
    print(amount + ' ' + str(string_dictionary[amount]))
