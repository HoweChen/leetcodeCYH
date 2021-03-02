class Solution {
  public int removeElement(int[] nums, int val) {
    int idx = 0;
    for (int num : nums) {
      if(num!=val){
        nums[idx] = num;
        idx+=1;
      }
    }

    for(int i=idx;i<nums.length;++i){
      nums[i] = nums[0];
    }
    return idx;
  }
}