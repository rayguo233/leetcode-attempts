from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        m = defaultdict(list)
        for s in strs:
            ls = [0] * 26
            for c in s:
                ls[ord(c) - ord('a')] += 1
            m[tuple(ls)].append(s)
        return list(m.values())



if __name__ == '__main__':
    sol = Solution()
    for c in "dfghsdef":
        print(ord(c) - ord('a'))
