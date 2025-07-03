import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;

public class Solution872 {
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
        public boolean leafSimilar(TreeNode root1, TreeNode root2){

            ArrayList<Integer> leftList = getList(root1);
            ArrayList<Integer> rightList = getList(root2);



            return leftList.equals(rightList);
        }

        ArrayList<Integer> getList(TreeNode root){
            ArrayList<Integer> list = new ArrayList();

            if (root.left != null){
                list.addAll(getList(root.left));
                if (root.right != null){
                    list.addAll(getList(root.right));
                }
            }else {
                if (root.right != null){
                    list.addAll(getList(root.right));
                }
                else {
                    list.add(root.val);
                }
            }

            return list;

        }



    }
    public static void main(String[] args) {

        TreeNode left = new Solution872().new TreeNode(76);
        TreeNode right = null;
        TreeNode test = new Solution872().new TreeNode(66,left,right);

        System.out.println(new Solution872().new Solution().getList(test));
    }

}
