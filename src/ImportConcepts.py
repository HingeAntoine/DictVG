import wget
import xml.etree.ElementTree as ET
import time


url_begin = 'https://www.giantbomb.com/api/concept/3015-'
url_end = '/?api_key='
api_key = 'YOUR KEY HERE'


def create_url(i):
    return url_begin + str(i) + url_end + api_key

begin = 1
end = 2000

for i in range(begin, end+1):
    url = create_url(i)
    print(url)
    filename = wget.download(url, '/tmp/')

    tree = ET.parse(filename)
    root = tree.getroot()

    name = ''
    aliases = list()

    for child in root:
        if child.tag == "results":
            for cchild in child:
                if cchild.tag == "name":
                    name = cchild.text

                if (cchild.tag == "aliases") & (cchild.text is not None):
                    aliases.append(cchild.text)

    with open("ConceptDict.txt", "a") as myfile:
        try:
            myfile.write(name + '\n')
        except UnicodeEncodeError:
            pass
        if aliases:
            for alias in aliases:
                try:
                    myfile.write(alias + '\n')
                except UnicodeEncodeError:
                    pass
    time.sleep(1)
