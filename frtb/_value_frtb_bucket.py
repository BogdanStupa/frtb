from frtb._frtb_bucket import FrtbBucket

class ValueFrtbBucket(FrtbBucket):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.data = {}
        for line in self.read_file():
            self.__save_line_from_file(line)

    def get_bucket(self, value):
        try:
            return self.data[value]
        except KeyError:
            return f"{value} Not Found"

    def __save_line_from_file(self, line):
        self.data[line[1]] = line[0]
