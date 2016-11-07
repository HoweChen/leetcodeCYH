class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size()!=1){
            std::sort(nums.begin(),nums.end());
        }
        return nums[0];
    }
};
