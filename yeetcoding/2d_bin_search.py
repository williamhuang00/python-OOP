from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        naive solution O(m*n) linear search

        how to do better?
        1. take advantage of sorted quality in the input
            - go row by row and ask: is target between first and element?
            - then do binary search on that row
            - tc: O(rows * log(cols))
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top, bot = 0, len(matrix)-1

        while top <= bot:
            row_idx = (top + bot) // 2
            cur_row = matrix[row_idx]
            if target > cur_row[-1]:
                top = row_idx + 1
            elif target < cur_row[0]:
                bot = row_idx - 1
            else:
                break
        l = 0
        r = COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target < cur_row[m]:
                r = m - 1
            elif target > cur_row[m]:
                l = m + 1
            else:
                print('found it')
                return True
        return False
        

