import random

# Optional format of the constructor for the OOP approach
class Player:
    def __init__(self):
        """
        Optional __init__ method is run once when your Player object is created before the
        game starts

        You can add other internal (instance) variables here at your discretion.

        You don't need to define food or reputation as instance variables, since the host
        will never use them. The host will keep track of your food and reputation for you
        as well, and return it through hunt_choices.
        """
        self.food = 0
        self.reputation = 0
	self.randomcount = random.randint(0,100)

    # All the other functions are the same as with the non object oriented setting (but they
    # should be instance methods so don't forget to add 'self' as an extra first argument).

    def hunt_choices(self, round_number, current_food, current_reputation, m,
            player_reputations):
        hunt_decisions = ['h' for x in player_reputations] # replace logic with your own

	for i in range(min(len(hunt_decisions), self.randomcount)):
		while hunt_decisions[i] == 's':
			i = (i+1) % len(hunt_decisions)
		hunt_decisions[i] = 's'
        return hunt_decisions

    def hunt_outcomes(self, food_earnings):
        pass # do nothing

    def round_end(self, award, m, number_hunters):
        pass # do nothing
