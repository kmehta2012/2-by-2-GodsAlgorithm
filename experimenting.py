"""
Timeline of the project:
1. To revise python - implement a fucking link list
2. Implement BFS on list rep
3. Finish the moves of the project and how the user gives input 
4. Finish the BFS on a dynamic graph ? - most challenging (I don't see how a 2-way BFS would be better tho?)

Today's Goal:
Linked list
BFS 
(almost finish permutations)
"""



#Linked List
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    """
    Insert
    Delete
    Search
    Return max/min
    Return succc/prededcc
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, node): #Seems to be working fine

        #Insert a node to the end of the list
        #node = Node(value)
        if self.head is None:
            #Linked List is empty
            self.head = Node(None)
            self.tail = Node(None)
            self.head.next = node
            self.tail.prev = node
            node.prev = self.head
            node.next = self.tail
        else:
            """
            Need to insert node in between tail and the current last node of the list (say lastNode)
            What things would I need to update?
                1. lastNode.next = node
                2. node.prev = lastNode
                3. node.next = tail
                4. tail.prev = node
            """
            node.prev = self.tail.prev
            node.next = self.tail
            node.prev.next = node
            self.tail.prev = node

    def deleteByPosition(self, pos = None):
        #delete node at pos position in the linked list
        
        if self.head is None:
            return "list is empty \n"

        elif pos is None:
            #if no position is passed then delete the last element by default
            deleteNode = self.tail.prev
            self.tail.prev = None
            self.tail.prev = deleteNode.prev
            deleteNode = None
            self.tail.prev.next = self.tail
        
        
        else:
            node = self.head.next
            i = 1
            while i  < pos and node is not self.tail:
                node = node.next
                i += 1
            
            if node != self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev
                node = None
            else:
                return f"List does not have {pos} elements\n"
        
                
    
    def printList(self):
        if self.head is not None:
            node  = self.head.next
            i = 1
            while node is not self.tail:
                print(f"{i}. {node.value}")
                i += 1
                node = node.next
        else:
            return "List Empty"
    


linkList = LinkedList()
j = 10
for i in range(1, 4):
    node = Node(j)
    j = j + 10
    linkList.insert(node)



linkList.printList()

print("Delete the 4th pos:\n")
print(linkList.deleteByPosition(4))

print("delete the third pos: \n")
linkList.deleteByPosition(3)
linkList.printList()

print("delete the second position \n")
linkList.deleteByPosition(2)

linkList.printList()



    

    


