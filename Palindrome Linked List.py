class Solution:
  def isPalindrome(self, head):
    def reverseList(head):
      last = None
      current = head
      while current:
        next = current.next
        current.next = last
        last = current
        current = next
      return last
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    if fast: slow = slow.next
    slow = reverseList(slow)
    while slow:
      if slow.val != head.val: return False
      slow = slow.next
      head = head.next
    return True