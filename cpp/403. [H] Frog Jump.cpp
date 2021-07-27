#include <vector>  
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <set>

using namespace std;

class Solution {
public:
    bool canCross(vector<int>& stones) {
        int target = stones.back();
        if (target == 1)
            return true;
        int len = stones.size();
        unordered_map<int, unordered_set<int>> map;
        map[1] = {1};
        int i;
        for (i = 1; i < len; i++) {
            int stone = stones.at(i);
            if (map.find(stone) == map.end())
                continue;
            // get stones that can be reached
            unordered_set<int> prev_jumps = map[stone];
            set<pair<int, int>> next_stones;
            for (int prevj : prev_jumps) {
                next_stones.insert({stone+prevj-1, prevj-1});
                next_stones.insert({stone+prevj+1, prevj+1});
                next_stones.insert({stone+prevj, prevj});
            }
            // modify stones that can be reached
            int j = i + 1;
            for (pair<int, int> p : next_stones) {
                while (j < len && stones.at(j) < p.first)
                    j++;
                if (j == len)
                    break;
                int next_stone = stones.at(j);
                if (next_stone > p.first)
                    continue;
                if (next_stone == target)
                    return true;
                if (map.find(next_stone) == map.end())
                    map[next_stone] = {p.second};
                else
                    map[next_stone].insert(p.second);
            }
            map.erase(stone);
        }
        return false;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> v = {0,1,3,5,6,8,12,17};
    cout << sol.canCross(v) << endl;
}