// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {
        
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        follow(userId, userId);
        m_userToTweet[userId].push_back({m_time, tweetId});
        m_time++;
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> feed;
        const auto followees = m_userToFollowee[userId];
        const int numFollowee = followees.size();
        vector<int> ptr(numFollowee, -2);
        while (true) {
            int i = 0;
            int maxI = -1;
            pair<int, int> mostRecentTweet;

            // find the most recent tweet
            for (int f : followees) {
                auto tweets = m_userToTweet[f];
                if (ptr[i] == -2)
                    ptr[i] = tweets.size()-1;
                int tweetPtr = ptr[i];
                if (tweetPtr >= 0) {
                    if (maxI == -1) {
                        maxI = i;
                        mostRecentTweet = tweets[tweetPtr];
                    } else if (tweets[tweetPtr].first > mostRecentTweet.first) {
                        maxI = i;
                        mostRecentTweet = tweets[tweetPtr];
                    }
                }
                i++;
            }

            if (maxI != -1) {
                ptr[maxI]--;
                feed.push_back(mostRecentTweet.second);
            }
            if (maxI == -1 || feed.size() == 10)
                break;
        }
        assert(feed.size() <= 10);
        return feed;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        m_userToFollowee[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        m_userToFollowee[followerId].erase(followeeId);
    }
private:
    unordered_map<int, vector<pair<int, int>>> m_userToTweet;
    unordered_map<int, unordered_set<int>> m_userToFollowee;
    int m_time = 0;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */

int main() {
    unordered_set<int> m;
    m.erase(1);
}