"""MAIN FILE """

import csv

count = 0
count_rows = 0
with open("Data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        count_rows += 1
        if row == ['High;High;Low;E;High;High;Low']:
            count += 1
    print(count)
    print(count_rows)
"""P(s'= H,H,L| s = H,H,L , a = E)"""
probability = count/count_rows
print(probability)
