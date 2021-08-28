#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <string>

using namespace std;;

class Solution {
public:
    int LeastInterval(const vector<char>& tasks, int n) {
        vector<int> count(26, 0);
        int max_count = 0;
        int max_count_freq = 0;
        for (char c : tasks) {
            int curr_count = ++count[c - 'A'];
            if (curr_count == max_count) {
                max_count_freq++;
            } else if (curr_count > max_count) {
                max_count = curr_count;
                max_count_freq = 1;
            }
        }
        int guess_from_max_count = (max_count-1) * (n+1) + max_count_freq;
        return max(guess_from_max_count, (int) tasks.size());
    }
};

int main() {
    Solution sol = Solution();
}