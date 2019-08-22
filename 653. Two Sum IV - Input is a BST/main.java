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
    HashSet<Integer> result = new HashSet<>();
    // dfs
    public boolean findTarget(TreeNode root, int k) {
        if (root==null){
            return false;
        }
        if (result.contains(k-root.val)){
            return true;
        } else {
            result.add(root.val);
            return findTarget(root.left, k) || findTarget(root.right,k);
        }
    }
    
    // bfs
    // public boolean findTarget(TreeNode root, int k) {
    //     if (root== null) return false;
    //     Queue<TreeNode> nodeQ = new LinkedList<TreeNode>();
    //     nodeQ.offer(root);
    //     while(nodeQ.size()!=0){
    //         TreeNode node = nodeQ.poll();
    //         if (result.contains(k-node.val)) return true;
    //         else {
    //             result.add(node.val);
    //             if (node.left != null) nodeQ.offer(node.left);
    //             if (node.right!=null) nodeQ.offer(node.right);
    //         }
    //     }
    //     return false;
    // }
}