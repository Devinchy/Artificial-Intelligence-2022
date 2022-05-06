"""MAIN FILE """
# first we import the csv to work with the file
import csv

# then we make dictionaries (states) for each set and inside each probability to be calculated

low_low_high = {
    "Low;Low;High;E;Low;Low;Low": 0,
    "Low;Low;High;E;Low;Low;High": 0,
    "Low;Low;High;E;Low;High;Low": 0,
    "Low;Low;High;E;High;Low;Low": 0,
    "Low;Low;High;E;High;High;Low": 0,
    "Low;Low;High;E;Low;High;High": 0,
    "Low;Low;High;E;High;Low;High": 0,
    "Low;Low;High;E;High;High;High": 0,
    "Low;Low;High;N;Low;Low;Low": 0,
    "Low;Low;High;N;Low;Low;High": 0,
    "Low;Low;High;N;Low;High;Low": 0,
    "Low;Low;High;N;High;Low;Low": 0,
    "Low;Low;High;N;High;High;Low": 0,
    "Low;Low;High;N;Low;High;High": 0,
    "Low;Low;High;N;High;Low;High": 0,
    "Low;Low;High;N;High;High;High": 0,
    "Low;Low;High;W;Low;Low;Low": 0,
    "Low;Low;High;W;Low;Low;High": 0,
    "Low;Low;High;W;Low;High;Low": 0,
    "Low;Low;High;W;High;Low;Low": 0,
    "Low;Low;High;W;High;High;Low": 0,
    "Low;Low;High;W;Low;High;High": 0,
    "Low;Low;High;W;High;Low;High": 0,
    "Low;Low;High;W;High;High;High": 0,

}
low_high_low = {
    "Low;High;Low;E;Low;Low;Low": 0,
    "Low;High;Low;E;Low;Low;High": 0,
    "Low;High;Low;E;Low;High;Low": 0,
    "Low;High;Low;E;High;Low;Low": 0,
    "Low;High;Low;E;High;High;Low": 0,
    "Low;High;Low;E;Low;High;High": 0,
    "Low;High;Low;E;High;Low;High": 0,
    "Low;High;Low;E;High;High;High": 0,
    "Low;High;Low;N;Low;Low;Low": 0,
    "Low;High;Low;N;Low;Low;High": 0,
    "Low;High;Low;N;Low;High;Low": 0,
    "Low;High;Low;N;High;Low;Low": 0,
    "Low;High;Low;N;High;High;Low": 0,
    "Low;High;Low;N;Low;High;High": 0,
    "Low;High;Low;N;High;Low;High": 0,
    "Low;High;Low;N;High;High;High": 0,
    "Low;High;Low;W;Low;Low;Low": 0,
    "Low;High;Low;W;Low;Low;High": 0,
    "Low;High;Low;W;Low;High;Low": 0,
    "Low;High;Low;W;High;Low;Low": 0,
    "Low;High;Low;W;High;High;Low": 0,
    "Low;High;Low;W;Low;High;High": 0,
    "Low;High;Low;W;High;Low;High": 0,
    "Low;High;Low;W;High;High;High": 0,
}
high_low_low = {
    "High;Low;Low;E;Low;Low;Low": 0,
    "High;Low;Low;E;Low;Low;High": 0,
    "High;Low;Low;E;Low;High;Low": 0,
    "High;Low;Low;E;High;Low;Low": 0,
    "High;Low;Low;E;High;High;Low": 0,
    "High;Low;Low;E;Low;High;High": 0,
    "High;Low;Low;E;High;Low;High": 0,
    "High;Low;Low;E;High;High;High": 0,
    "High;Low;Low;N;Low;Low;Low": 0,
    "High;Low;Low;N;Low;Low;High": 0,
    "High;Low;Low;N;Low;High;Low": 0,
    "High;Low;Low;N;High;Low;Low": 0,
    "High;Low;Low;N;High;High;Low": 0,
    "High;Low;Low;N;Low;High;High": 0,
    "High;Low;Low;N;High;Low;High": 0,
    "High;Low;Low;N;High;High;High": 0,
    "High;Low;Low;W;Low;Low;Low": 0,
    "High;Low;Low;W;Low;Low;High": 0,
    "High;Low;Low;W;Low;High;Low": 0,
    "High;Low;Low;W;High;Low;Low": 0,
    "High;Low;Low;W;High;High;Low": 0,
    "High;Low;Low;W;Low;High;High": 0,
    "High;Low;Low;W;High;Low;High": 0,
    "High;Low;Low;W;High;High;High": 0,
}
low_high_high = {
    "Low;High;High;E;Low;Low;Low": 0,
    "Low;High;High;E;Low;Low;High": 0,
    "Low;High;High;E;Low;High;Low": 0,
    "Low;High;High;E;High;Low;Low": 0,
    "Low;High;High;E;High;High;Low": 0,
    "Low;High;High;E;Low;High;High": 0,
    "Low;High;High;E;High;Low;High": 0,
    "Low;High;High;E;High;High;High": 0,
    "Low;High;High;N;Low;Low;Low": 0,
    "Low;High;High;N;Low;Low;High": 0,
    "Low;High;High;N;Low;High;Low": 0,
    "Low;High;High;N;High;Low;Low": 0,
    "Low;High;High;N;High;High;Low": 0,
    "Low;High;High;N;Low;High;High": 0,
    "Low;High;High;N;High;Low;High": 0,
    "Low;High;High;N;High;High;High": 0,
    "Low;High;High;W;Low;Low;Low": 0,
    "Low;High;High;W;Low;Low;High": 0,
    "Low;High;High;W;Low;High;Low": 0,
    "Low;High;High;W;High;Low;Low": 0,
    "Low;High;High;W;High;High;Low": 0,
    "Low;High;High;W;Low;High;High": 0,
    "Low;High;High;W;High;Low;High": 0,
    "Low;High;High;W;High;High;High": 0,
}
high_high_low = {
    "High;High;Low;E;Low;Low;Low": 0,
    "High;High;Low;E;Low;Low;High": 0,
    "High;High;Low;E;Low;High;Low": 0,
    "High;High;Low;E;High;Low;Low": 0,
    "High;High;Low;E;High;High;Low": 0,
    "High;High;Low;E;Low;High;High": 0,
    "High;High;Low;E;High;Low;High": 0,
    "High;High;Low;E;High;High;High": 0,
    "High;High;Low;N;Low;Low;Low": 0,
    "High;High;Low;N;Low;Low;High": 0,
    "High;High;Low;N;Low;High;Low": 0,
    "High;High;Low;N;High;Low;Low": 0,
    "High;High;Low;N;High;High;Low": 0,
    "High;High;Low;N;Low;High;High": 0,
    "High;High;Low;N;High;Low;High": 0,
    "High;High;Low;N;High;High;High": 0,
    "High;High;Low;W;Low;Low;Low": 0,
    "High;High;Low;W;Low;Low;High": 0,
    "High;High;Low;W;Low;High;Low": 0,
    "High;High;Low;W;High;Low;Low": 0,
    "High;High;Low;W;High;High;Low": 0,
    "High;High;Low;W;Low;High;High": 0,
    "High;High;Low;W;High;Low;High": 0,
    "High;High;Low;W;High;High;High": 0,
}
high_low_high = {
    "High;Low;High;E;Low;Low;Low": 0,
    "High;Low;High;E;Low;Low;High": 0,
    "High;Low;High;E;Low;High;Low": 0,
    "High;Low;High;E;High;Low;Low": 0,
    "High;Low;High;E;High;High;Low": 0,
    "High;Low;High;E;Low;High;High": 0,
    "High;Low;High;E;High;Low;High": 0,
    "High;Low;High;E;High;High;High": 0,
    "High;Low;High;N;Low;Low;Low": 0,
    "High;Low;High;N;Low;Low;High": 0,
    "High;Low;High;N;Low;High;Low": 0,
    "High;Low;High;N;High;Low;Low": 0,
    "High;Low;High;N;High;High;Low": 0,
    "High;Low;High;N;Low;High;High": 0,
    "High;Low;High;N;High;Low;High": 0,
    "LHigh;Low;High;N;High;High;High": 0,
    "High;Low;High;W;Low;Low;Low": 0,
    "High;Low;High;W;Low;Low;High": 0,
    "High;Low;High;W;Low;High;Low": 0,
    "High;Low;High;W;High;Low;Low": 0,
    "High;Low;High;W;High;High;Low": 0,
    "High;Low;High;W;Low;High;High": 0,
    "High;Low;High;W;High;Low;High": 0,
    "High;Low;High;W;High;High;High": 0,
}

# counters to develop the probabilities
count_rows = 0  # counter to accumulate the total value of the number of rows
count = 0
count_low_low_high_1st = 0
count_low_low_high_2nd = 0
count_low_low_high_3th = 0
count_low_low_high_4th = 0
count_low_low_high_5th = 0
count_low_low_high_6th = 0
with open("Data_files/Data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        count_rows += 1

        if row == ['Low;Low;Low;W;Low;Low;Low']:
            count += 1
        if row == ['Low;Low;Low;W;Low;Low;High']:
            count += 1
        if row == ['Low;Low;Low;W;Low;High;Low']:
            count += 1
        if row == ['Low;Low;Low;W;High;Low;Low']:
            count += 1
        if row == ['Low;Low;Low;W;High;High;Low']:
            count += 1
        if row == ['Low;Low;Low;W;Low;High;High']:
            count += 1
        if row == ['Low;Low;Low;W;High;Low;High']:
            count += 1
        if row == ['Low;Low;Low;W;High;High;High']:
            count += 1

    print(count)
    print(count_rows)
"""P(s'= H,H,L| s = H,H,L , a = E)"""
probability = count / count_rows
print(probability)
