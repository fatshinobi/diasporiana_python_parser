from bs4 import BeautifulSoup

from lib.http_request import HttpRequest
from lib.book import Book

class Page:
    def __init__(self, page_url):
        request = HttpRequest()
        req = request.get(page_url)

        bs = BeautifulSoup(req.text, 'html.parser')

        books_list = bs.find_all('div', {'class':'book-details'})
        for book_div in books_list:
            book = Book(book_div)