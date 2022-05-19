"""
    This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
    Your task is to compute the number of inversions in the file given, where the i(th) row of the file indicates the i(th) entry of an array.
    Because of the large size of this array, you should implement the fast divide-and-conquer algorithm.

"""

import time
from file_reader import *

class Inversions:

    def __init__(self, _array):
        self._array = _array 


    def get_data():

        return list(map(lambda s: int(s), read_input(FilePath.FILE)))


    def merge_and_count(left_array,right_array):
        
        res_arr, inv_count = [], 0
        while len(left_array) > 0 or len(right_array) > 0:
            if len(left_array) > 0 and len(right_array) > 0:
                if left_array[0] < right_array[0]:
                    res_arr.append(left_array[0])
                    left_array = left_array[1:]
                else:
                    res_arr.append(right_array[0])
                    right_array = right_array[1:]
                    inv_count += len(left_array)
            elif len(left_array) > 0:
                res_arr.append(left_array[0])
                left_array = left_array[1:]
            elif len(right_array) > 0:
                res_arr.append(right_array[0])
                right_array = right_array[1:]

        return res_arr, inv_count


    def sort_and_count(_array):
        
        arr_len = len(_array)
        if arr_len <= 1:
            return _array, 0
        left_array,count_left = Inversions.sort_and_count(_array[:(arr_len//2)])
        right_array,count_right = Inversions.sort_and_count(_array[(arr_len//2):])
        merged_array,count_merge = Inversions.merge_and_count(left_array,right_array)

        return merged_array, count_left + count_right + count_merge



if __name__ == '__main__':

    start = time.time()
    f = Inversions.get_data()
    print(Inversions.sort_and_count([int(l) for l in f])[1])
    print('Total time: %f' % (time.time() - start))


# 2407905288
