

class ShortInputException(Exception):
	'''A user-defined exceptoin class.'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	s = raw_input('Enter something-->')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
	#Other work can continue as usual here 
except EOFError:
	print '\nWhy did you do an EOF on me?'
except ShortInputException,x:
	print 'ShortInputException: The input was of length %d,\
	was excepting at least %d'%(x.length, x.atleast)
else:
	print 'No excepting was raised.'