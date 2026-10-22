from json import *

with open("students.json") as f0, open("newsudents.json", "w") as f1:
    st = load(f0)
    mx = 0
    nmx = ""
    for i in st:
        i["passes"] = i["score"] >= 60
        if (mx < i["score"]):
            mx = i["score"]
            nmx = i["name"]
    dump(st, f1, indent=4)
print(nmx)