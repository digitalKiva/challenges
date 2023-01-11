class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        // Time: O(n) - but only loops the array 1 time
        // Space: O(n) (additinal)
        vector<int> sorted;
        for(int n=0; n<nums.size(); n++) {
            if (nums[n] % 2 == 0) {
                sorted.insert(sorted.begin(), nums[n]);
            } else {
                sorted.push_back(nums[n]);
            }
        }
        return(sorted);
    }
};