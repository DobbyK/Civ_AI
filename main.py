import time, os
startup = True
gameon = True

def newgame():
	try:
		print('Loading Default Settings...')
		os.system('python default.py')
		print('Done')
		startup == None
		return
	except:
		print('Error')
		return

def start():
	try:
		os.system('cat text/openning.txt')
		ch = input('>> ')
		global c
		c = int(ch)
		return
	except:
		print('Error')
		start()

while gameon == True:
	if startup == True:
		try:
			start()
			print(c)
			startup = False
		except:
			print('Error')
	if startup == False:
		try:
			if c == 1:
				newgame()
			else:
				print('Error')
		except:
			print('Error')
			return
	if startup == None:
		try:
			os.system('cat text/actions.txt')

while gameon == False:
	print('Are you sure that you want to exit?')
	ch = input('>> ')
	if ch == 'y':
		gameon == True
	elif ch == 'n':
		quit()
	else:
		print('Error')
