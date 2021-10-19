# create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None;
    def listLength(self):
        currentNode = self.head;
        length = 0;
        while currentNode is not None:
            currentNode = currentNode.next;
            length += 1;
        return length
    def insertHead(self, newNode):
        temNode = self.head
        self.head = newNode
        self.head.next = temNode;
        del temNode
    def insertAt(self, newNode, pos):
        if pos < 0 or pos > self.listLength():
            print("invalide position");
            
        if pos == 0:
            self.insertHead(newNode);
            return
        currpos = 0;
        currNode = self.head
        while True:
            if currpos == pos:
                prevNode.next = newNode;
                newNode.next = currNode
                break
            prevNode = currNode
            currNode = currNode.next;
            currpos += 1;

                
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
    def deleteEnd(self):
        lastNode = self.head;
        while lastNode.next is not None:
            prevNode = lastNode
            lastNode = lastNode.next;
        # del lastNode
        prevNode.next = None;
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


node = Node(10);
linked = LinkedList();
firstNode = linked.insert(node)
node1 = Node(20);
secondNode = linked.insert(node1)
node2 = Node(15);
thirdNode = linked.insert(node2)
linked.deleteEnd();
linked.printList();

