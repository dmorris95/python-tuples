#Task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_new_book(title, author, exist_lib):
    flag = False
    for book in exist_lib:
        if title in book and author in  book:
            #some books have the same title but different authors
            print("That book already exists!")
            flag = True
    if flag == False:
        library.append((title, author))

add_new_book("Red Fish", "Dr. Suess", library)
print(library)