class Solution {
  public void moveZeroes(int[] nums) {
    int idx = 0;
    for (int num : nums) {
      if(num!=0){
        nums[idx] = num;
        idx+=1;
      }
    }

    for(int i=idx;i<nums.length;++i){
      nums[i] = 0;
    }
  }
}