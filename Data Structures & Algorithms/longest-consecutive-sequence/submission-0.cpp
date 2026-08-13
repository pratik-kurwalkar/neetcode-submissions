class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // int maxSequence = 0;
        // int sequence = 0;
        // for (int x = 0; x < nums.size() - 1; x++) {
        //     if (nums[x]+1 == nums[x+1]) {
        //         cout << "A = " << nums[x] << " B = " << nums[x+1] << endl;
        //         sequence++;
        //         cout << "Sequence = " << sequence << endl;
        //     } else {
        //         if (sequence > maxSequence) {
        //             maxSequence = sequence;
        //         }
        //         sequence = 0;
        //     }
        // }
        // return maxSequence;

        // 1, 6, 7, 2, 8, 3, 4

        unordered_set<int> numsSet;
        vector<int> startingSet;
        int maxSequence = 0;
        for (const int& num : nums) {
            numsSet.insert(num);
        }
        for (const int& num : numsSet) {
            if (!numsSet.count(num-1)) {
                // Starting number
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
