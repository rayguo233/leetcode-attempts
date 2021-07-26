// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <math.h>
#include <map>

using namespace std;;

class FreqStack {
public:
    FreqStack() {
        
    }
    
    void push(int val) {
        if (num_to_freq_.find(val) == num_to_freq_.end())
            num_to_freq_[val] = 0;
        num_to_freq_[val]++;
        int freq = num_to_freq_[val];
        if (freq_to_num_.find(freq) == freq_to_num_.end()) {
            freq_to_num_[freq] = {};
        }
        freq_to_num_[freq].push_back(val);
    }
    
    int pop() {
        int num = (freq_to_num_.begin()->second).back();
        (freq_to_num_.begin()->second).pop_back();
        if ((freq_to_num_.begin()->second).empty()) {
            freq_to_num_.erase(freq_to_num_.begin()->first);
        }
        num_to_freq_[num]--;
        return num;
    }

private:
    map<int, vector<int>, greater<int>> freq_to_num_;
    map<int, int> num_to_freq_;
};

int main() {
}