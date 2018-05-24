# coding:utf-8
# python3


# 定义一个Date类
class Date(object):
	def __init__(self, year, month, day):
		if not isinstance(year, int) or not isinstance(month, int) or\
		not isinstance(day, int):
			raise TypeError
		self.year = year
		self.month = month
		self.day = day

	# 给Date对象加日期得到一个新的对象。写的毫无优雅可言，而且可能有BUG，有时间来优化。
	@staticmethod
	def plus(D, n):
		if not isinstance(n, int):
			raise TypeError
		if n < 0 or n > 31:
			raise('n要介于0和31之间')
		D.day = D.day + int
		# 闰年
		if D.month in set(1, 3, 5, 7, 8, 10, 12):
			if D.day >31:
				D.day = D.day - 31
				D.month = D.month +1
				if D.year//100 !=0 and D.year//4 == 0 or\
					D.year//100 == 0 and D.year//400 == 0:
					if D.month == 2 and D.day > 29:
						D.month = 3
						D.day = D.day - 29
				else:
					if D.month == 2 or and D.day > 28:
						D.month = 3
						D.day = D.day - 28
				if D.month = 13:
					D.month = 1
					D.year = D.year +1
		else:
			if D.day > 30:
				D.day = D.day - 30
				D.month = D.month +1

			
		