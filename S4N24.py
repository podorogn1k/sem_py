from re import *

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

for i in products:
    if (fullmatch(r"PRD-\d{5}", i)):
        print(i)