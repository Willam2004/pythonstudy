from urllib import request
from requests_html import HTMLSession
import os
def download(args):
    v = ""
    u = request.urlopen(args)
    cat_img = u.read()
    filename = os.path.basename(args)
    with open(v + filename, 'wb') as f:
        f.write(cat_img)


session = HTMLSession()
url="https://www.sohu.com/a/195049321_717378"
r = session.get(url)
imgs = r.html.find('img')
for item in imgs:
        s = item.attrs['src']
        download(s)

