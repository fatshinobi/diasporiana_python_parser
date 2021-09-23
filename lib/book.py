from bs4 import BeautifulSoup
import pdb

from lib.http_request import HttpRequest

class Book:
    def __init__(self, post_header):
        ref_elem = post_header.find('a')
        self.url = ref_elem['href']
        parsed_uri = self.url.split('/')
        self.code = parsed_uri[-2]
        self.category = parsed_uri[-3]

    def get_details(self):
        request = HttpRequest()
        req = request.get(self.url)

        bs = BeautifulSoup(req.text, 'html.parser')

        book_details = bs.find('div', {'class':'book-details'})
        self.name = book_details.find('h1', {'class':'book-title'}).getText()

        attributes_list = book_details.find_all('p')
        self.author = self.__clear_pulled_string(attributes_list[0].getText())
        self.published = self.__clear_pulled_string(attributes_list[1].getText())
        self.publisher = self.__clear_pulled_string(attributes_list[3].getText())

    def __clear_pulled_string(self, str_val):
        return str_val.strip().replace('\t', '').replace('\n', '')
