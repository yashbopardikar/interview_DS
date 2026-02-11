from typing import List
from zipfile import sizeFileHeader


class Solution:
    def sortSizes(self, size: List[str]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid= 0,0
        high = len(size)-1

        while mid < high:
            if size[mid] == "S":
                size[low], size[mid] = size[mid], size[low]
                low += 1
                mid += 1
            elif size[mid] == "M":
                mid +=1
            else:
                size[mid], size[high] = size[high], size[mid]
                high -= 1

        print(size)


sol = Solution()
size = ["S","M","S","L","L","M","S"]
sol.sortSizes(size)


