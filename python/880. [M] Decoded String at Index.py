import bisect


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        starts = []
        start_to_str = {}
        curr_start = 0
        prev_i = 0
        for i, c in enumerate(s):
            if c.isalpha():
                continue
            starts.append(curr_start)
            start_to_str[curr_start] = s[prev_i:i]
            curr_start += len(start_to_str[curr_start])
            curr_start *= int(c)
            prev_i = i + 1
        
        def find_jth(j: int) -> str:
            i = bisect.bisect_right(starts, j) - 1
            start = starts[i]
            length = start + len(start_to_str[start])
            if j < length:
                return start_to_str[starts[i]][j-start]
            return find_jth(j % length)

        if not starts:
            return s[k-1]
        print(starts, start_to_str)
        return find_jth(k - 1)



if __name__ == '__main__':
    s = Solution()
    print(s.decodeAtIndex('sf1fd2df3', 29))
