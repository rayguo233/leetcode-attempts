#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    int longestSubarray(const vector<int>& nums, int limit) {
        int res = 1;
        int l = 0, r = 0;
        multiset<int> s;
        while (true) {
            while (s.empty() || *(s.rbegin()) - *(s.begin()) <= limit) {
                res = max(res, (int)s.size());
                if (r == nums.size())
                    return res;
                s.insert(nums[r]);
                r++;
            }
            while (!s.empty() && *(s.rbegin()) - *(s.begin()) > limit) {
                auto itr = s.find(nums[l]);
                s.erase(itr, ++itr);
                l++;
            }
        }
        assert(false);
        return res;
    }
};

int main() {
}