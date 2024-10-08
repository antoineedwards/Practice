class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, *dataItems):
        for data in dataItems:
            newNode = Node(data)
            #if there are no items in the list
            if self.head is None:
                self.head = newNode
            else:
                lastNode = self.head
                while lastNode.next:
                    lastNode = lastNode.next
                lastNode.next = newNode
    def insert_at_start(self, *dataItems):
        for data in dataItems[::-1]:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def printList(self):
        currNode = self.head
        while currNode:
            print(currNode.data)
            currNode = currNode.next

    '''def sortList(self):
        currNode = self.head
        while currNode:
            nextNode = currNode.next
            if nextNode < currNode.data:
                nextNode.next = currNode
                currNode = nextNode'''

    def removeNode(self, n):
        lastNode = self.head
        count = 1
        while count < n-1:
            lastNode = lastNode.next
            count+=1
        lastNode.next = lastNode.next.next

def main():
    newList = LinkedList()
    newList.insert_at_end(5,10,15,20,25)
    newList.insert_at_start(2,3)
    newList.removeNode(5)
    newList.printList()
main()