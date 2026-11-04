
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True
        #Find the middle of the linked_list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the second half of the linked list
        prev = None
        curr = slow

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        #Compare the linked lists now

        left, right = head, prev
        is_pal = True

        while right:
            if left.val != right.val:
                is_pal = False
                break
            left = left.next
            right = right.next
        return is_pal




        
        