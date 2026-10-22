from re import *

def del_space(st):
    st = sub(r" +", " ", st)
    st = sub(r"^ | $", "", st)
    return st

print(del_space("Это   строка    с     большим    количеством   пробелов."))
print(del_space("   Текст   с   пробелами   "))