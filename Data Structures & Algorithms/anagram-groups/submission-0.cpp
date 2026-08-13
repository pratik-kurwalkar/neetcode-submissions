class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        vector<vector<string>> anagramList;
        unordered_map<string, vector<string>> map;

        for (int x = 0; x < strs.size(); x++) {
            string sortedString = strs[x];
            sort(sortedString.begin(), sortedString.end());
            auto it = map.find(sortedString);
            if (it == map.end()) {
                vector<string> vec = {strs[x]};
                map[sortedString] = vec;
            } else {
                vector<string> vec = map[sortedString];
                vec.push_back(strs[x]);
                map[sortedString] = vec;
            }
        }
        for (const auto& pair : map) {
            anagramList.push_back(pair.second);
        }

        return anagramList;
    }
};
