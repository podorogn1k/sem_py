f = open("1.txt")
st = ""
cst = 0
cw = 0
csm = 0
lm = 0
for line in f:
    st = line
    cst += 1
    cw += len(list(map(str, st.replace("  ", " ").strip().split())))
    csm += len(st)
    lm = max(len(st), lm)
print(cst, cw, csm, lm)