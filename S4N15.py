from io import StringIO

def count_lines(stream):
    c = 0
    for i in stream:
        c += 1
    return c

print(count_lines(StringIO("first\nsecond\nthird")))