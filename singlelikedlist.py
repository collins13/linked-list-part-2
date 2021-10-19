# create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None;

    def insertHead(self, newNode):
        temNode = self.head
        self.head = newNode
        self.head.next = temNode;
        del temNode

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            # self.head.next = newNode;
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode =  lastNode.next;
            lastNode.next = newNode;
    def printList(self):
        currentnode = self.head
        if self.head is None:
            print("List is empty")
            return
            
        while True:
            if currentnode is None:
                break
            
            print(currentnode.data)
            currentnode = currentnode.next


node = Node("john");
linked = LinkedList();
firstNode = linked.insert(node)
node1 = Node("james");
firstNode = linked.insert(node1)
node2 = Node("rashid");
firstNode = linked.insertHead(node2)
linked.printList();
