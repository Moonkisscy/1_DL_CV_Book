from multiprocessing import Process
def process_data(filelist):
	for fielpath in filelist:
		print('Processing {} ...'.format(fielpath))
if __name__ =='__main__':
	#如果是在windows下，需要加上freeze_support()函数
	#freeze_support()
	#full_list包含了要处理的全部文件列表
	...
	n_total=len(full_list)
	n_processes=32
	#求每段子列表的平均长度
	length=float(n_total)/float(n_processes)
	#计算下标，尽可能均匀地划分输入文件列表
	indices=[int(round(i*length)) for i in range(n_processes)]
	sublists=[full_list[indices[i]:indices[i+1]] for i in range(n_processes)]
	process=[Process(target=process_data, args=(x,)) for x in sublists]

	for p in process:
		p.start()
	for p in process:
		p.join()

