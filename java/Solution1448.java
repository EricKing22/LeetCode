public class Solution1448 {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }


    class Solution {
        public int goodNodes(TreeNode root){
            return getNum(root, root.val);
        }

        public int getNum(TreeNode root, Integer max){
            int n = 0;

            if (root.val >= max){
                n++;
            }

            if (root.left != null){
                n = n + getNum(root.left, Math.max(max, root.val));
            }

            if (root.right != null){
                n = n + getNum(root.right, Math.max(max, root.val));
            }


            return n;
        }
    }
}
