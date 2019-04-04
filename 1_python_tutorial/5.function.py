def say_hello():
	print("hello chenyong")
def greetings(x='good morning'):
	print(x)
say_hello()
greetings()
greetings("cao ni")
a=greetings()

def create_a_list(x,y=2,z=3):
	return [x,y,z]
b=create_a_list(1)
c=create_a_list(3,3)
d=create_a_list(6,7,8)
print(b,'\n',c,'\n',d)

#*args是可变参数，args接收的是一个tuple，
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def traverse_args(*args):
	for arg in args:
		print(arg)

traverse_args(1,2,3)
traverse_args('a','b','v','d')
def traverse_kargs(**kwargs):
	#for i,j in kwargs.items():
	print(kwargs)
	for i,j in kwargs.items():
		print(i,j)
traverse_kargs(x=3,y=4,z=5)
traverse_kargs(fig='f',f2='r')
def foo(x,y,*args,**kwargs):
	print(x,y)
	print(args)
	print(kwargs)
foo(1,2,3,4,5,a=6,b='bar')
#有些情况下函数也可以当成一个变量使用
moves=['up','left','down','right']
coord=[0,0]
for move in moves:
	if move=='up':
		coord[1]+=1
		print(coord)
	elif move=='down':
		coord[1]-=1
		print(coord)
	elif move=='right':
		coord[0]+=1
		print(coord)
	elif move =='left':
		coord[0]-=1
		print(coord)
	else:
		pass
	print(coord)

def move_up(x):
	x[1]+=1
def move_down(x):
	x[1]-=1
def move_left(x):
	x[0]-=1
def move_right(x):
	x[0]+=1
actions={'up':move_up,'down':move_down,'left':move_left,'right':move_right}
coord=[0,0]
for move in moves:
	actions[move](coord)
	print('函数版本:\n',coord)

def get_val_at_pos_1(x):
	return x[1]
heros=[('superman',99),('bataman',100),('jker',95)]
#d=sorted(a.iteritems(),key=itemgetter(1)) 字典
sorted_pairs0=sorted(heros,key=get_val_at_pos_1)
sorted_pairs1=sorted(heros,key=lambda x:	x[1])
print(sorted_pairs0)
print(sorted_pairs1)


som_ops=lambda x,y: x+y+x*y+x**y
result=som_ops(2,3)
print(result)