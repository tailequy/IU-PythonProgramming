class TextBook():
    def __init__(self, pages_number=None):
        if pages_number is not None:
            self.pages_number = pages_number
        else:
            self.pages_number = None
    def print_book_title(self, book_title):
        print(book_title)
    def print_book_pages_number(self):
        if self.pages_number is not None:
            print("The number of pages is: {}".format(self.pages_number))
def main():
    pages_number = 300
    # object text_book is the instant of the class TextBook():
    text_book = TextBook(pages_number)
    book_title = "Programming with Python"
    # calling print_book_title() method
    text_book.print_book_title(book_title)
    # calling print_book_pages_number method
    text_book.print_book_pages_number()
if __name__ == '__main__':
    main()