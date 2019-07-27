#from urllib import request
from urllib.request import urlopen
from urllib.parse import *

#-- urlopen function
#request_url = urlopen("https://www.geeksforgeeks.org/python-urllib-module/")
#print(request_url.read())

#-- urlparse

parse_url = urlparse("https://www.geeksforgeeks.org/python-urllib-module/")
print(parse_url)

#-- urlsplit is same as urlparse expect that it doesnt split params
split_url = urlsplit("https://www.geeksforgeeks.org/python-urllib-module/")
print(split_url)

#--urlunparse

unparse_url = urlunparse(parse_url)
print(unparse_url)

#---urlunsplit

unsplit_url = urlunsplit(split_url)
print(unsplit_url)

#-- urllib.parse.urldeflag - if url contains a fragment the it returns a url by removing fragment

#--- urllib.error module is used for exceptions raised

#--- urllib.robotparser for parsig robot.txt files
