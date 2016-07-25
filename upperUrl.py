#coding: utf8

def upperUrl(url):

    new_url = url[::-1]
    pos = len(new_url) - new_url.find('/') + -1
    new_url = new_url[::-1][:pos]

    return new_url

# if __name__ == '__main__':
#     upperUrl('https://www.btcc.com/news/woshi')
