from re import *

st = input()
url = findall(r"https?://[^\s,]+", st)
for i in url:
    print(i)
