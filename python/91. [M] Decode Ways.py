class Solution:
    def num_decodings(self, s: str) -> int:
        self.d = [-1] * len(s)
        return int(self.num_decodings_from_n(s, 0))

    def num_decodings_from_n(self, s: str, n: int) -> int:
        if len(s) == n:
            return 1
        if len(s) == n - 1:
            return 0
        if self.d[n] != -1:
            return self.d[n]
        if s[n] == '0':
            self.d[n] = 0
            return 0

        one_digit = self.num_decodings_from_n(s, n + 1)
        two_digits = 0 if int(s[n:n+2]) > 26 else self.num_decodings_from_n(s, n + 2)
        self.d[n] = one_digit + two_digits
        return self.d[n]
