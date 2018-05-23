#-*- coding:utf-8 -*-

class Rational :
	@staticmethod
	def _gcd(m,n):
		if n == 0:
			m,n = n,m
		while m !=0:
			m,n = n% m ,m
		return n 

	def __init__(self,num,den=1):
		if not isinstance(num,int) or not isinstance(den,int):
			raise TypeError
		if den == 0:
			raise ZeroDivisionError
		sign = 1
		if num < 0:
			num,sign = -num,-sign
		if den < 0:
			den, sign = -den, -sign
		g = Rational._gcd(num,den)
		self._num = sign * (num/g)
		self._den = den/g