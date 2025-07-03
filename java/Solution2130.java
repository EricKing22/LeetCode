import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class Solution2130 {
    class ListNode {

        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    class Solution {
        public int pairSum(ListNode head){

            int length = 1;

            ListNode mid = head;
            ListNode current = head;

            while (current.next != null){
                length++;
                current = current.next;
            }

            int middle = length / 2;


            for (int i = 0; i < middle-1; i++){
                mid = mid.next;
            }

            ListNode newHead = reverseList(mid.next);




            int max = 0;
            for (int i = 0; i < middle; i++){
                int a = head.val;
                int b = newHead.val;
                int sum = a + b;

                if (sum > max) max = sum;
                head = head.next;
                newHead = newHead.next;

            }

            return max;
        }

        public ListNode reverseList(ListNode head) {
            Stack<ListNode> stack = new Stack<>();

            ListNode current = head;
            while (current != null) {
                stack.add(current);
                current = current.next;
            }

            if(stack.isEmpty()) return null;

            ListNode newHead = stack.pop();
            current = newHead;

            while (!stack.isEmpty()) {
                current.next = stack.pop();
                current = current.next;
            }

            current.next = null;


            return newHead;
        }


    }

}
