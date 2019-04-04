class A:
	""""Class A"""
	def __init__(self,x,y,name):
		self.x=x
		self.y=y
		self._name=name
	def introduce(self):
		print(self._name)
	def greeting(self):
		print("what's up")
	def __12norm(self):
		return self.x**2+self.y**2
	def cal_12norm(self):
		return self.__12norm()
a= A(11,11,'leonardo')
print(A.__doc__)
a.introduce()
a.greeting()
print(a._name)
print(a.cal_12norm)
print(a._A__12norm())
#print(a.__12norm())

class B(A):
	""""CLASS B 继承"""
	def greeting(self):
		print("how's going")
b=B(12,12,'FA')
b.introduce()
b.greeting()
print(b._name)
print(b._A__12norm)

