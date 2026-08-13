class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int totalProduct = 1;
        int zeroCount = 0;
        vector<int> productList;
        for (int x = 0; x < nums.size(); x++) {
            if (nums[x] != 0) {
                totalProduct *= nums[x];
            } else {
                zeroCount++;
            }
        }
        if(zeroCount > 1) {
            totalProduct = 0;
        }

        for (int x = 0; x < nums.size(); x++) {
            if(nums[x] != 0) {
                if (zeroCount > 0) {
                    productList.push_back(0);
                } else {
                    productList.push_back(totalProduct/nums[x]);
                }
            } else {
                productList.push_back(totalProduct);
            }
        }
        return productList;
    }
};
