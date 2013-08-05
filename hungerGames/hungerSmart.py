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
        self.roundnumber = 0
        self.hunts = 0
        self.totalfights = 0
        self.huntprice = 6
        self.slackprice = 2

    # All the other functions are the same as with the non object oriented setting (but they
    # should be instance methods so don't forget to add 'self' as an extra first argument).

    def hunt_choices(self, round_number, current_food, current_reputation, m,
            player_reputations):
        self.reputation = current_reputation
        self.roundnumber = round_number
        self.food = current_food

        hunt_decisions = ['h' for x in player_reputations] # replace logic with your own

        slacks = 0
        if round_number > 1:
            for i in range(len(player_reputations)):
                otherhunt = player_reputations[i] * self.totalfights
                lastrounds = self.food < 3 * len(player_reputations) * self.slackprice
                lastplayer = len(player_reputations) == 1
                # if player_reputations[i] != current_reputation:
                if otherhunt == 0 or lastrounds or lastplayer or abs(otherhunt - self.hunts) > 3:
                # if otherhunt == 0 or lastrounds or lastplayer or otherhunt + 5 < self.hunts:
                    hunt_decisions[i] = 's'
                    slacks += 1

        # print('Slacks: {0} Hunts: {1} Total: {2}'.format(slacks, len(hunt_decisions) - slacks, self.totalfights))

        self.totalfights += len(player_reputations)
        self.hunts += len(hunt_decisions) - slacks

        return hunt_decisions

    def hunt_outcomes(self, food_earnings):
        pass # do nothing

    def round_end(self, award, m, number_hunters):
        pass # do nothing

    def __str__(self):
        return "Smart player (food: {0} reputation {1} hunts: {2} total: {3} total*rep: {4})".format(
                self.food, 
                self.reputation,
                self.hunts,
                self.totalfights,
                self.totalfights * self.reputation)
