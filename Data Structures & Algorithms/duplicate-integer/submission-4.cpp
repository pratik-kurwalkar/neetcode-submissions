class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (int x = 0; x < nums.size(); x++) {
            if (set.count(nums[x])) {
                return true;
            } else {
                set.insert(nums[x]);
            }
        }
        return false;
    }
};