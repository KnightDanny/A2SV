class Solution:
  def deleteDuplicates(self, head):
    current_num = head

    while current_num:
      while current_num.next and current_num.val == current_num.next.val:
        current_num.next = current_num.next.next
      current_num = current_num.next

    return head