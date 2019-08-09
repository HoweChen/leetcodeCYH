/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        if (root1 == null || root2==null){
            return false;
        } else if (root1==null && root2==null){
            return true;
        } else {
            List<Integer> lvsOne = new ArrayList<>();
            List<Integer> lvsTwo = new ArrayList<>();
            dfs(root1,lvsOne);
            dfs(root2,lvsTwo);
            return lvsOne.equals(lvsTwo);
        }
    }
    
    public void dfs(TreeNode node, List<Integer> lvs){
        if (node!=null){
            if (node.left == null && node.right ==null){
                lvs.add(node.val);
            } else {
                dfs(node.left,lvs);
                dfs(node.right,lvs);
            }
        }
        return;
    }
}