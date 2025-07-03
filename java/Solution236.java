public class Solution236 {
    class Solution {
        public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
            if (root == null || root == p || root == q) {
                // If the root is null, or we find one of the nodes, return root
                return root;
            }

            // Search in the left and right subtrees
            TreeNode left = lowestCommonAncestor(root.left, p, q);
            TreeNode right = lowestCommonAncestor(root.right, p, q);

            if (left != null && right != null) {
                // If both left and right return non-null, root is the LCA, this means p and q are in both left and right subtrees
                return root;
            }

            // Otherwise, return the non-null child (or null if both are null)
            return left != null ? left : right;
        }
    }
}