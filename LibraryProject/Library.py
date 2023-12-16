library = []

def display_library():
    if len(library) == 0:
        print("\nYour library is empty.")

    else:
        print("\nYour Library:")
        id = 1
        for book in library:
            print("{}. Book: {}, Pages: {}, Bookmark: {}\n".format(id, book['name'], book['pages'], book['bookmark']))
            id += 1

def add_book():
    try:

        name = input("\nEnter the book name: ")
        pages = int(input("Enter the number of pages: "))
        book = {'name': name, 'pages': pages, 'bookmark': 0}
        library.append(book)
        print("\nBook '{}' added to your library.\n".format(name))

    except Exception as e:
        print("Error : ",e)

def update_bookmark():
    try:
        display_library()

        while True:
            try:
                book_choice = int(input("\nEnter the number of the book you want to update the bookmark for: "))
                if 1 <= book_choice <= len(library):
                    break
                else:
                    print("\nInvalid book number. Please enter a valid number.\n")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")

        book = library[book_choice - 1]
        pages = book['pages']

        while True:
            try:
                bookmark = int(input("Enter the current page number for '{}': ".format(book['name'])))
                if 0 <= bookmark <= pages:
                    break
                else:
                    print("\nInvalid bookmark number. It should be between 0 and {}.\n".format(pages))
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")

        book['bookmark'] = bookmark
        print("\nBookmark updated for '{}.'\n".format(book['name']))

    except Exception as e:
        print("Error: ", e)


def mark_as_completed():
    try:
        display_library()

        book_choice = int(input("\nEnter the number of the book you want to mark as completed: "))
        if 1 <= book_choice <= len(library):
            book = library[book_choice - 1]
            book['bookmark'] = book['pages']
            print("\nCongratulations! '{}' marked as completed.\n".format(book['name']))
        else:
            print("\nInvalid book number.\n")
    except ValueError:
        print("\nInvalid input. Please enter a valid number for the bookmark.\n")

def delete_book():
    try:
        display_library()

        book_choice = int(input("\nEnter the number of the book you want to delete: "))
        if 1 <= book_choice <= len(library):
            book = library[book_choice - 1]
            library.remove(book)
            print("\nBook '{}' deleted from your library.\n".format(book['name']))
        else:
            print("\nInvalid book number.\n")
    except Exception as e:
        print("Error: ",e)

while True:
    print("\nWelcome to your library!")
    print("1. Display Library")
    print("2. Add Book")
    print("3. Update Bookmark")
    print("4. Mark as Completed")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        display_library()
    elif choice == '2':
        add_book()
    elif choice == '3':
        update_bookmark()
    elif choice == '4':
        mark_as_completed()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print("\nGoodbye! Exiting the program.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.\n")
