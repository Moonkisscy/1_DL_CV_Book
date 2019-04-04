pets=['dog','cat','droid','fly','fish']
for pet in pets:
	if pet=='dog':
		food='steak'
	elif pet=='cat':
		food='milk'
	elif pet=='droid':
		food='oil'
	elif pet=='fly':
		food='shit'
	else:
		pass
	print(food)
#因为空格debug半天

food_for_pet={'dog':'steak','cat':'milk','droid':'oil','fly':'shit'}
for pet in pets:
	food=food_for_pet[pet] if pet in food_for_pet else None
	print(food)

#3.if表达中的小技巧
x=0
if -1<x<1:
	print('The absoult value of x is <1')
if x in ['pinao','violin']:
	print('it is a instrument')
else:
	print('it is not a instrument')

a=True
if a:
	print('a is True')
if 'sky':
	print('birds')
if '':
	print('nothing')
if {}:
	print('Nothing')
if 'elif':
	print('nothing')
if {}:
	print('Nothing')