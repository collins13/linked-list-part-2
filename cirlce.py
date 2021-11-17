from singlelikedlist import Node, LinkedList

class NewNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.isVisited = False;

def detect(LinkedList):
    currentNode = LinkedList.head
    currentNode.isVisited = True

    while True:
        if currentNode.next.isVisited is True:
            currentNode.next = None
            break
        currentNode = currentNode.next
        currentNode.isVisited = True


node1 = NewNode('john')
node2 = NewNode('ben')
node3 = NewNode('mathew')
LinkedList = LinkedList()

LinkedList.insert(node1)
LinkedList.insert(node2)
LinkedList.insert(node3)

node3.next = node2
detect(LinkedList);

LinkedList.printList()