
class Solution:
    def minimumDeletions(self, s: str) -> int:
        num_delete = sum(c == 'a' for c in s)
        res = num_delete
        for last_a_i, c in enumerate(s):
            if c == 'a':
                num_delete -= 1
            else:
                num_delete += 1
            res = min(res, num_delete)
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumDeletions('ba'), 1)
    print(sol.minimumDeletions('babb'), 1)
    print(sol.minimumDeletions('bbbbabb'), 1)
    print(sol.minimumDeletions('aaaaaabbaabb'), 2)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
