class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numsSet;
        int maxSequence = 0;
        for (const int& num : nums) {
            numsSet.insert(num);
        }
        for (const int& num : numsSet) {
            if (!numsSet.count(num-1)) {
                int sequence = 1;
                int nextNumber = num + 1;
                while(numsSet.count(nextNumber)) {
                    sequence++;
                    nextNumber++;
                }
                if (sequence > maxSequence) {
                    maxSequence = sequence;
                }
            }
        }
        return maxSequence;
    }
};
