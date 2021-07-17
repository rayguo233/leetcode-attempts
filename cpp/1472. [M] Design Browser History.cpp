// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>

using namespace std;

class BrowserHistory {
public:
    BrowserHistory(string homepage) : m_his({homepage}), m_currpage(0) {}
    
    void visit(string url) {
        if (m_currpage + 1 != m_his.size()) {
            m_his.resize(m_currpage + 1);
        }
        m_his.push_back(url);
        m_currpage++;
    }
    
    string back(int steps) {
        m_currpage = max(0, m_currpage-steps);
        return m_his[m_currpage];
    }
    
    string forward(int steps) {
        m_currpage = min(m_his.size()-1, (unsigned long)m_currpage+steps);
        return m_his[m_currpage];
    }
private:
    vector<string> m_his;
    int m_currpage;
};

int main() {

}