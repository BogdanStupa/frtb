import csv

def read_from_csv(file_name, callback):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0

        for line in csv_reader:
            if line_count > 0:
                callback(line)
            line_count += 1
