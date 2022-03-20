class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        def get_substr_fixed(ss: str, tt: str) -> int:
            length = min(len(ss), len(tt))
            ss = ss[:length]
            tt = tt[:length]
            diff = [i for i, (sc, tc) in enumerate(zip(ss, tt)) if sc != tc]
            print(diff)
            if not diff:
                return 0
            diff.append(length)
            left = 0
            mid = diff[0]
            right = diff[1]
            res = 0
            for right in diff[1:]:
                right -= 1
                res += (mid - left + 1) * (right - mid + 1)
                left = mid + 1
                mid = right + 1
            return res

        res = 0
        for i in range(len(s)):
            res += get_substr_fixed(s[i:], t)
        for i in range(1, len(t)):
            res += get_substr_fixed(s, t[i:])
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings('aba', 'baba'))
    print(sol.countSubstrings('ab', 'bb'))