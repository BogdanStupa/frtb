from range_search_array import RangeSearchArray
from frtb._frtb_bucket import FrtbBucket
from typing import Tuple, List


class RangeFrtbBucket(FrtbBucket):

    def __init__(self, file_name: str):
        super().__init__(file_name)
        data_ = []
        for line in self.read_file():
            data_.append(self.__get_data_from_line(line))
        self.data = RangeSearchArray(data_)

    def get_bucket(self, value: int) -> int:
        return self.data.get_bucket(value=value)

    def __get_data_from_line(self, line: List[str]) -> Tuple[int, int, int]:
        if len(line) != 3:
            raise ValueError("Invalid data in line")

        for digit in line:
            if not digit.isdigit():
                raise ValueError("Invalid data in line")

        return int(line[1]), int(line[2]), int(line[0])
