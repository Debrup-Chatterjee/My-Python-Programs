class LinkedList:
     def __init__(self,value=None):
          self.value=value
          self.next=None
class SingleLinkedList:
     def __init__(self):
          self.head=None
     def addBeg(self,newval):
          temp=LinkedList(newval)
          temp.next=self.head
          self.head=temp
     def addEnd(self,newval):
          temp=LinkedList(newval)
          if self.head is None:
               self.head=temp
               return
          ptr=self.head
          while(ptr.next):
               ptr=ptr.next
          ptr.next=temp
     def del_beg(self):
          if self.head is None:
               print("The linked list is empty")
               return
          if self.head.next is None:
               self.head=None
               return
          self.head=self.head.next
     def PrintList(self):
          num=self.head
          while num is not None:
               print(num.value)
               num=num.next
slist=SingleLinkedList()
slist.head=LinkedList("MON")
node2=LinkedList("TUE")
node3=LinkedList("WED")
slist.head.next=node2
node2.next=node3
print("Initially...")
slist.PrintList()
print("After inserting at beginning:")
slist.addBeg("SUN")
slist.PrintList()
print("After inserting at end:")
slist.addEnd("THURS")
slist.PrintList()
print("After deleting from beginning:")
slist.del_beg()
slist.PrintList()


