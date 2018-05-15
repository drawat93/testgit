class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def printList(self):
        tmp=self.head
        while(tmp is not None):
            print(tmp.data,end=' ')
            tmp=tmp.next

    def Frontpush(self,new_data):
        node=Node(new_data)
        node.next=self.head
        self.head=node

    def Insert(self, new_data):
        node = Node(new_data)
        tmp=self.head
        previous = tmp
        if (tmp is not None):
            if (self.head == self.tail and self.head is not None):
                self.head.next = node
                self.tail = node
                self.tail.prev = self.head
            else:
                while(tmp.next is not None):
                    previous=tmp
                    tmp=tmp.next
                previous=previous.next
                self.tail = tmp
                self.tail.next=node
                self.tail=node
                self.tail.prev = previous
                print('Prev: ', previous.data)
        else:
            self.head=node
            self.tail=node
        print('Inserted: ',self.tail.data)


    def Pop(self):
        tmp = self.head
        if (tmp is not None):
            while(tmp.next.next is not None):
                tmp = tmp.next
            tmp.next=None
            self.tail=tmp
        else:
            print('Empty List')

    def FrontPop(self):
        if self.head is not None:
            tmp = self.head.next
            self.head = None
            self.head=tmp
        else:
            print('Empty List')

    def deleteN(self,key):
        tmp=self.head
        found=0
        if(tmp is not None):
            if(key==self.head.data):
                self.FrontPop()
            elif(key==self.tail.data):
                self.Pop()
            elif(tmp.next is not None):
                while(tmp.next.next is not None):
                    if(tmp.next.data==key):
                        found=1
                        break
                    tmp=tmp.next
                if (found==1):
                    print('Deleted Node: ',tmp.next.data)
                    end_node=tmp.next.next
                    tmp.next=None
                    tmp.next=end_node
                else:
                    print('Key does not exist in LinkedList')
            else:
                if (tmp.data == key):
                    tmp=None

        else:
            print('Empty List')

    def reversePrint(self):
        tmp = self.tail
        print('tmp',tmp.data)
        while(tmp is not None):
            print(tmp.data, end=' ')
            tmp = tmp.prev


if __name__=='__main__':
    llist=DoubleLinkedList()

    for i in range(1,6):
       # print(i)
        llist.Insert(i)

    llist.printList()
    llist.reversePrint()
    #llist.Pop()
    #llist.FrontPop()
    #llist.deleteN(5)

    #llist.printList()
