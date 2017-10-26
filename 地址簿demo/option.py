
import os
import cPickle as p
#import pickle as p

#the name of the file where we will store the object
filename = 'address.data'

def readFile():
	#Read the file
	if not os.path.exists(filename):
		return []
	f = file(filename)
	datas = p.load(f)
	f.close()
	return datas

def writeFile(datas):
	#Write to file
	f = file(filename, 'w')
	p.dump(datas, f)
	f.close()
	
def add(name, phonenumber):
	datas = readFile()

	if len(datas) == 0:
		datas = [{name: phonenumber}]
		writeFile(datas)
	else:
		datas.append({name: phonenumber})
		writeFile(datas)
	result = readFile()
	if len(result[-1][name]) != 0:
		print 'Add a user:%s successful'%name

def delete(name):
	datas = readFile()
	if len(datas) == 0:
		print 'Nothing to delete'
	else:
		for dict in datas:
			if len(dict[name]) != 0:
				datas.remove(dict)
			else:
				print 'The name is not exists.'
		writeFile(datas)

def update(name, phonenumber):
	pass

def query():
	datas = readFile()
	if len(datas) == 0:
		print 'Nothing in address.'
	else:
		print datas