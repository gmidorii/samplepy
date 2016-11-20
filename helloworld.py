# coding:utf-8

def greet(name):
	print(name)

def main():
	print("Hello World")
	message = "Oi! {}".format("test")
	print(message)

	# input
	#name = raw_input('What is your name?\n')
	#print('Hi {}'.format(name))

	# for loop (plus iterator)
	friends = ['john', 'Bob', 'Herey']
	for it, name in enumerate(friends):
		print("it {} : name{}".format(it, name))

	# function
	greet("Taga")

if __name__ == "__main__":
	main()

