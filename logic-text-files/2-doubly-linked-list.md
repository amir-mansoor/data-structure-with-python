# Doubly Linked List 
It is basically the same to linked list but now it also hold the referece of the previous node. so we can say it is doubly connected linked list. 

# Operations
# Push 
1. if list is empty just create a node as we do in linked list
2. but in case 2 we need to set the prev reference variable to the prev node

# Pop 
1. if there is only one node just set self.head to None
2. in second case traverse on whole list and set prev and temp as we did in linked list then set prev.next to None and maybe temp.prev to None 🤔

# Insert 
1. if we want to insert at 0 index then set new node to head and also set head to new node and set new node.prev to self.head
    1. if head is set to none
    2. if head is pointing to atleast something
2. if u want to insert at any position except 0 
