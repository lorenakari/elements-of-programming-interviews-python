"""Singly linked list class."""


class ListNode:
    """Node for singly linked list."""

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def search_in_list(L: ListNode, key: int):
    """Search node in list by key (if data corresponds to the key,
    return node.) O(n) time complexity."""
    while L and L.data != key:
        L = L.next

    # If the key was not present in the list, L will become None (you have
    # reached the tail of the list).
    return L


def insert_in_list(node: ListNode, new_node: ListNode) -> None:
    """Insert new node after given node. O(1) time complexity."""
    new_node.next = node.next
    node.next = new_node


def delete_node(node: ListNode) -> None:
    """Delete node after the given node. O(1) time complexity."""
    deleted_node = node.next
    node.next = deleted_node.next


def print_list(L: ListNode) -> None:
    print("List:")
    while L:
        print(L.data)
        L = L.next


if __name__ == "__main__":
    L = ListNode()
    print_list(L)
    node_1 = ListNode(1)
    insert_in_list(L, node_1)
    print_list(L)
    node_2 = ListNode(2)
    insert_in_list(node_1, node_2)
    print_list(L)
    node_3 = ListNode(3)
    insert_in_list(node_2, node_3)
    print_list(L)
    delete_node(node_1)
    print_list(L)
