from urllib.request import urlopen
from pprint import pprint

url_content = urlopen("https://api.github.com/users/mralexgray/repos")
#pprint(url_content.read())
print(url_content.read())
