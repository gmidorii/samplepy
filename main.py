# coding:utf-8

import sys
import glob
from time import localtime

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
	#try:
		#arg = sys.argv[1:]
		#print(arg)
	#except ValueError:
		#print("Error")
	print("\n")

	# file
	files = glob.glob("sample/*.txt")
	print(files)
	for file_name in files:
		print("--------- " + file_name + " -----------")

		with open(file_name) as f:
			for line in f:
				print(line.rstrip())
	print("\n")

	# time
	now = localtime()
	hour = now.tm_hour
	print(hour)
	print("\n")

	# triple quote
	REFRAIN = '''
	{} bottles
	{} bottoles of beer
	{} hogehoge
	'''
	beer = 5
	while beer > 1:
		print(REFRAIN.format(beer, beer, beer - 1))
		beer -= 1

	# class
	class BankAccount:
		# constructor
		def __init__(self, val):
			self.val = val

		def output(self):
			print(self.val)

	bank = BankAccount(20)
	bank.output()


	# test
	return 4;

if __name__ == "__main__":
	main()

