import tkinter as tk
from tkinter import simpledialog, messagebox

library = []

def display_library():
    if len(library) == 0:
        result_text.set("Your library is empty.")
    else:
        result_text.set("Your Library:\n")
        for id in range(len(library)):
            book = library[id]
            result_text.set(result_text.get() + "{}. Book: {}, Pages: {}, Bookmark: {}\n".format(id + 1, book['name'], book['pages'], book['bookmark']))

def add_book():
    try:
        name = simpledialog.askstring("Add Book", "Enter the book name:")
        pages = int(simpledialog.askstring("Add Book", "Enter the number of pages:"))
        book = {'name': name, 'pages': pages, 'bookmark': 0}
        library.append(book)
        result_text.set("Book '{}' added to your library.".format(name))
    except ValueError:
        result_text.set("Invalid input. Please enter a valid number for the number of pages.")

def update_bookmark():
    try:
        display_library()
        book_choice = int(simpledialog.askstring("Update Bookmark", "Enter the number of the book you want to update the bookmark for:"))
        if 1 <= book_choice <= len(library):
            book = library[book_choice - 1]
            pages = book['pages']
            bookmark = int(simpledialog.askstring("Update Bookmark", "Enter the current page number for '{}':".format(book['name'])))
            
            if 0 <= bookmark <= pages:
                book['bookmark'] = bookmark
                result_text.set("Bookmark updated for '{}'.".format(book['name']))
            else:
                result_text.set("Invalid bookmark number. It should be between 0 and {}.".format(pages))
        else:
            result_text.set("Invalid book number.")
    except ValueError:
        result_text.set("Invalid input. Please enter a valid number for the bookmark.")

def mark_as_completed():
    try:
        display_library()
        book_choice = int(simpledialog.askstring("Mark as Completed", "Enter the number of the book you want to mark as completed:"))
        if 1 <= book_choice <= len(library):
            book = library[book_choice - 1]
            book['bookmark'] = book['pages']
            result_text.set("Congratulations! '{}' marked as completed.".format(book['name']))
        else:
            result_text.set("Invalid book number.")
    except ValueError:
        result_text.set("Invalid input. Please enter a valid number for the bookmark.")

def delete_book():
    try:
        display_library()
        book_choice = int(simpledialog.askstring("Delete Book", "Enter the number of the book you want to delete:"))
        if 1 <= book_choice <= len(library):
            book = library[book_choice - 1]
            library.remove(book)
            result_text.set("Book '{}' deleted from your library.".format(book['name']))
        else:
            result_text.set("Invalid book number.")
    except ValueError:
        result_text.set("Invalid input. Please enter a valid number for the bookmark.")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Library Program")

result_text = tk.StringVar()

result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

button_display = tk.Button(root, text="Display Library", command=display_library)
button_display.pack()

button_add = tk.Button(root, text="Add Book", command=add_book)
button_add.pack()

button_update = tk.Button(root, text="Update Bookmark", command=update_bookmark)
button_update.pack()

button_mark_completed = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
button_mark_completed.pack()

button_delete = tk.Button(root, text="Delete Book", command=delete_book)
button_delete.pack()

button_exit = tk.Button(root, text="Exit", command=exit_program)
button_exit.pack()

root.mainloop()