import urllib.request
from bs4 import BeautifulSoup


def main():
    site = 'http://www.yac8.com/'
    url = site + "news/list_136.html"
    respone = urllib.request.urlopen(url)
    contents = respone.read()
    soup = BeautifulSoup(contents, 'html5lib')
    dict = {}
    for link in soup.find_all('img'):
        title = link.get('title')
        if title != '置顶' and title != None:
            dict[title] = link.get("src")

    for x in dict:
        v = dict.get(x)
        r = urllib.request.urlopen(site + v[3:])
        contents = r.read()
        f = open(x + ".jpg", 'wb')
        f.write(contents)
        f.close()


if __name__ == '__main__':
    main()
