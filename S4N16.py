from re import *

with open("16.txt") as f:
    a = f.read()
    ci = len(findall(r"INFO", a))
    cw = len(findall(r"WARNING", a))
    ce = len(findall(r"ERROR", a))
    users = findall(r"ERROR User (\d+)", a)
    print(f"INFO: {ci}\nWARNING: {cw}\nERROR: {ce}")
    print(*sorted(set(users)))
