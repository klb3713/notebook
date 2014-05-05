import re
import urllib

next = "8022"
url = ""
response = ""
while next:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+next
    res = urllib.urlopen(url)
    response = res.read()

    # handle the solution (last) line
    if re.findall(r'\.html$', response):
        break
    
    code = re.findall(r'\d+$', response)

    if(code):
        next = code[0]
    else:
        # handle the divide by two line
        next = str (int (next) / 2 )

    print url
    print response