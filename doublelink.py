class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.previous = None
        
        
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.previous = currentNode;
        
    def inserthead(self, newNode):
        previousNode = self.head
        self.head = newNode;
        self.head.next = previousNode
        previousNode.previous = self.head
        
    def printList(self):
        if self.head is None:
            print("list is Empty");
            return
        currentNode = self.head
        print("print at the begining")
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            if currentNode.next is None:
                reverseNode = currentNode;
            currentNode = currentNode.next
            
        print("print from end")
        
        while True:
            if reverseNode is None:
                break
            print(reverseNode.data)
            reverseNode = reverseNode.previous
        
        
nodeOne = Node("john");
nodeTwo = Node("mary");
nodeThree = Node("grace");

LinkedList = LinkedList();

LinkedList.insertEnd(nodeOne)
LinkedList.insertEnd(nodeTwo)
LinkedList.inserthead(nodeThree)

LinkedList.printList();