# How do you find and return the middle node of a singly linked list in one pass? 
- You do not have access to the length of the list. 
- If the list is even, you should return the first of the two "middle" nodes. 
- You may not store the nodes in another data structure.

## PLAN
- take 2 pointers label 1 'middle' and 1 'end'
- start a loop putting both pointers at head
- while 'end' pointer is not None 
    - increment the 'end' pointer to the next node
    - if the 'end' pointer is not None 
    - increment the 'end' pointer and the 'middle' pointer to their respective nodes.
    - When the while loop ends print out the value of the node 'middle' is pointing to