from bs4 import BeautifulSoup
import time
import pdb

from lib.http_request import HttpRequest
from lib.book import Book

class Page:
    def __init__(self, page_url):
        request = HttpRequest()
        req = request.get(page_url)

        bs = BeautifulSoup(req.text, 'html.parser')

        books_list = bs.find_all('div', {'class':'book-details'})
        
        self.books = []

        for book_div in books_list:
            self.books.append(Book(book_div))

        for book in self.books:
            time.sleep(1)
            book.get_details()

            print("Code: {}".format(book.code))
            print("Name: {}".format(book.name))
            print("Author: {}".format(book.author))
            print("Published: {}".format(book.published))
            print("Publisher: {}".format(book.publisher))
