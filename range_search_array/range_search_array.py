import numpy as np
from typing import List, Tuple


class RangeSearchArray:
    __slots__ = ["__data", "__n"]

    def __init__(self, data_: List[Tuple[int, int, int]]):
        self.__data = np.sort(np.array(data_, dtype=[('left_range', int), ('right_range', int), ('bucket_id', int)]))
        self.__n = self.__data.shape[0]

    def find(self, value: int) -> int:
        left = 0
        right = self.__n - 1
        while left <= right:
            mid = (left + right) // 2
            if self.__data[mid][0] > value:
                right = mid - 1
            elif self.__data[mid][1] < value:
                left = mid + 1
            else:
                if value == self.__data[mid][1] and mid + 1 != self.__n:
                    return self.__data[mid + 1][2]
                return self.__data[mid][2]
        return -1
