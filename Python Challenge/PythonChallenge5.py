from urllib.request import urlopen
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
text = urlopen(url).read()
print(pickle.load(text))
