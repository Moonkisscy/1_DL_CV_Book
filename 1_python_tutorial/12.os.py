import os
label_map={'cat':1,'dog':0,'bat':2}
with open('data.txt','w') as f:
# os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下
	for root,dirs,files in os.walk('data'):
		for filename in files:
			filepath=os.sep.join([root,filename])
			dirname=root.split(os.sep)[-1]
			labe=label_map[dirname]
			line='{},{}\n'.format(filepath,label)
			f.write(line)

