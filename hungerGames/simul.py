import sys
import importlib
import random
 
playercount = 100
roundnumber = 1
players = []
mrandom = 0;

def run_tests(script_name):
	global playercount

	user_module = importlib.import_module(script_name[:-3])
	for i in range(playercount):
		players.append(user_module.Player())
		players[i].reputation = 0
		players[i].hunts = 0
		players[i].slacks = 0
		players[i].food = 300 * playercount
	
	while playercount > 1:
		mrandom = random.randint(1,playercount * (playercount-1))
		totalhunts = 0
		for i in range(playercount):
			totalhunts += test_hunt_choices(players[i], i)
	 
		test_hunt_outcomes()
		
		totalfood = 0
		for i in range(playercount):
			test_round_end(players[i], 
					2 * (playercount-1) if totalhunts > mrandom else 0,
					sum(players[0].outcome),
					players[i].cost,
					mrandom,
					totalhunts)
			totalfood += players[i].food

		print('Total food:', totalfood)
		
		i = 0
		maxplayer = players[0]
		while i < playercount:
			if players[i].food > maxplayer.food:
				maxplayer = players[i]

			if players[i].food <= 0:
				print('Removing player with slacerness of', players[i].randomcount)
				del(players[i])
				playercount-=1
			else:
				i+=1

		print('Max player food and slackerness:', maxplayer.food, maxplayer.randomcount, maxplayer.reputation)

	"""
	print(players[0].outcome)
	print(players[0].cost)
	print(sum(players[0].outcome) - players[0].cost)
	print(players[0].reputation)
	print(totalhunts)
	"""
	print('Winner''s food and slackerness:', players[0].food, players[0].randomcount)
 
def test_hunt_choices(player, position):
	player.decisions = player.hunt_choices(roundnumber, player.food, player.reputation, mrandom,
			[r.reputation for r in players if player != r])
	player.decisions.insert(position, '')
	slacks = len( filter(lambda d: d == 's', player.decisions) ) 
	hunts = len( filter(lambda d: d == 'h', player.decisions) )
	player.slacks += slacks
	player.hunts += hunts
	player.reputation = float(player.hunts) / (player.hunts + player.slacks) 
	player.cost = 2*slacks + 6*hunts 
	return hunts
 
def test_hunt_outcomes():
	for p1id in range(playercount):
		p1 = players[p1id]
		p1.outcome = [0] * playercount
		for p2id in range(playercount):
			if p2id == p1id:
				continue

			p2 = players[p2id]
			if not hasattr(p2, 'outcome'):
				p2.outcome = [0] * playercount
			p1v = 0
			p2v = 0
			if p1.decisions[p2id] == 'h':
				if p2.decisions[p1id] == 's':
					p1v = 3; p2v = 3
				else:
					p1v = 6; p2v = 6
			else:
				if p2.decisions[p1id] == 's':
					p1v = 0; p2v = 0
				else:
					p1v = 3; p2v = 3
			p1.outcome[p2id] = p1v
			p2.outcome[p1id] = p2v
 
def test_round_end(player, award, gain, cost, m, hunts):
	player.round_end(award, m, hunts)
	player.food += award + gain - cost
 
if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print ("\nYou must include the filename that contains your code "
               "as the only argument to this script.\n\n"
               "Example: python tester.py filename_of_your_script.py\n")
        raise
    else:
        run_tests(filename)
