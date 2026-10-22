with open("17.txt") as f:
    s = 0
    mn = float('inf')
    mx = float('-inf')
    c = 0
    for i in f:
        n = int(i)
        mx = max(mx, n)
        mn = min(mn, n)
        s += n
        c += 1
    print(s, mn, mx, c, int(s / c), sep="\n")