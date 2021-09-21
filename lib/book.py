from bs4 import BeautifulSoup

class Book:
    def __init__(self, post_header):
        ref_elem = post_header.find('a')
        self.url = ref_elem['href']
        print(self.url)
