#include <vector>  
#include <iostream>
#include <math.h>
#include <queue>

using namespace std;


bool comp(pair<int, string> a, pair<int, string> b) {
    if (a.first > b.first)
        return true;
    if (a.first < b.first)
        return false;
    return a.second < b.second;
}

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        sort(words.begin(), words.end());
        priority_queue<pair<int, string>, vector<pair<int, string>>, 
            function<bool(pair<int, string>, pair<int, string>)>> q(comp);
        int size = words.size();
        int counter = 0;
        for (int i = 0; i < size; ++i) {
            if (i == 0 || words[i] == words[i-1]) {
                counter++;
                continue;
            }
            if (q.size() != k || comp({counter, words[i]}, q.top()))
                q.push({counter, words[i-1]});
            if (q.size() > k)
                q.pop();
            counter = 1;
        }
        if (counter && (q.size() != k || comp({counter, words[size-1]}, q.top())))
            q.push({counter, words[size-1]});
        if (q.size() > k)
                    q.pop();
        vector<string> res;
        while (!q.empty()) {
            res.push_back(q.top().second);
            q.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<string> words = {"i", "love", "leetcode", "i", "love", "coding", "coding"};
    // words = {"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"};
    vector<string> res = sol.topKFrequent(words, 3);
    for (string word : res) {
        cout << word << " ";
    }
    cout << endl;
}