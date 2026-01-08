# Singly Linked List

class SinglyNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
def display(head):
    curr = head 
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(element))

def search(head, val):
    curr = head 
    # count = 0
    while curr:
        if int(curr.val) == val:
            return True
        curr = curr.next
        # count += 1

    return False



if __name__ == "__main__":
    Head = SinglyNode(1)
    A = SinglyNode(2)
    B = SinglyNode(3)
    C = SinglyNode(4)

    Head.next = A
    A.next = B 
    B.next = C 

    # Traverse the list - O(n)
    curr = Head
    while curr:
        print(curr)
        curr = curr.next

    # Display linked list - O(n)
    display(Head)

    # Search Linked List - O(n)
    print(search(Head, 2)) # True
    print(search(Head, 5)) # False