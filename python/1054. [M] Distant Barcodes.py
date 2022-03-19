import collections
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = collections.Counter(barcodes)
        vals = sorted([[freq, val] for val, freq in c.items()], reverse=True)
        sub_arrays = [[vals[0][1]] for _ in range(vals[0][0])]
        vals = vals[1:]
        i = 0
        for freq, val in vals:
            for _ in range(freq):
                sub_arrays[i].append(val)
                i = (i + 1) % len(sub_arrays)
            
        print(sub_arrays)
        return [item for sublist in sub_arrays for item in sublist]




if __name__ == '__main__':
    s = Solution()
    print(s.rearrangeBarcodes([1,1,1,2,1,2,2,3,4,5,6,7,3,4,5,4,4,3,4,4,4,4,4]))
