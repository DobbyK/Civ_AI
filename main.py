import time, os
global ruleset
ruleset = 'default'
def startgame(file):
	try:
		os.system('python ' + file)
		print('Loaded Game, Starting...')
	except:
		print('Error')
		return
def newgame():
	if ruleset == 'default':
		print('Would you like to load default settings?(y/n)')
		c = input('>> ')
		if c == 'y' or c == 'Y':
			print('What do you want to call it?')
			sf = input('>> ')
			os.system('cp saves/default.py' + ' saves/' + sf + '.py')
			startgame('saves/' + sf + '.py')
		if c == 'n' or c == 'N':
			print('What settings would you like to load?')
			ld = input('>> ')
			print('What would like to call the game?')
			sf = input('>> ')
			os.system('cp saves/' + ld + '.py ' + 'saves/' + sf + '.py')
			startgame()
		else:
			print('Error')
			newgame()
	else:
		print('Error')
		newgame()
def start():
	try:
		os.system('cat text/openning.txt')
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
