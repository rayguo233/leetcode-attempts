// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <unordered_map>
#include <iostream>
#include <map>
#include <string>
#include <math.h>

using namespace std;

class TimeMap {
private:
    unordered_map<string, map<int, string>> m_map;
public:
    /** Initialize your data structure here. */
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        m_map[key].insert({ timestamp, value });
    }
    string get(string key, int timestamp) {
        auto it = m_map[key].upper_bound(timestamp);
        return it == m_map[key].begin() ? "" : prev(it)->second;
    }
};

int main() {
    TimeMap sol = TimeMap();
    cout << ceil((1 + 2) / 2.) << endl;
}