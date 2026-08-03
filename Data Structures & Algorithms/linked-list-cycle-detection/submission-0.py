# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        tail = head

        while tail is not None:
            if tail not in visited:
                visited[tail] = True
                tail = tail.next
            else:
                return True
        
        return False
        
        