#生成器，边计算边生成。迭代，会记住迭代的对象。

def countdown(x):
	while x>=0:
		yield x
		x-=1
for i in countdown(10):
	print(i)

def fibonaci(n):
	a=0
	b=1
	while b<n:
		yield b
		a,b=b,a+b
	return 'no more'
for x in fibonaci(100):
	print(x)
a=fibonaci(3)
print(a)
#fibonaci(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

