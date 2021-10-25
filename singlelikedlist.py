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
            print("invalid position");
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
    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False;

    def deleteHead(self):
        if self.isListEmpty() == False:
            previousNode = self.head
            self.head = self.head.next;
            previousNode.next = None;
        else:
            print("the list is empty");

    def deleteEnd(self):
        if self.isListEmpty == False:
            if self.head.next is None:
                self.deleteHead();
                return
            lastNode = self.head;
            while lastNode.next is not None:
                prevNode = lastNode
                lastNode = lastNode.next;
            # del lastNode
            prevNode.next = None;
        else:
            print("the list is empty");
    def deleteAt(self, position):
        if position < 0 and position >= self.listLength():
            print("invalid position")
            return;
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead
                return
            currentNode = self.head;
            currentPos = 0;
            while True:
                if currentPos == position:
                    prevNode.next = currentNode.next
                    currentNode.next = None;
                    break
                prevNode = currentNode
                currentNode = currentNode.next
                currentPos += 1;


                
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
node1 = Node(15);
secondNode = linked.insert(node1)
node2 = Node(20);
thirdNode = linked.insert(node2)
linked.deleteAt(1)
# linked.deleteEnd()
linked.printList();

