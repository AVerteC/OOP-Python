# this goes in the SinglyList class

s
def print_list(self, list_head):
    while list_head is not None:
        print(list_head.content)
        list_head = list_head.next
