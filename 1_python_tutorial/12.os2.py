import os,shutil
filepath0='data/bat/IMG_000001.jpg'
filepath1='data/bat/IMG_000002.jpg'

os.system('mv {} {}'.format(filepath0,filepath1))
os.rename(filepath0,filepath1)

dirname='data_samples'
os.system('mkdir -p {}'.format(dirname))
if not os.path.exists(dirname):
	os.mkdir(dirname)

os.system('cp {} {}'.format(filepath1,dirname))
