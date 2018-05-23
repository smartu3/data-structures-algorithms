#-*- coding:utf-8 -*-

#Array类似于list对象，只能存储一种类型的元素，程序需要优化内存的话，则可使用Array

# from array import array

# a = array("i",[1,2,3,4,5])
# b = array(a.typecode,(2*x for x in a))
# print type(a)
# print type(b)#type <array.array>

#array倾向于使用in-place操作，可使用enumerate:

# for i,x in enumerate(a):
	# a[i] = 2*x

#单链链表

class Node():
	def __init__(self,d=None):
		self.data = d
		self.nextNode = None
	def set_and_return_nextNode(self,d=None):
		self.nextNode = Node(d)
		return self.nextNode
	def get_data(self):
		return self.data

class LinkedList():
	def buildList(self,array):
		self.head = Node(array[0])
		self.tem = self.head
		for i in array[1:]:
			self.tem = self.tem.set_and_return_nextNode(i)
		return self.head
	def printList(self):
		tempNode = self.head
		while tempNode :
			print tempNode.get_data()
			tempNode = tempNode.nextNode

myArray = [3,5,4,6,2,6,7,8,9,10,21]
myList = LinkedList()
myList.buildList(myArray)
myList.printList()
