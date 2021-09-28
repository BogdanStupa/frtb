from frtb.frtb_bucket import FrtbBucket
import csv

class ValueFrtbBucket(FrtbBucket):


    def __init__(self, file_name):
        # super().__init__(file_name)
        self.data = {}
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            line_count = 0

            for line in csv_reader:
                if line_count > 0:
                    self.__save_line_from_file(line)
                line_count += 1

    def get_bucket(self, value):
        try:
            return self.data[value]
        except KeyError:
            return f"{value} Not Found"

    def __save_line_from_file(self, line):
        self.data[line[1]] = line[0]
