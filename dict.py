
ab = {'Swaroop': 'swaroopch@byteofpython.info',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}

print 'Swaroop\'s address is', ab['Swaroop']

ab['Gudio'] = 'gudio@python.org'

del ab['Spammer']

print '\nThere are %d contacts in the  address-book\n'%len(ab)
for name,address in ab.items():
	print 'Contacts %s at %s'%(name, address)
if 'Gudio' in ab:
	print '\nGudio\'s address is ',ab['Gudio']