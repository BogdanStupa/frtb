from frtb.frtb_bucket import FrtbBucket
from serch_tree.search_tree import SearchTree
import csv

class RangeFrtbBucket(FrtbBucket):

    def __init__(self, file_name):
        self.data = SearchTree()
        # super().__init__(file_name)
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            line_count = 0
            for line in csv_reader:
                if line_count > 0:
                    self.__save_line_from_file(line)
                line_count += 1


    def get_bucket(self, value):
        return self.data.get_bucket(value=value)


    def __save_line_from_file(self, line):
        self.data.insert(bucket_range=[int(line[1]), int(line[2])], bucket_id=line[0])
