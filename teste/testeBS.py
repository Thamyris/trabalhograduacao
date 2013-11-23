import urllib
from bs4 import BeautifulSoup

url = 'http://angelmasked.blogspot.com.br'
resp = urllib.urlopen(url).read()
soup = BeautifulSoup(resp,from_encoding ="UTF-8")
msg = soup.get_text()
print(msg)

