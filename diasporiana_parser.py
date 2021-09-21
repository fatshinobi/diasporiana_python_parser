import pdb
import time

from lib.page import Page

url = 'https://diasporiana.org.ua/page/'

for page_number in range(1, 10):
    time.sleep(1)
    print("Page: {}".format(str(page_number)))
    page_url = "{}{}/".format(url, str(page_number))
    print("Parsing url:{}".format(page_url))
    page = Page(page_url)

#pdb.set_trace()
