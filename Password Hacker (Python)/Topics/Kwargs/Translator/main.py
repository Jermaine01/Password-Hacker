def translate(**kwargs):
    for word in kwargs:
        print(word, ":", kwargs[word])


words = {"mother": "madre", "father": "padre",
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
