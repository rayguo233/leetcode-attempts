// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

#include <vector>  
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string removeDuplicates(string s) {
        int fp = 0, sp = 1;
        int size = s.size();
        if (size <= 1)
            return s;
        
        while (sp < size) {
            if (fp == -1) {
                fp = 0;
                s.at(fp) = s.at(sp);
                sp++;
                continue;
            }
            if (s.at(fp) == s.at(sp)) {
                fp--, sp++;
                continue;
            }
            s.at(fp+1) = s.at(sp);
            fp++, sp++;
        }
        s.resize(fp+1);
        return s;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.removeDuplicates("aabbc") << endl;
}