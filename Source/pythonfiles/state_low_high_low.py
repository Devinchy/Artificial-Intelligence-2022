# first we import the csv to work with the file
import csv

# then we make dictionaries (states) for each set and inside each probability to be calculated
def probability_low_high_low():
    low_high_low = {
        "[Low;High,Low;E;Low;Low;Low']": 0,
        "[Low;High,Low;E;Low;Low;High']": 0,
        "[Low;High,Low;E;Low;High;Low']": 0,
        "[Low;High,Low;E;High;Low;Low']": 0,

        "[Low;High,Low;E;High;High;Low']": 0,
        "[Low;High,Low;E;Low;High;High']": 0,
        "[Low;High,Low;E;High;Low;High']": 0,
        "[Low;High,Low;E;High;High;High']": 0,

        "[Low;High,Low;N;Low;Low;Low']": 0,
        "[Low;High,Low;N;Low;Low;High']": 0,
        "[Low;High,Low;N;Low;High;Low']": 0,
        "[Low;High,Low;N;High;Low;Low']": 0,

        "[Low;High,Low;N;High;High;Low']": 0,
        "[Low;High,Low;N;Low;High;High']": 0,
        "[Low;High,Low;N;High;Low;High']": 0,
        "[Low;High,Low;N;High;High;High']": 0,

        "[Low;High,Low;W;Low;Low;Low']": 0,
        "[Low;High,Low;W;Low;Low;High']": 0,
        "[Low;High,Low;W;Low;High;Low']": 0,
        "[Low;High,Low;W;High;Low;Low']": 0,

        "[Low;High,Low;W;High;High;Low']": 0,
        "[Low;High,Low;W;Low;High;High']": 0,
        "[Low;High,Low;W;High;Low;High']": 0,
        "[Low;High,Low;W;High;High;High']": 0,
    }
    count_rows = 0  # counter to accumulate the total value of the number of rows
    with open("Data.csv") as f:
        reader = csv.reader(f)
        # counter high_high_high state
        counter_low_high_low_1st = 0
        counter_low_high_low_2nd = 0
        counter_low_high_low_3rd = 0
        counter_low_high_low_4th = 0
        counter_low_high_low_5th = 0
        counter_low_high_low_6th = 0
        counter_low_high_low_7th = 0
        counter_low_high_low_8th = 0
        counter_low_high_low_9th = 0
        counter_low_high_low_10th = 0
        counter_low_high_low_11th = 0
        counter_low_high_low_12th = 0
        counter_low_high_low_13th = 0
        counter_low_high_low_14th = 0
        counter_low_high_low_15th = 0
        counter_low_high_low_16th = 0
        counter_low_high_low_17th = 0
        counter_low_high_low_18th = 0
        counter_low_high_low_19th = 0
        counter_low_high_low_20th = 0
        counter_low_high_low_21st = 0
        counter_low_high_low_22nd = 0
        counter_low_high_low_23rd = 0
        counter_low_high_low_24th = 0
        for row in reader:
            count_rows += 1
            if row == ['High;High;Low;E;Low;Low;Low']:
                counter_low_high_low_1st += 1
            if row == ['High;High;Low;E;Low;Low;High']:
                counter_low_high_low_2nd += 1
            if row == ['High;High;Low;E;Low;High;Low']:
                counter_low_high_low_3rd += 1
            if row == ['High;High;Low;E;High;Low;Low']:
                counter_low_high_low_4th += 1

            if row == ['High;High;Low;E;High;High;Low']:
                counter_low_high_low_5th += 1
            if row == ['High;High;Low;E;Low;High;High']:
                counter_low_high_low_6th += 1
            if row == ['High;High;Low;E;High;Low;High']:
                counter_low_high_low_7th += 1
            if row == ['High;High;Low;E;High;High;High']:
                counter_low_high_low_8th += 1

            if row == ['High;High;Low;N;Low;Low;Low']:
                counter_low_high_low_9th += 1
            if row == ['High;High;Low;N;Low;Low;High']:
                counter_low_high_low_10th += 1
            if row == ['High;High;Low;N;Low;High;Low']:
                counter_low_high_low_11th += 1
            if row == ['High;High;Low;N;High;Low;Low']:
                counter_low_high_low_12th += 1

            if row == ['High;High;Low;N;High;High;Low']:
                counter_low_high_low_13th += 1
            if row == ['High;High;Low;N;Low;High;High']:
                counter_low_high_low_14th += 1
            if row == ['High;High;Low;N;High;Low;High']:
                counter_low_high_low_15th += 1
            if row == ['High;High;Low;N;High;High;High']:
                counter_low_high_low_16th += 1

            if row == ['High;High;Low;W;Low;Low;Low']:
                counter_low_high_low_17th += 1
            if row == ['High;High;Low;W;Low;Low;High']:
                counter_low_high_low_18th += 1
            if row == ['High;High;Low;W;Low;High;Low']:
                counter_low_high_low_19th += 1
            if row == ['High;High;Low;W;High;Low;Low']:
                counter_low_high_low_20th += 1

            if row == ['High;High;Low;W;High;High;Low']:
                counter_low_high_low_21st += 1
            if row == ['High;High;Low;W;Low;High;High']:
                counter_low_high_low_22nd += 1
            if row == ['High;High;Low;W;High;Low;High']:
                counter_low_high_low_23rd += 1
            if row == ['High;High;Low;W;High;High;High']:
                counter_low_high_low_24th += 1

        low_high_low["[Low;High,Low;E;Low;Low;Low']"] = round(counter_low_high_low_1st/count_rows, 6)
        low_high_low["[Low;High,Low;E;Low;Low;High']"] = round(counter_low_high_low_2nd / count_rows, 6)
        low_high_low["[Low;High,Low;E;Low;High;Low']"] = round(counter_low_high_low_3rd / count_rows, 6)
        low_high_low["[Low;High,Low;E;High;Low;Low']"] = round(counter_low_high_low_4th / count_rows, 6)

        low_high_low["[Low;High,Low;E;High;High;Low']"] = round(counter_low_high_low_5th / count_rows, 6)
        low_high_low["[Low;High,Low;E;Low;High;High']"] = round(counter_low_high_low_6th / count_rows, 6)
        low_high_low["[Low;High,Low;E;High;Low;High']"] = round(counter_low_high_low_7th / count_rows, 6)
        low_high_low["[Low;High,Low;E;High;High;High']"] = round(counter_low_high_low_8th / count_rows, 6)

        low_high_low["[Low;High,Low;N;Low;Low;Low']"] = round(counter_low_high_low_9th/count_rows, 6)
        low_high_low["[Low;High,Low;N;Low;Low;High']"] = round(counter_low_high_low_10th / count_rows, 6)
        low_high_low["[Low;High,Low;N;Low;High;Low']"] = round(counter_low_high_low_11th/ count_rows, 6)
        low_high_low["[Low;High,Low;N;High;Low;Low']"] = round(counter_low_high_low_12th/ count_rows, 6)

        low_high_low["[Low;High,Low;N;High;High;Low']"] = round(counter_low_high_low_13th/count_rows, 6)
        low_high_low["[Low;High,Low;N;Low;High;High']"] = round(counter_low_high_low_14th/ count_rows, 6)
        low_high_low["[Low;High,Low;N;High;Low;High']"] = round(counter_low_high_low_15th/ count_rows, 6)
        low_high_low["[Low;High,Low;N;High;High;High']"] = round(counter_low_high_low_16th/ count_rows, 6)

        low_high_low["[Low;High,Low;W;Low;Low;Low']"] = round(counter_low_high_low_17th/count_rows, 6)
        low_high_low["[Low;High,Low;W;Low;Low;High']"] = round(counter_low_high_low_18th/ count_rows, 6)
        low_high_low["[Low;High,Low;W;Low;High;Low']"] = round(counter_low_high_low_19th/ count_rows, 6)
        low_high_low["[Low;High,Low;W;High;Low;Low']"] = round(counter_low_high_low_20th/ count_rows, 6)

        low_high_low["[Low;High,Low;W;High;High;Low']"] = round(counter_low_high_low_21st/count_rows, 6)
        low_high_low["[Low;High,Low;W;Low;High;High']"] = round(counter_low_high_low_22nd/ count_rows, 6)
        low_high_low["[Low;High,Low;W;High;Low;High']"] = round(counter_low_high_low_23rd/ count_rows, 6)
        low_high_low["[Low;High,Low;W;High;High;High']"] = round(counter_low_high_low_24th / count_rows, 6)

    return low_high_low

