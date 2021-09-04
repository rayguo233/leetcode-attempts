#include <vector>  
#include <iostream>
#include <unordered_set>
#include <algorithm>

using namespace std;

#define FindLadders findLadders
class Solution {
public:
    vector<vector<string>> FindLadders(string begin_word, string end_word, vector<string>& word_list) {
        unordered_set<string> dict;
        for (string s : word_list)
            dict.insert(s);
        if (dict.count(end_word) == 0)
            return {};
        vector<unordered_set<string>> step_to_words[2] = {{{begin_word}}, {{end_word}}};
        dict.erase(begin_word), dict.erase(end_word);
        bool end_to_begin = false;
        for (int curr_step = 0; 
             !step_to_words[end_to_begin].back().empty() || !step_to_words[!end_to_begin].back().empty(); 
             curr_step += end_to_begin, end_to_begin = !end_to_begin) 
        {
            // cout << curr_step << endl;
            unordered_set<string> matches;
            // see if there are solutions
            for (string w : step_to_words[end_to_begin][curr_step]) {
                for (int pos = 0; pos < w.length(); pos++) {
                    const char kOrigChar = w[pos];
                    for (int i = 0; i < 26; i++) {
                        w[pos] = 'a' + i;
                        if (step_to_words[!end_to_begin][curr_step+end_to_begin].count(w))
                            matches.insert(w);
                    }
                    w[pos] = kOrigChar;
                }
            }
            // if solutions found
            if (!matches.empty())
                return FindSteps(matches, step_to_words[0], step_to_words[1], end_to_begin);
            // else solutoins not found
            step_to_words[end_to_begin].push_back({});
            for (string w : step_to_words[end_to_begin][curr_step]) {
                for (int pos = 0; pos < w.length(); pos++) {
                    const char kOrigChar = w[pos];
                    for (int i = 0; i < 26; i++) {
                        w[pos] = 'a' + i;
                        if (dict.count(w) == 0)
                            continue;
                        dict.erase(w);
                        step_to_words[end_to_begin][curr_step+1].insert(w);
                    }
                    w[pos] = kOrigChar;
                }
            }
        }
        // for (auto v : step_to_words) {
        //     for (auto set : v) {
        //         for (string s : set) {
        //             cout << s << " ";
        //         }
        //         cout << endl;
        //     }
        // }
        return {};
    }
private:
    vector<vector<string>> FindSteps(unordered_set<string> &matches, vector<unordered_set<string>> &begin_to_end_steps, 
                                     vector<unordered_set<string>> &end_to_begin_steps, bool match_at_first_half) 
    {
        match_at_first_half ? begin_to_end_steps.pop_back() : end_to_begin_steps.pop_back();
        vector<vector<string>> solutions;
        for (string w : matches) {
            vector<vector<string>> some_first_half_paths = ConstructPartialPath(w, begin_to_end_steps.size()-1, begin_to_end_steps);
            vector<vector<string>> some_second_half_paths = ConstructPartialPath(w, end_to_begin_steps.size()-1, end_to_begin_steps);
            for (auto &first_half_path : some_first_half_paths) {
                for (auto &second_half_path : some_second_half_paths) {
                    solutions.push_back({});
                    solutions.back().insert(solutions.back().end(), first_half_path.rbegin(), first_half_path.rend());
                    solutions.back().push_back(w);
                    solutions.back().insert(solutions.back().end(), second_half_path.begin(), second_half_path.end());
                }
            }
        }
        return solutions;
    }
    vector<vector<string>> ConstructPartialPath(string start_word, int target_step, vector<unordered_set<string>> &step_vec) {
        if (target_step == -1)
            return {{}};
        unordered_set<string> matches;
        for (int pos = 0; pos < start_word.length(); pos++) {
            const char kOrigChar = start_word[pos];
            for (int i = 0; i < 26; i++) {
                start_word[pos] = 'a' + i;
                if (step_vec[target_step].count(start_word))
                    matches.insert(start_word);
            }
            start_word[pos] = kOrigChar;
        }
        
        vector<vector<string>> solutions;
        for (string w : matches) {
            vector<vector<string>> partial_paths = ConstructPartialPath(w, target_step-1, step_vec);
            for (auto path : partial_paths) {
                solutions.push_back({w});
                solutions.back().insert(solutions.back().end(), path.begin(), path.end());
            }
        }
        return solutions;        
    }
};

int main() {
    Solution sol = Solution();
    string begin_word = "hit", end_word = "cog";
    vector<string> word_list = {"hot","dot","dog","lot","log","cog"};
    auto res = sol.findLadders(begin_word, end_word, word_list);
    for (auto v : res) {
        for (string s : v) {
            cout << s << " ";
        }
        cout << endl;
    }
}