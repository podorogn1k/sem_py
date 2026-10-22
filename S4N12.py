from re import *

with open('12.txt', encoding='utf-8') as f:
    info = f.read()
    lines = findall(r"\b[\w\.-_]+@[\w\.-_]+\.\w+\b", info)
    for i in set(lines):
        print(i)