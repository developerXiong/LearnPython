
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
	name = str(name)
	datas = readFile()
	if len(datas) == 0:
		print 'Nothing to delete'
	else:
		removeDicts = []
		for dict in datas:
			for (k, v) in dict.items():
				if k == name:
					removeDicts.append(dict)
		if len(removeDicts) != 0:
			for item in removeDicts:
				datas.remove(item)
			writeFile(datas)
			print 'Delete %s successful'%name
		else:
			print 'The address is not exists.'

def update(name, phonenumber):
	pass

def query():
	datas = readFile()
	if len(datas) == 0:
		print 'Nothing in address.'
	else:
		print datas