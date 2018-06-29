def has_cycle(self, list_head):
    if list_head is None:
        return False
    if list_head.next is not None:
        return True
