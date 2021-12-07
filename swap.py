from singlelikedlist import Node, LinkedList;

def swap(LinkedList, dataOne, dataTwo):
    currentnode = LinkedList.head;
    previousFirst = None;
    previousTwo = None;
    
    while True:
        if currentnode.data == dataOne:
            firstNode = currentnode;
            break
        previousFirst = currentnode
        currentnode = currentnode.next
    currentnode = LinkedList.head;
    
    while True:
        if currentnode.data == dataTwo:
            secondNode = currentnode
            break
        previousTwo = currentnode
        currentnode = currentnode.next;
    previousFirst.next = secondNode
    nextSecond = secondNode.next
    secondNode.next = firstNode.next
    previousTwo.next = firstNode
    firstNode.next = nextSecond;

oneNode = Node(4)
twoNode = Node(3)
threeNode = Node(5)
fourNode = Node(2)
fiveNode = Node(7)
sixNode = Node(1)

linkedList = LinkedList();

linkedList.insert(oneNode);
linkedList.insert(twoNode);
linkedList.insert(threeNode);
linkedList.insert(fourNode);
linkedList.insert(fiveNode);
linkedList.insert(sixNode);
swap(linkedList, 3,7);
linkedList.printList();