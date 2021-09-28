import csv

def read_csv_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0
        for line in csv_reader:
            if line_count > 0:
                yield line
            line_count += 1
