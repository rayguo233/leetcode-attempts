// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        int num_words = words.size();
        int num_puz = puzzles.size();
        vector<int> w(num_words, 0);
        vector<int> res(num_puz, 0);
        for (int i = 0; i < num_words; i++) {
            string word = words.at(i);
            for (char c : word) {
                w.at(i) |= 1 << (c - 'a');
            }
        }
        for (int i = 0; i < num_puz; i++) {
            string puzzle = puzzles.at(i);
            int mask = ~0;
            int first_letter_mask = 1 << (puzzle.at(0) - 'a');
            for (char c : puzzle) {
                mask &= ~(1 << (c - 'a'));
            }
            for (int j = 0; j < num_words; j++) {
                if ((first_letter_mask & w.at(j)) == first_letter_mask && ((w.at(j) & mask) == 0)) {
                    res.at(i)++;
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<string> words = {"apple","pleas","please"};
    vector<string> puzzles = {"aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"};
    vector<int> res = sol.findNumOfValidWords(words, puzzles);
    for (int i : res)
        cout << i << ' ';
    cout << endl;
}