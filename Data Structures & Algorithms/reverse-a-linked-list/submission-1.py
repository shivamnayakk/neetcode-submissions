class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head

        previous = None

        while temp is not None:

            front = temp.next
            temp.next = previous
            previous = temp
            temp = front

        return previous

        