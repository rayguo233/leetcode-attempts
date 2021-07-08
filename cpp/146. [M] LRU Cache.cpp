// https://leetcode.com/problems/lru-cache/

#include <list>
#include <utility>
#include <unordered_map>

using namespace std;


class LRUCache {
private:
    int m_size;
    list<pair<int, int>> m_list;
    unordered_map<int, list<pair<int, int>>::iterator> m_map;

public:
    LRUCache(int capacity) : m_size(capacity) {}
    
    int get(int key) {
        auto itr = m_map.find(key);
        if (itr != m_map.cend()) {
            m_list.splice(m_list.begin(), m_list, m_map[key]);
            return m_map[key]->second;
        }
        return -1;
    }
    
    void put(int key, int value) {
        // if key found
        if (m_map.find(key) != m_map.end()) {
            m_map[key]->second = value;
            m_list.splice(m_list.begin(), m_list, m_map[key]);
            return;
        }

        if (m_list.size() != m_size) {
            m_list.push_front({key, value});
            m_map[key] = m_list.begin();
            return;
        }

        int d_key = m_list.back().first;
        m_map.erase(key);
        m_list.pop_back();

        m_list.push_front({key, value});
        m_map[key] = m_list.begin();
    }
};