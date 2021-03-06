# first we import the csv to work with the file
import csv


def probability_high_high_high():
    
    high_high_high = {
        "['High;High;High;E;Low;Low;Low']": 0,
        "['High;High;High;E;Low;Low;High']": 0,
        "['High;High;High;E;Low;High;Low']": 0,
        "['High;High;High;E;High;Low;Low']": 0,
    
        "['High;High;High;E;High;High;Low']": 0,
        "['High;High;High;E;Low;High;High']": 0,
        "['High;High;High;E;High;Low;High']": 0,
        "['High;High;High;E;High;High;High']": 0,
    
        "['High;High;High;N;Low;Low;Low']": 0,
        "['High;High;High;N;Low;Low;High']": 0,
        "['High;High;High;N;Low;High;Low']": 0,
        "['High;High;High;N;High;Low;Low']": 0,
    
        "['High;High;High;N;High;High;Low']": 0,
        "['High;High;High;N;Low;High;High']": 0,
        "['High;High;High;N;High;Low;High']": 0,
        "['High;High;High;N;High;High;High']": 0,
    
        "['High;High;High;W;Low;Low;Low']": 0,
        "['High;High;High;W;Low;Low;High']": 0,
        "['High;High;High;W;Low;High;Low']": 0,
        "['High;High;High;W;High;Low;Low']": 0,
    
        "['High;High;High;W;High;High;Low']": 0,
        "['High;High;High;W;Low;High;High']": 0,
        "['High;High;High;W;High;Low;High']": 0,
        "['High;High;High;W;High;High;High']": 0,
    }
    count_rows = 0  # counter to accumulate the total value of the number of rows
    with open("Data.csv") as f:
        reader = csv.reader(f)
        # counter high_high_high state
        counter_high_high_high_1st = 0
        counter_high_high_high_2nd = 0
        counter_high_high_high_3rd = 0
        counter_high_high_high_4th = 0
        counter_high_high_high_5th = 0
        counter_high_high_high_6th = 0
        counter_high_high_high_7th = 0
        counter_high_high_high_8th = 0
        counter_high_high_high_9th = 0
        counter_high_high_high_10th = 0
        counter_high_high_high_11th = 0
        counter_high_high_high_12th = 0
        counter_high_high_high_13th = 0
        counter_high_high_high_14th = 0
        counter_high_high_high_15th = 0
        counter_high_high_high_16th = 0
        counter_high_high_high_17th = 0
        counter_high_high_high_18th = 0
        counter_high_high_high_19th = 0
        counter_high_high_high_20th = 0
        counter_high_high_high_21st = 0
        counter_high_high_high_22nd = 0
        counter_high_high_high_23rd = 0
        counter_high_high_high_24th = 0
        for row in reader:
            count_rows += 1
            if row == ['High;High;High;E;Low;Low;Low']:
                counter_high_high_high_1st += 1
            if row == ['High;High;High;E;Low;Low;High']:
                counter_high_high_high_2nd += 1
            if row == ['High;High;High;E;Low;High;Low']:
                counter_high_high_high_3rd += 1
            if row == ['High;High;High;E;High;Low;Low']:
                counter_high_high_high_4th += 1
    
            if row == ['High;High;High;E;High;High;Low']:
                counter_high_high_high_5th += 1
            if row == ['High;High;High;E;Low;High;High']:
                counter_high_high_high_6th += 1
            if row == ['High;High;High;E;High;Low;High']:
                counter_high_high_high_7th += 1
            if row == ['High;High;High;E;High;High;High']:
                counter_high_high_high_8th += 1
    
            if row == ['High;High;High;N;Low;Low;Low']:
                counter_high_high_high_9th += 1
            if row == ['High;High;High;N;Low;Low;High']:
                counter_high_high_high_10th += 1
            if row == ['High;High;High;N;Low;High;Low']:
                counter_high_high_high_11th += 1
            if row == ['High;High;High;N;High;Low;Low']:
                counter_high_high_high_12th += 1
    
            if row == ['High;High;High;N;High;High;Low']:
                counter_high_high_high_13th += 1
            if row == ['High;High;High;N;Low;High;High']:
                counter_high_high_high_14th += 1
            if row == ['High;High;High;N;High;Low;High']:
                counter_high_high_high_15th += 1
            if row == ['High;High;High;N;High;High;High']:
                counter_high_high_high_16th += 1
    
            if row == ['High;High;High;W;Low;Low;Low']:
                counter_high_high_high_17th += 1
            if row == ['High;High;High;W;Low;Low;High']:
                counter_high_high_high_18th += 1
            if row == ['High;High;High;W;Low;High;Low']:
                counter_high_high_high_19th += 1
            if row == ['High;High;High;W;High;Low;Low']:
                counter_high_high_high_20th += 1
    
            if row == ['High;High;High;W;High;High;Low']:
                counter_high_high_high_21st += 1
            if row == ['High;High;High;W;Low;High;High']:
                counter_high_high_high_22nd += 1
            if row == ['High;High;High;W;High;Low;High']:
                counter_high_high_high_23rd += 1
            if row == ['High;High;High;W;High;High;High']:
                counter_high_high_high_24th += 1
    
        high_high_high["['High;High;High;E;Low;Low;Low']"] = round(counter_high_high_high_1st/count_rows, 6)
        high_high_high["['High;High;High;E;Low;Low;High']"] = round(counter_high_high_high_2nd / count_rows, 6)
        high_high_high["['High;High;High;E;Low;High;Low']"] = round(counter_high_high_high_3rd / count_rows, 6)
        high_high_high["['High;High;High;E;High;Low;Low']"] = round(counter_high_high_high_4th / count_rows, 6)
    
        high_high_high["['High;High;High;E;High;High;Low']"] = round(counter_high_high_high_5th / count_rows, 6)
        high_high_high["['High;High;High;E;Low;High;High']"] = round(counter_high_high_high_6th / count_rows, 6)
        high_high_high["['High;High;High;E;High;Low;High']"] = round(counter_high_high_high_7th / count_rows, 6)
        high_high_high["['High;High;High;E;High;High;High']"] = round(counter_high_high_high_8th / count_rows, 6)
    
        high_high_high["['High;High;High;N;Low;Low;Low']"] = round(counter_high_high_high_9th/count_rows, 6)
        high_high_high["['High;High;High;N;Low;Low;High']"] = round(counter_high_high_high_10th / count_rows, 6)
        high_high_high["['High;High;High;N;Low;High;Low']"] = round(counter_high_high_high_11th/ count_rows, 6)
        high_high_high["['High;High;High;N;High;Low;Low']"] = round(counter_high_high_high_12th/ count_rows, 6)
    
        high_high_high["['High;High;High;N;High;High;Low']"] = round(counter_high_high_high_13th/count_rows, 6)
        high_high_high["['High;High;High;N;Low;High;High']"] = round(counter_high_high_high_14th/ count_rows, 6)
        high_high_high["['High;High;High;N;High;Low;High']"] = round(counter_high_high_high_15th/ count_rows, 6)
        high_high_high["['High;High;High;N;High;High;High']"] = round(counter_high_high_high_16th/ count_rows, 6)
    
        high_high_high["['High;High;High;W;Low;Low;Low']"] = round(counter_high_high_high_17th/count_rows, 6)
        high_high_high["['High;High;High;W;Low;Low;High']"] = round(counter_high_high_high_18th/ count_rows, 6)
        high_high_high["['High;High;High;W;Low;High;Low']"] = round(counter_high_high_high_19th/ count_rows, 6)
        high_high_high["['High;High;High;W;High;Low;Low']"] = round(counter_high_high_high_20th/ count_rows, 6)
    
        high_high_high["['High;High;High;W;High;High;Low']"] = round(counter_high_high_high_21st/count_rows, 6)
        high_high_high["['High;High;High;W;Low;High;High']"] = round(counter_high_high_high_22nd/ count_rows, 6)
        high_high_high["['High;High;High;W;High;Low;High']"] = round(counter_high_high_high_23rd/ count_rows, 6)
        high_high_high["['High;High;High;W;High;High;High']"] = round(counter_high_high_high_24th / count_rows, 6)
    
        return high_high_high
