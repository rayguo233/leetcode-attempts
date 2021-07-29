// https://leetcode.com/problems/candy/

#include <vector>  
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size();
        if (len == 1)
            return 1;

        bool was_increasing = ratings[1] > ratings[0];
        int num_equal = ratings[1] == ratings[0];
        int prev_depth = INT_MAX, curr_depth = 1 + was_increasing - num_equal;
        int total_candy = 0;
        for (int i = 2; i < len; i++ ) {
            num_equal += ratings[i] == ratings[i-1];
            // if continue increasing or decreasing
            if (was_increasing == (ratings[i] > ratings[i-1])) {
                curr_depth++;
                continue;
            }
            // if changing from increasing to decreasing
            if (was_increasing) {
                was_increasing = !was_increasing;
                prev_depth = curr_depth, curr_depth = 0;
                total_candy += get_sequence_total(prev_depth);
                continue;
            }
            // if changing from decreasing to increasing
            was_increasing = !was_increasing;
            total_candy += max(curr_depth + 2 - prev_depth, 0);
            prev_depth = curr_depth, curr_depth = 2;
            total_candy += get_sequence_total(prev_depth+1) - 1;
            num_equal = 0;
        }
        // if was increasing
        if (was_increasing) {
            total_candy += get_sequence_total(curr_depth);
            return total_candy;
        }
        // if was decreasing
        total_candy += max(curr_depth + 2 - prev_depth, 0);
        total_candy += get_sequence_total(curr_depth+1);
        return total_candy;
    }
private:
    int get_sequence_total(int depth) {
        if (depth == 1)
            return 1;
        return (1 + depth) * depth / 2;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> a = {1,2,2};
    a = {1,0,2}; // 5
    a = {1,2,2}; // 4
    a = {1,3,2,1,0}; // 11
    a = {1,3,2,2,1}; // 7
    cout << sol.candy(a) << endl;
}