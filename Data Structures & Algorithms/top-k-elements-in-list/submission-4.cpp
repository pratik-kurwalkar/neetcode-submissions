class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        unordered_map<int, int> numCount;
        for (const int& num : nums) {
            auto it = numCount.find(num);
            if(it == numCount.end()) {
                numCount[num] = 1;
            } else {
                numCount[num]++;
            }

        }
        vector<pair<int, int>> numList;
        for (const pair<int, int>& p : numCount) {
            pair<int, int> temp;
            temp.first = p.second;
            temp.second = p.first;
            numList.push_back(temp);
        }
        sort(numList.begin(), numList.end());
        auto it = numList.rbegin();
        for (int x = 0; x < k; x++) {
            pair<int, int> values = *it++;
            result.push_back(values.second);
            // cout << "--" << values.first << endl;
        }
        return result;
    }
};
