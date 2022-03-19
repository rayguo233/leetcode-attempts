from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted([a % k for a in arr if a % k])
        # print(arr)
        if len(arr) % 2:
            return False
        for i in range(len(arr) // 2):
            if (arr[i] + arr[-i-1]) != k:
                return False
        return True



if __name__ == '__main__':
    s = Solution()
    print(s.canArrange([1,1],2))
    print(s.canArrange([4,4,2,2],2))
    print(s.canArrange([1,3,5,5],2))
    print(s.canArrange([5,1],3))
    print(s.canArrange([1,5,2,4],2))
    print(s.canArrange([1,2,3,4,5,10,6,7,8,9],5))