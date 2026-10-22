from re import *

st = input()
numbers = findall(r"(?:\+7|8) (?:\(\d{3}\)|\d{3}) \d{3}-\d{2}-\d{2}", st)
for i in numbers:
    print(i)