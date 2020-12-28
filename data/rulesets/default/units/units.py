# This is the terrian rules for the default ruleset, this is how its setup:
# class: unit type
# 	{unitname} = [{Acorym}, {A}, {D}, {HP}, {MP}, {TECH}, {PRODUCTION}]
import random, time

def battle(ah, dh, aa, da, ad, dd, am):
	alive = True
	while alive == True:
		if am < 1:
			alive = False
			print('Attacker does not have enough mp!')
			break
		x = random.randint(1, 6)
		x = x + aa - dd
		dh = dh - x
		time.sleep(1)
		if dh < 0:
			dh = 0
		print('Attacker does ' + str(x) + ' damage DH:' + str(dh) + ' AH:' + str(ah))
		if dh < 1:
			time.sleep(1)
			print('Attacker Wins!' + ' AH:' + str(ah))
			alive == False
			break
		x = random.randint(1, 6)
		x = x + da - ad
		ah = ah - x
		time.sleep(1)
		if ah < 0:
			ah = 0
		print('Defender does ' + str(x) + ' damage DH:' + str(dh) + ' AH:' + str(ah))
		if ah < 1:
			time.sleep(1)
			print('Defender Wins!' + ' DH:' + str(dh))
			alive == False
			break

class melee:
	warrior = ['WR', 1, 1, 10, 2, 'NONE', 10]
	settler = ['ST', 0, 1, 20, 2, 'NONE', 40]
	worker = ['WK', 0, 1, 10, 2, 'POTTERY', 25]

class ranged:
	slinger = ['SL', 1, 1, 10, 2, 'NONE', 20]
	archer = ['AR', 3, 2, 10, 2, 'ARCHERY', 30]

battle(melee.warrior[3], melee.worker[3], melee.warrior[1], melee.worker[1], melee.warrior[2], melee.worker[2], melee.warrior[4])
