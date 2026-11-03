
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        n = 0
        m = 0

        while a != None:
            n += 1
            a = a.next

        while b != None:
            m += 1
            b = b.next

        a = headA
        b = headB

        while n > m:
            a = a.next
            n -= 1

        while m > n:
            b = b.next
            m -= 1

        while a != None:
            if a is b:
                return a

            a = a.next
            b = b.next

        return None
