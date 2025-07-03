import javax.swing.*;
import java.util.List;

public class Solution328 {

    public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }

        @Override
        public String toString() {
            return String.valueOf(val);
        }
    }

    class Solution {
        public ListNode oddEvenList(ListNode head) {

            if (head == null || head.next == null) return head;

            ListNode odd = head;
            ListNode even = head.next;
            ListNode evenStart = head.next;

            while(even != null && even.next != null){
                odd.next = even.next;
                odd = odd.next;
                even.next = odd.next;
                even = even.next;

            }

            odd.next = evenStart;

            return head;
        }

    }

    public static void main(String[] args) {
        Solution328 ss = new Solution328();
        ListNode head = ss.new ListNode(1, ss.new ListNode(2));

        Solution s = ss.new Solution();
        System.out.println(s.oddEvenList(head));
    }

}
