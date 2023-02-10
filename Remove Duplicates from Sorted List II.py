class Solution:
  def deleteDuplicates(self, head):
    output = ListNode(0, head)
    last_num = output

    while head:
      while head.next and head.val == head.next.val:
        head = head.next
      if last_num.next == head: last_num = last_num.next
      else: last_num.next = head.next
      
      head = head.next

    return output.next