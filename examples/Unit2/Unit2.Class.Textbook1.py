class TextBook():
    def print_book_title(self, title):
        print(title)
def main():
    # object text_book is the instant of the class TextBook():
    text_book = TextBook()
    book_title = "Programming with Python"
    # calling print_book_title() method
    text_book.print_book_title(book_title)
if __name__ == '__main__':
    main()