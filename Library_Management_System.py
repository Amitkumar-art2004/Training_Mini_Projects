import csv
def add_book():
    title = input("Enter book name: ")
    with open("books.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([title])
    print("Book Added!")

def search_book():
    try:
        with open("books.csv", "r",newline="") as file:
            reader = csv.reader(file)
            name = input("Enter book to search: ")
            found = False
            for row in reader:
                if row[0] == name:
                    found = True
                    break
            if found:
                print("Book Found")
            else:
                print("Book Not Found")
    except FileNotFoundError:
        print("File does not exist")
def remove_book():
    try:
        name = input("Enter book name to remove: ")
        books = []
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != name:
                    books.append(row)
        with open("books.csv", "w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(books)
        print("Book Removed")
        with open("books.csv", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File does not exist")
add_book()
search_book()
remove_book()
