import operator
books_pages = []
for value in books:
    books_pages.append(books[value])
books_name = list(books)
shortest_index = books_pages.index(min(books_pages))
longest_index = books_pages.index(max(books_pages))
# find the shortest book and print its title
print(books_name[shortest_index])
# find the longest book and print its
print(books_name[longest_index])
