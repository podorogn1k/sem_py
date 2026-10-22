from re import *

st = input()
dates = findall(r"\d{2}\.\d{2}\.\d{4}", st)
for i in dates:
    print(i)