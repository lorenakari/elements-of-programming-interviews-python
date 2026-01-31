from singly_linked_list import ListNode, insert_in_list, print_list


def even_odd_merge(L: ListNode) -> ListNode:
    odd_dummy_head, even_dummy_head = ListNode(), ListNode()
    odd_tail, even_tail = odd_dummy_head, even_dummy_head

    while L:
        if L.data % 2 == 0:
            even_tail.next = L
            even_tail = even_tail.next
        else:
            odd_tail.next = L
            odd_tail = odd_tail.next
        L = L.next

    even_tail.next = odd_dummy_head.next
    odd_tail.next = None
    return even_dummy_head.next


if __name__ == "__main__":
    L = ListNode(1)
    insert_in_list(L, ListNode(5))
    insert_in_list(L, ListNode(4))
    insert_in_list(L, ListNode(2))
    insert_in_list(L, ListNode(3))
    print_list(L)

    print_list(even_odd_merge(L))
