from csv import *

f = open("students.csv")
res = []
res101 = []
res102 = []
reader = reader(f)
headers = next(reader)
for line in reader:
    res.append(line)
    if (line[1] == "101"):
        res101.append(line)
    else:
        res102.append(line)
num = [int(res[i][2]) for i in range(len(res))]
num101 = [int(res101[i][2]) for i in range(len(res101))]
num102 = [int(res102[i][2]) for i in range(len(res102))]
print(sum(num)/len(num), sorted(res, key = lambda x: -int(x[2]))[0][0], sum(num101)/len(num101), sum(num102)/len(num102))