
# lets code up a simple solution
"""
## PLAN
- take 2 pointers label 1 'middle' and 1 'end'
- start a loop putting both pointers at head
- while 'end' pointer is not None 
    - increment the 'end' pointer to the next node
    - if the 'end' pointer is not None 
    - increment the 'end' pointer and the 'middle' pointer to their respective nodes.
    - When the while loop ends print out the value of the node 'middle' is pointing to
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def find_middle(self):
        middle = self
        end = self
        while end is not None:
            end = end.next

            if end:
                end = end.next
                middle = middle.next
        print(f"Middle Value is {middle.value}")

root = Node(4)
current_node = root
current_node.add(7)
current_node = current_node.next
current_node.add(9)
current_node = current_node.next
current_node.add(2)
current_node = current_node.next
current_node.add(12)
current_node = current_node.next
current_node.add(42)
current_node = current_node.next


root.find_middle()



        
        