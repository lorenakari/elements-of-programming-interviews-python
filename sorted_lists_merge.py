from singly_linked_list import ListNode, insert_in_list, print_list


def merge_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    # Iniate M with a dummy head
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    # Append the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


if __name__ == "__main__":
    L1 = ListNode(2)
    insert_in_list(L1, ListNode(7))
    insert_in_list(L1, ListNode(5))
    print_list(L1)

    L2 = ListNode(3)
    insert_in_list(L2, ListNode(11))
    print_list(L2)

    print_list(merge_sorted_lists(L1, L2))
