from csv import *

with open("4.csv") as f0, open("expensive.csv", "w", newline = "") as f1:
    reader = reader(f0)
    writer = writer(f1)
    header = next(reader)
    writer.writerow(header)
    for i in reader:
        if (int(i[2]) > 100):
            writer.writerow(i)