// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <map>
#include <string>

using namespace std;;

#define CountOfAtoms countOfAtoms

class Solution {
public:
    string CountOfAtoms(string formula) {
        map<string, int> total_map;
        int start = 0;
        CountAtomsFrom(formula, start, total_map);
        string res = "";
        for (auto itr = total_map.begin(); itr != total_map.end(); ++itr) {
            res += itr->first;
            if ((itr->second) > 1)
                res += to_string(itr->second);
        }
        return res;
    }
private:
    void CountAtomsFrom(string &formula, int &start, map<string, int> &total_map) {
        const int kSize = formula.size();
        map<string, int> curr_map;
        while (start < kSize) {
            if (formula[start] == ')') {
                start++;
                if (start == kSize || !isdigit(formula[start]))
                    return merge_maps(curr_map, total_map, 1);
                string freq_str = "";
                for (; start < kSize && isdigit(formula[start]); ++start)
                    freq_str += formula[start];
                return merge_maps(curr_map, total_map, stoi(freq_str));
            }
            if (formula[start] == '(') {
                start++;
                CountAtomsFrom(formula, start, curr_map);
                continue;
            }
            assert(isupper(formula[start]));
            string atom_name = "";
            atom_name += formula[start];
            for (start++; start < kSize && islower(formula[start]); start++)
                atom_name += formula[start];
            string atom_freq = "";
            for (; start < kSize && isdigit(formula[start]); start++)
                atom_freq += formula[start];
            if (atom_freq == "")
                atom_freq = "1";
            curr_map[atom_name] += stoi(atom_freq);
        }
        return merge_maps(curr_map, total_map, 1);
    }

    void merge_maps(const map<string, int> &from, map<string, int> &to, int freq) {
        for (auto itr = from.begin(); itr != from.end(); itr++) {
            to[itr->first] += (itr->second) * freq;
        }
    }
};

int main() {
    Solution sol = Solution();
    string f = "MgOH2P";
    cout << sol.countOfAtoms(f) << endl;
}