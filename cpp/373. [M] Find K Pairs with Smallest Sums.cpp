#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int size1 = nums1.size();
        int size2 = nums2.size();
        int curr1 = 0; 
        int next1 = 1; 
        int curr2[size2];
        for (int i = 0; i < size2; i++)
            curr2[i] = 0;
        vector<vector<int>> res;
        while (curr1 < size1 && k) {
            int cf = nums1[curr1], cs = nums2[curr2[curr1]];
            if (next1 >= size1 || cf + cs <= nums1[next1] + nums2[curr2[next1]]) {
                res.push_back({cf, cs});
                k--;
                curr2[curr1]++;
                if (curr2[curr1] == size2) {
                    curr1++;
                    if (next1 == curr1)
                        next1++;
                }
                continue;
            }
            res.push_back({nums1[next1], nums2[curr2[next1]]});
            k--;
            curr2[next1]++;
            while (next1+1 < size1 && nums1[next1] + nums2[curr2[next1]] > nums1[next1+1] + nums2[curr2[next1+1]])
                next1++;
            if (next1 == size1-1 && next1 > curr1+1 && 
                nums1[next1] + nums2[curr2[next1]] < nums1[curr1+1] + nums2[curr2[curr1+1]])
            {
                next1 = curr1 + 1;
                while (next1+1 < size1 && nums1[next1] + nums2[curr2[next1]] > nums1[next1+1] + nums2[curr2[next1+1]])
                    next1++;
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {10,2};
}