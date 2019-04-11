import pickle
lines=['I lIKE ','i wont ','i just']
with open('line.pkl','wb') as f:#序列化保存文件
	pickle.dump(lines,f)
with open('line.pkl','rb') as f:
	lines_back=pickle.load(f)
print(lines_back)

#异常
#for fielpath in filelist:
try:
	fh=open('age_name2.txt','w')
	fh.write('测试')
	print('{} is processed!'.format(fh))
except IOError:
	print('error,没有找到这个文件')
else:
	print('写入成功')
	fh.close()
try:
	fh=open('age_name2.txt','w')
	#fh.readlines
	print('{} is processed!'.format(fh))
except IOError:
	print('error,没有找到这个文件')
else:
	print('写入成功')
	fh.close()
