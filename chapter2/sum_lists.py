"""Solution to 2.5 Sum Lists.

You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in /reverse/ order, such
that the 1's digit is at the head of the list. Write a function that
adds the two numbers and returns the sum as a linked list. (You are not
allowed to "cheat" and just convert the linked list to an integer.)

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above
problem.

EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912
"""

from chapter2.node import LinkedList, Node


def sum_reverse_lists(head1: LinkedList, head2: LinkedList) -> LinkedList:
    """Returns sum of given lists as a linked list.

    The digits are stored in /reverse/ order.
    """
    sentinel = tail = Node(0)
    carry = 0
    while head1 or head2 or carry:
        sum_ = carry
        if head1:
            sum_ += head1.data
            head1 = head1.next
        if head2:
            sum_ += head2.data
            head2 = head2.next
        tail.next = Node(sum_ % 10)
        carry = sum_ // 10
        tail = tail.next
    return sentinel.next


def sum_forward_lists(head1: LinkedList, head2: LinkedList) -> LinkedList:
    """Returns sum of given lists as a linked list.

    The digits are stored in forward order.
    """
    def reverse_list(head: LinkedList) -> LinkedList:
        if not head:
            return None
        curr = head.next
        head.next = None
        prev = head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_
        return prev
    tail1, tail2 = reverse_list(head1), reverse_list(head2)
    ret = reverse_list(sum_reverse_lists(tail1, tail2))
    reverse_list(tail1)
    reverse_list(tail2)
    return ret
