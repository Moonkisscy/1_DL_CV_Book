a=map(lambda x: x**2, [1,2,3,4])
print(a)
map(lambda x, y:x+y,[1,2,3],[5,6,7])
#reduce(lambda x,y:x+y,[1,2,3,4])
#filter，根据条件对可遍历结构进行筛选。
#filter(lambda,x: x%2,[1,2,3,4,5])

#列表生成
b=[x**2 for x in [1,2,3,4]]
#zib()函数按顺序同时输出两个列表对应位置的元素对
c=[sum(x) for x in zip([1,2,3],[5,6,7])]
d=[x for x in [1,2,3,4,5,6] if x%3]
print(b,c,d)

iter_odd=(x for x in [1,2,3,4,5] if x%2)
print(type(iter_odd))
square_dict={x: x**2 for x in range(5)}
print(square_dict)

a='I like a {} chasing {}'

print(a.format('dog','cars'))

b='I prefer {1} {0} to {2} {0}'
print(b.format('food','chinese','american'))

for i in [1 ,19,256]:
	print('The index is {:0>8f}'.format(i))
for x in ['*','****','******']:
	progress_bar='{:->10}'.format(x)
	print(progress_bar)
for x in [0.0001,1e17,3e-18]:
	print('{:.1f}'.format(x),'\n')
for x in [0.0001,1e17,3e-18]:
	print('{:.1e}'.format(x),'\n')
for x in [0.0001,1e17,3e-18]:
	print('{:g}'.format(x))

tmpleate='{name} is {age} years old'
print(tmpleate.format(name=3,age=3))


#upload github test
#关闭git客户端测试