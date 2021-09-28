from abc import ABCMeta, abstractmethod
from utils.utils import read_csv_file


class FrtbBucket:
    __metaclass__ = ABCMeta
    __slots__ = ["data", "file_name"]

    def __init__(self, file_name):
        self.data = None
        self.file_name = file_name

    def read_file(self):
        return read_csv_file(self.file_name)

    @abstractmethod
    def get_bucket(self, value):
        pass

    @abstractmethod
    def __save_line_from_file(self, line):
        pass
