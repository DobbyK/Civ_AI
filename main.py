import time, os

def start():
	try:
		os.system('cat text/open.txt')
		c = input('>> ')
		c = int(c)
	except:

		print('That is not a number, or has letters')
		start()

	if c == 1:
		newgame()
	else:
		print('Error')

start()
