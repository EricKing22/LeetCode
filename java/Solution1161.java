public class Solution1161 {
    class Solution {
        public int maxLevelSum(TreeNode root) {
            int current_level = 1;
            int max = Integer.MIN_VALUE;
            Integer value = sumAtLevel(root, current_level);
            int level = 0;

            while(value != null){
                System.out.println(value);
                if (value > max){
                    max = value;
                    level = current_level;
                }
                current_level++;
                value = sumAtLevel(root,current_level);
            }

            return level;
        }


        public Integer sumAtLevel(TreeNode root, int level){

            if (root == null) return null;

            if (level == 1){
                return root.val;
            }

            Integer left = sumAtLevel(root.left, level-1);

            Integer right = sumAtLevel(root.right,level-1);

            if (left == null){
                if (right == null) return null;
                else return right;
            }

            else{
                if (right == null) return left;
                else return left + right;

            }

        }
    }


}
