# coding:utf-8

import sys

def greet(name):
	print(name)

def main():
	print("Hello World")
	message = "Oi! {}".format("test")
	print(message)
	print("\n")

	# input
	#name = raw_input('What is your name?\n')
	#print('Hi {}'.format(name))

	# for loop (plus iterator)
	friends = ['john', 'Bob', 'Herey']
	for it, name in enumerate(friends):
		print("it {} : name{}".format(it, name))
	print("\n")

	# function
	greet("Taga")
	print("\n")

	# string join
	print('JOIN' + ' string')
	print("\n")

	# array + loop
	array = {'apple': 1, 'banana': 3}
	sum_array = sum(array[key] for key in array)
	print(sum_array)
	print("\n")

	# arg + try-except
	try:
		#arg = sys.argv[1:]
		#print(arg)
	except ValueError:
		print("Error")

if __name__ == "__main__":
	main()

