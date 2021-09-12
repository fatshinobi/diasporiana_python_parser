#from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pdb

session = requests.Session()

url = 'https://diasporiana.org.ua'

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
req = session.get(url, headers=headers)

bs = BeautifulSoup(req.text, 'html.parser')

books_list = bs.find_all('div', {'class':'book-details'})
for book_div in books_list:
  title = book_div.find('h2', {'class':'book-title'})
  #pdb.set_trace()
  print(title.get_text())