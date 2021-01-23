import urllib.request
import hashlib

def hashCode(url):
    contents = urllib.request.urlopen(url).read()
    hash256 = hashlib.sha3_256(contents).hexdigest()
    return hash256

k = hashCode("https://raw.githubusercontent.com/shashank-shekher/dummy-files/main/code.txt")
print(k)
