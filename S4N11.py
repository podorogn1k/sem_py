from re import *

with open('11.txt') as f:
    info = f.read()
    users = findall(r"User (\d+)", info)
    print(*[int(n) for n in users])
    lines = findall(r".*ERROR.*", info)
    for i in lines:
        print(i)
    users_error = findall(r"ERROR User (\d+)", info)
    print(*[int(n) for n in users_error])