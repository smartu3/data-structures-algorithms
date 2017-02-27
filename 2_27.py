#-*- coding:utf-8 -*-
#python3
from collections import Counter#Counter函数统计item在序列中出现的次数

li=['Dog','Cat','Mouse',42,'Dog',42,'Cat','Dog']
a=Counter(li)

print a #Counter({'Dog':3,42:2,'Cat':2,'Mouse':1})
print len(set(li)) #4

print a.most_common(3) #[('Dog',3),(42,2),('Cat',2)]

#Deque 双端队列
#与list的比较结果

# import time
# from collections import deque

# num = 100000

# def append(c):
	# for i in range(num):
		# c.append(i)

# def appendleft(c):
	# if isinstance(c,deque):
		# for i in range(num):
			# c.appendleft(i)
	# else:
		# for i in range(num):
			# c.insert(0,i)

# def pop(c):
	# for i in range(num):
		# c.pop()

# def popleft(c):
	# if isinstance(c,deque):
		# for i in range(num):
			# c.popleft()
	# else:
		# for i in range(num):
			# c.pop(0)

# for container in [deque,list]:
	# for operation in [append,appendleft,pop,popleft]:
		# c = container(range(num))
		# start = time.time()
		# operation(c)
		# elapsed = time.time() - start
		# print "Completed {0}/{1} in {2} seconds: {3} ops/sec".format(
			# container.__name__,operation.__name__,elapsed,num/elapsed)
#在进行大数据的操作时，双端队列deque比list效率要更高
# from collections import deque
# q = deque(range(5))
# q.append(5)
# q.appendleft(6)
# print q
# print q.pop()
# print q.popleft()
# print q.rotate(3)
# print q
# print q.rotate(-1)
# print q
#rotate 队列的旋转操作，正参数将右端队列（参数个）移动到左端，负参数相反

#Defaultdict
#defaultdict对象适合存放追踪数据

from collections import defaultdict
s = "the quick brown fox jumps over the lazy dog"

words = s.split()
location = defaultdict(list)#搭配list可以保存插入元素顺序，搭配set能够消除重复元素
for m,n in enumerate(words):
	location[n].append(m)

print location

class Example(dict):
	def __getitem__(self,item):
		try:
			return dict.__getitem__(self,item)
		except KeyError:
			value = self[item] = type(self)()
			return value

a =Example()

a[1][2][3] =4
a[1][3][3] = 5
a[1][2]['test'] = 6

print a