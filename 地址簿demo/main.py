
import option


def main():
	while True:
		# 1.get input value
		input = raw_input('''Enter following:
			1. add
			2. delete
			3. update
			4. query
			5. quit
			and press the enter on your keyboard.\n''')
		# 2.check input type
		if input == '1':
			name = raw_input('Enter name:')
			phone = raw_input('Enter phonenumber:')
			option.add(name, phone)
		elif input == '2':
			name = raw_input('Enter name:')
			option.delete(name)
		elif input == '3':
			name = raw_input('Enter name:')
			phone = raw_input('Enter phonenumber:')
			option.update(name, phone)
		elif input == '4':
			# name = raw_input('Enter name:')
			option.query()
		elif input == '5':
			break
		else:
			print 'Please input right command.'
			continue

main()
			

