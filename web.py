import urllib.request

response = urllib.request.urlopen('http://python.org')
contents = response.read()
print(contents)