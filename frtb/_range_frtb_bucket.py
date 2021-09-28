from frtb._frtb_bucket import FrtbBucket
from search_tree import SearchTree


class RangeFrtbBucket(FrtbBucket):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.data = SearchTree()
        for line in self.read_file():
            self.__save_line_from_file(line)

    def get_bucket(self, value):
        return self.data.get_bucket(value=value)

    def __save_line_from_file(self, line):
        self.data.insert(bucket_range=[int(line[1]), int(line[2])], bucket_id=line[0])
