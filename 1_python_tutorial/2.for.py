#for 2019.4.4 chenyong in chengdu
a=['This','is','a','list','!']
for i in a:
	print(i)
for x in a:
	print(x)
for key in a:
	print(key)
for i in range(10):
	print(i)
i=0
names=['Rick','Chen','Yong']
for element in names:
	print(element)
	print(i,names[i])
	i+=1

print(list(enumerate(names)))
for i,name in enumerate(names):
	print(i,name)

for i in range(len(names)):
	print(names[i])

wusuowei=['I',"don't",'give',"shit"]
hexie=True
for x in wusuowei:
	if x=="shigt":
		print('what the fuck')
		hexie=False
		break
	#else:
	#	print('hehe')
#if hexie:
#	print("Ha")
else:
	print("caodandeshehui")