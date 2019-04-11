with open('name_age.txt','r') as f:
	lines=f.readlines()
	print(lines)
	for line in lines:
		name,age=line.rstrip().split(',')#Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格)
		print('{} is {} years old.'.format(name,age))#Python split() 通过指定分隔符对字符串进行切片，
		print(line.rstrip().split(','))
		print(line.rstrip())
		print(line.split(','))
		#print(line.split(',').rstrip())
with open('name_age.txt','r') as fread, open('age_name.txt','w') as fwrite:
	line=fread.readlines()
	#while line:
	for line in lines:
		name,age =line.rstrip().split(',')
		fwrite.write('{},{}\n'.format(age,name))
		line=fread.readline()
		print(line)