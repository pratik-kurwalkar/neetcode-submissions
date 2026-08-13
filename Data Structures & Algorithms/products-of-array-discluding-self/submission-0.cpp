class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> productList;
        for (int x = 0; x < nums.size(); x++) {
            int product = 1;
            for (int y = 0; y < nums.size(); y++) {
                // if (nums[y] == 0) {
                //     product = 0;
                //     break;
                // }
                if(x != y) {
                    product *= nums[y];
                }
            }
            productList.push_back(product);
        }
        return productList;
    }
};
