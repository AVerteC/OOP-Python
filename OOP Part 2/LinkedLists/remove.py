def remove(self, list_head, val):
    if list_head is not None:
        if list_head == val:
            list_head = list_head.next
            list_head = None
            return
    while list_head is not None:
        if list_head.content == val:
            break
        back = list_head
        list_head = list_head.next

    if list_head is None:
        return
    back.next = list_head.next