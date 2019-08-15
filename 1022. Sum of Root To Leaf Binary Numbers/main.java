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
    int ans = 0;
    public int sumRootToLeaf(TreeNode root) {
        dfs(root,0);
        return ans;
    }
    private void dfs(TreeNode root, int val){
        if (root==null) return;
        val = val << 1 | root.val;
        if(root.left == null && root.right == null) ans+= val;
        dfs(root.left,val);
        dfs(root.right,val);
    }
}