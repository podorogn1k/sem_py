def parse_number(value):
    if ('.' in value):
        return float(value)
    if (',' in value):
        return float(value.replace(',', '.'))
    return int(value)

n = input()
try:
    n = parse_number(n)
    print(n)
except ValueError:
    print("ValueError; введено не число")