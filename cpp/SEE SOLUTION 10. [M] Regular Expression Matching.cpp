// httsp://leetcode.com/problems/strong-password-checker/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <math.h>

using namespace std;;

class Solution {
public:
    bool isMatch(string s, string p) {
        int s_size = s.size(), p_size = p.size();
        return MatchPartial(s, p, 0, 0, s_size, p_size);
    }
private:
    bool MatchPartial(string &s, string &p, int sp, int pp, int &s_size, int &p_size) {
        if (sp >= s_size || pp >= p_size) {
            while (pp + 1 < p_size && p.at(pp+1) == '*')
            pp += 2;
            return sp == s_size && pp == p_size;
        }
        for (; sp < s_size && pp < p_size; sp++, pp++) {
            char schar = s.at(sp), pchar = p.at(pp);
            cout << sp << ": " << schar << ' ' << pp << ": " << pchar << endl;
            assert(pchar != '*');

            if (pp+1 < p_size && p.at(pp+1) == '*') {
                if (pchar != '.' && pchar != schar) {
                    sp--, pp++;
                    continue;
                }
                if (MatchPartial(s, p, sp+1, pp, s_size, p_size))
                    return true;
                sp--;
                pp++;
                continue;
            }

            if (pchar == '.')
                continue;

            if (schar == pchar)
                continue;

            return false;
        }
        while (pp + 1 < p_size && p.at(pp+1) == '*')
            pp += 2;
        return sp == s_size && pp == p_size;
    }
};

int main() {
    Solution sol = Solution();
    string s = "bbbba";
    string p = ".*a*a";
    s = "aa";
    p = "a*";
    cout << sol.isMatch(s, p) << endl;
}