// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        int size = dictionary.size();
        vector<int> ind(size, 0);
        string res = "";
        for (char c : s) {
            for (int i = 0; i < size; i++) {
                string str = dictionary[i];
                if (ind[i] == -1 || str[ind[i]] != c)
                    continue;
                ind[i]++;
                if (ind[i] == str.size()) {
                    ind[i] = -1;
                    if (str.size() > res.size()) {
                        res = str;
                    }
                    if (str.size() == res.size()) {
                        res = min(res, str);
                    }
                }
            }
        }
        return res;
    }

    string findLongestWord_slow(string s, vector<string>& dictionary) {
        int size = dictionary.size();
        vector<int> ind(size, 0);
        string res = "";
        for (char c : s) {
            for (int i = 0; i < size; i++) {
                string str = dictionary[i];
                if (ind[i] == -1 || str[ind[i]] != c)
                    continue;
                ind[i]++;
                if (ind[i] == str.size()) {
                    ind[i] = -1;
                    if (str.size() > res.size()) {
                        res = str;
                    }
                    if (str.size() == res.size()) {
                        res = min(res, str);
                    }
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<char> a = {'a','a','b','b','c','c','c'};
}