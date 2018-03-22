import random

"""
    将一个厂url转为短链的方法
    https://leetcode.com/problems/encode-and-decode-tinyurl/description/
"""
class Codes:
    def __init__(self):
        self.map = {}
        self.num_map = {}
        self.BASE = "https://leetcode.com/"

    def encode(self, url):
        if url in self.map:
            return self.map[url]
        set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        key = ""
        exist = True
        while exist:
            for i in range(0, 6):
                index = random.randint(0, set.__len__() - 1)
                key = key + set[index]
            if key in self.num_map:
                exist = True
            else:
                exist = False
        self.num_map[key] = url
        self.map[url] = key
        return self.BASE + key

    def decode(self, url):
        return self.num_map[url.replace(self.BASE, "")];


code = Codes()
url = "https://leetcode.com/problems/design-tinyurl";
tinyUrl = code.encode(url)
print(tinyUrl)
print(code.decode(tinyUrl))
