from urllib.request import urlopen
import re


nextNothing = 82682
offset = 140
for i in range(400):
    response = urlopen("http://pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(nextNothing))
    page_source = response.read()
    nextNothing = re.search(r'(and the next nothing is) (\d{1,})', str(page_source))
    if nextNothing != None:
        print(nextNothing.group(2) + " Count: "+str(i+offset))
        nextNothing = nextNothing.group(2)

    else:
        print("No matches found. This is the page source that was read: " + str(page_source))
        break



