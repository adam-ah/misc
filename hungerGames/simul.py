import sys
import importlib
import random
 
playercount = 100
roundnumber = 1
players = []
mrandom = 0;
smartcount = 1

def run_tests(script_name, script_name2):
    global playercount
    global roundnumber

    user_module = importlib.import_module(script_name[:-3])
    user_module2 = importlib.import_module(script_name2[:-3])

    for i in range(playercount):
        player = user_module.Player()
        if i >= playercount - smartcount:
            player = user_module2.Player()
        players.append(player)
        players[i].reputationS = 0
        players[i].nextreputationS = 0
        players[i].huntsS = 0
        players[i].slacksS = 0
        players[i].foodS = 300 * playercount

    while playercount > 1:
        mrandom = random.randint(1,playercount * (playercount-1))
        totalhunts = 0
        for i in range(playercount):
            totalhunts += test_hunt_choices(players[i], i, roundnumber)
     
        test_hunt_outcomes()
        
        totalfood = 0
        for i in range(playercount):
            players[i].reputationS = players[i].nextreputationS
            test_round_end(players[i], 
                    2 * (playercount-1) if totalhunts > mrandom else 0,
                    sum(players[i].outcome),
                    players[i].cost,
                    mrandom,
                    totalhunts)
            totalfood += players[i].foodS

        i = 0
        maxplayer = players[0]
        while i < playercount:
            if players[i].foodS > maxplayer.foodS:
                maxplayer = players[i]

            if players[i].foodS <= 0:
                print('Removing ' + str(players[i]))

                del(players[i])
                playercount-=1
            else:
                i+=1

        print('Round: {0} Players: {1} Total food: {2} Top player: {3} '.format(roundnumber, len(players), totalfood, str(maxplayer)))
        roundnumber += 1

    """
    print(players[0].outcome)
    print(players[0].cost)
    print(sum(players[0].outcome) - players[0].cost)
    print(players[0].reputation)
    print(totalhunts)
    """
    if len(players) != 0:
        print('Winner\'s: ' + str(players[0]))
    else:
        print('No winner, draw.')
 
def test_hunt_choices(player, position, roundnumber):
    player.decisions = player.hunt_choices(roundnumber, player.foodS, player.reputationS, mrandom,
            [r.reputationS for r in players if player != r])
    player.decisions.insert(position, '')
    slacks = len( filter(lambda d: d == 's', player.decisions) ) 
    hunts = len( filter(lambda d: d == 'h', player.decisions) )
    player.slacksS += slacks
    player.huntsS += hunts
    player.nextreputationS = float(player.huntsS) / (player.huntsS + player.slacksS) 
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
    player.foodS += award + gain - cost
 
if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        filename2 = sys.argv[2]
    except IndexError:
        print ("\nYou must include the filename that contains your code "
               "as the only argument to this script.\n\n"
               "Example: python tester.py filename_of_your_script.py\n")
        raise
    else:
        run_tests(filename, filename2)
