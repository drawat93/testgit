#from ..Week1 import  LinkedList
class entry:

    def __init__(self,name,number):
        self.data=[name,number]
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def Insert(self, node):
        #node = entry(new_data)
        tmp = self.head
        if (tmp is not None):
            while (tmp.next is not None):
                tmp = tmp.next
            self.tail = tmp
            self.tail.next = node
            self.tail = node
            # node.next = None
        else:
            self.head = node
            self.tail = node

    def Pop(self):
        tmp = self.head
        if (tmp is not None):
            while (tmp.next.next is not None):
                tmp = tmp.next
            tmp.next = None
            self.tail = tmp
        else:
            print('Empty List')

    def FrontPop(self):
        if self.head is not None:
            tmp = self.head.next
            self.head = None
            self.head = tmp
        else:
            print('Empty List')

    def find_replace(self,node):
        tmp = self.head
        if (tmp is not None):
            while(tmp is not None):
                if(tmp.data[1]==node.data[1]): #comparing phone number
                    tmp.data[0]=node.data[0] #changing name
                    #print(True)
                    return True #same number
                tmp=tmp.next
            #print(False)
            return False

    def find(self, number):
        tmp = self.head
        if (tmp is not None):
            while (tmp is not None):
                if (tmp.data[1] == number):  # comparing phone number
                    #print(True)
                    return tmp.data[0]  # return name
                tmp = tmp.next
            #print(False)
            return False
    def deleteN(self,key):
        tmp=self.head
        found=0
        if(tmp is not None):
            if(key==self.head.data[1]):
                print('if1')
                self.FrontPop()
            elif(key==self.tail.data[1]):
                print('elif2')
                self.Pop()
            elif(tmp.next is not None):
                print('if3')
                while(tmp.next.next is not None):
                    if(tmp.next.data[1]==key):
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
class phoneBook:

    def __init__(self,a,b,prime):
        self.a=a
        self.b=b
        self.prime=prime
        self.map=[0]*(1000)


    def add_number(self,name,number):
        user_detail = entry(name, number)
        #print(user_detail.data)
        hash=self.hash_number(number)
        #print('hash value ',hash)
        if(self.map[hash]==0):
            #print('if')
            list = LinkedList()
            list.Insert(user_detail)
            self.map[hash]=list
        else:
            if(self.map[hash].find_replace(user_detail)): #phone_number already exist and replacing names
                print('replaced existing contact with new name ',name)
            else:
                self.map[hash].Insert(user_detail)

    def find(self,number):
        hash_value=self.hash_number(number)
        #print('hash ',hash_value)
        if(self.map[hash_value]==0):
            print('Number does not exist in phone book')
        else:
            #print('else')
            list=self.map[hash_value]
            print('Name of given phone number is ',list.find(number))

    def hash_number(self,number):
        hash=(number*self.a + self.b) % self.prime
        hash=hash%1000
        return hash

    def delete_number(self,number):
        hash_value = self.hash_number(number)
        print('hash ',hash_value)
        if (self.map[hash_value] == 0):
            print('Number does not exist in phone book')
        else:
            print('else')
            list = self.map[hash_value]
            print(list)
            print('Name of given phone number is ', list.find(number))
            list.deleteN(phone)

if __name__ == '__main__':

    phone=9876543
    prime=10000019
    a=31
    b=5
    p=phoneBook(a,b,prime)

    p.add_number('Deepanshu',phone)
    p.add_number('Ander', phone+2)
    p.add_number('Jane', phone+3)
    ll=p.map[268]
    print(p.map[268].head.data)
    p.find(123)
    p.delete_number(phone)
    p.delete_number(312213123123)

    print(p.map[268].head)


