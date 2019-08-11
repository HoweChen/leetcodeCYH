/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    // bfs method
    // public List<List<Integer>> levelOrder(Node root) {
    // if (root==null){
    // return new LinkedList();
    // }
    // List<Node> stack = new ArrayList<Node>();
    // stack.add(root);
    // List<List<Integer>> result = new LinkedList();
    // while (!stack.isEmpty()){
    // List<Integer> cls = new ArrayList<>(); // cls: current level stack
    // List<Node> tmpStack = new ArrayList<>();
    // for (Node node:stack){
    // cls.add(node.val);
    // if (node.children!=null){
    // for (Node child:node.children){
    // tmpStack.add(child);
    // }
    // }
    // }
    // stack = tmpStack;
    // result.add(cls);
    // }
    // return result;
    // }

    // solution with dfs
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> count = new ArrayList<>();
        dfs(root, 0, count);
        return count;
    }

    public void dfs(Node root, int i, List<List<Integer>> count) {
        if (root == null)
            return;
        if (i > count.size() - 1) {
            count.add(new ArrayList<Integer>());
            count.get(i).add(root.val);
        } else {
            count.get(i).add(root.val);
        }
        if (root.children != null) {
            for (Node child : root.children) {
                dfs(child, i + 1, count);
            }
        }
    }
}