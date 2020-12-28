import time, os
startup = True
gameon = True
def game():
	try:
		os.system('cat text/actions.txt')
		c = input('>> ')
		c = int(c)

def newgame():
	try:
		print('Loading Default Settings...')
		os.system('python saves/default.py')
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
	elif startup == False:
		try:
			if c == 1:
				newgame()
			else:
				print('Error')
		except:
			print('Error')
	elif startup == None:
		try:
			game()
		except:
			print('Error')
	else:
		break

while gameon == False:
	print('Are you sure that you want to exit?')
	ch = input('>> ')
	if ch == 'y':
		gameon == True
	elif ch == 'n':
		quit()
	else:
		print('Error')
