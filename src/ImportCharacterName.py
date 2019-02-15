import wget
import xml.etree.ElementTree as ET
import time
#from exceptions import UnicodeEncodeError


url_begin = 'https://www.giantbomb.com/api/character/3005-'
url_end = '/?api_key='
api_key = 'YOUR KEY HERE'


def create_url(i):
    return url_begin + str(i) + url_end + api_key

begin = 27001
end = 29000

for i in range(begin, end+1):
    url = create_url(i)
    print(url)
    filename = wget.download(url, '/tmp/')

    tree = ET.parse(filename)
    root = tree.getroot()

    name = ''
    real_name = ''

    for child in root:
        if child.tag == "results":
            for cchild in child:
                if cchild.tag == "name":
                    name = cchild.text

                if cchild.tag == "real_name":
                    real_name = cchild.text

    with open("CharactersDict.txt", "a") as myfile:
        try:
            myfile.write('\n' + name)
        except UnicodeEncodeError:
            pass
        if real_name:
            try:
                myfile.write('\n' + real_name)
            except UnicodeEncodeError:
                pass
    time.sleep(1)
