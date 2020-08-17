import java.util.Map;

/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] result = new int[2];

        Map<Integer, Integer> intMap = new HashMap<>();
        if (nums.length == 0) {
            return nums;
        }

        for (int i = 0; i < nums.length; i++) {
            int another = target - nums[i];
            if (intMap.get(another) != null && intMap.get(another) != i) {
                result[0] = intMap.get(another);
                result[1] = i;
                return result;
            } else {
                intMap.put(nums[i], i);
            }
        }
        return result;
    }
}
// @lc code=end
