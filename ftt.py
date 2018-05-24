# coding:utf-8
# python3

print('from ftt.py')

# 定义一个表示时间的类
class Time(object):
	# 默认hours,minutes,seconds均在合理数值范围内
	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def _alltime(self):
		return self.seconds + self.minutes*60 + self.hours*60*60

	def hours(self):
		return self.hours

	def minutes(self):
		return self.minutes

	def seconds(self):
		return self.seconds

	def __add__(self, T):
		seconds = self.seconds + T.seconds
		if seconds > 60:
			seconds = seconds-60
			minutes = self.minutes + T.minutes +1
		else:
			minutes = self.minutes + T.minutes
		if minutes >60:
			minutes = minutes -60
			hours = self.hours + T.hours +1
		else:
			hours = self.hours + T.hours
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def __sub__(self, T):
		allseconds = self._alltime()
		allseconds2 = T._alltime()
		if allseconds < allseconds2:
			raise Exception('错误')
		diff = allseconds - allseconds2
		self.hours = diff//3600
		self.minutes = diff%3600//60
		self.seconds = diff%3600%60

	def __eq__(self, T):
		if self._alltime() == T._alltime():
			return True
		return False

	def __lt__(self, T):
		if self._alltime() < T._alltime():
			return True
		return False


