// https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <stack>

using namespace std;;

class Solution {
public:
    bool validateStackSequences(const vector<int>& pushed, const vector<int>& popped) {
        stack<int> s;
        int pushed_size = pushed.size();
        int pushed_i = 0;
        for (int n : popped) {
            while (s.empty() || s.top() != n) {
                if (pushed_i == pushed_size)
                    return false;
                s.push(pushed.at(pushed_i));
                pushed_i++;
            }
            s.pop();
        }
        return true;
    }

    bool validateStackSequences_too_slow(const vector<int>& pushed, const vector<int>& popped) {
        int next_push = 0;
        int max_pop = INT_MIN;
        unordered_map<int, int> m;

        for (int n : popped) {
            if (m.find(n) == m.end()) {
                while (pushed.at(next_push) != n) {
                    m[pushed.at(next_push)] = next_push;
                    next_push++;
                }
                next_push++;
                max_pop = next_push;
                continue;
            }
            if (m[n] > max_pop)
                return false;
            max_pop = m[n];
            m.erase(n);
        }
        return true;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,2,3,4,5};
    vector<int> b = {4,5,3,1,2};
    cout << sol.validateStackSequences(a, b) << endl;
}