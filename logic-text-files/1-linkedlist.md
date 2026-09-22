# Linked List
Linked list is a reference variable which points to the first node.

# Node 
Create a node which will have value and reference variable for the next node

# Operations 
# Push 
There are two cases in push operation
1. If there are no nodes means head is pointing to nothing then create a new node point head to it.
2. If there is already node exist then create a variable for example last and start traverse and check whenever the last.next is none stop and create a new node point last.next to new node and now they are link

# Pop
Now there are two cases in pop
1. if there is only one node mean if self.head.next is None then set the value to self.head is None and put the value somewhere to return it.
2. if there are at least two nodes then set temp to head and move temp one time because we know there is at least two nodes and set prev to temp at last set prev.next to None and return temp.val 


# Insert 
1. insert at 0 position first create a new node point new node to the head and then point head to the new node.
2. for mid insertion: set temp to self.head and set prev to temp and move to next until the index is reached and insert between the prev and temp and connect it. stop when the list is end or the index is reach.
3. for end insertion: if we want to insert at the end of the list this case will be also handle in case 2.

# Remove
1. if the value found at first then self.head will be set on it's next
2. if it is somewhere between or at the end of the list i mean if it is not first. 
 
