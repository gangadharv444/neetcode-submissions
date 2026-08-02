# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy  # FIX 2: Added a tracker to move forward
        
        temp1 = list1
        temp2 = list2

        # FIX 3: Changed to condition on the nodes themselves to prevent crashes
        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:  # FIX 1: Compare .val, not the objects
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next
            
            tail = tail.next  # FIX 2: Move the tracker forward!

        # Connect the remaining elements of whichever list is left
        if temp1 is not None:
            tail.next = temp1
        if temp2 is not None:
            tail.next = temp2

        # Return the actual start of the merged list (skipping the dummy 0)
        return dummy.next


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            return self.merge(list1, list2)



        