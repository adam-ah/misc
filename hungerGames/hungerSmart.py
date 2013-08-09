import random

# You are reading a comment in code. You are doing it wrong...
class Player:
    def __init__(self):
        self.food = 0 
        self.reputation = 0
        self.roundnumber = 0
        self.hunts = 0 # My total hunts so far.
        self.totalfights = 0 # Hunt != Total decisions so far.
        self.huntprice = 6
        self.slackprice = 2
        self.players = 0 # Other players.

    def hunt_choices(self, round_number, current_food, current_reputation, m, player_reputations):
        self.reputation = current_reputation
        self.roundnumber = round_number
        self.food = current_food
        self.players = len(player_reputations)

        hunt_decisions = ['h']  * self.players

        slacks = 0
        if round_number > 1: # Only slack after first round.
            for i in range(self.players):
                otherhunt = int(round(player_reputations[i] * self.totalfights))
                lastrounds = self.food < 3 * self.players * self.slackprice
                lastplayer = self.players == 1
                randomplayer = otherhunt != self.hunts and abs(otherhunt * 2 - self.totalfights) < 2
                # Be a slacker if: the other player never hunted; We are approaching the end of game;
                # the other player is playing a very different strategy.
                if otherhunt == 0 or lastrounds or lastplayer or abs(otherhunt - self.hunts) > 3:
                    hunt_decisions[i] = 's'
                    slacks += 1

        self.totalfights += self.players
        self.hunts += self.players - slacks

        return hunt_decisions

    def hunt_outcomes(self, food_earnings):
        pass # Meh.

    def round_end(self, award, m, number_hunters):
        pass # Meh.

    def __str__(self):
        return "Smart player (food: {0} reputation {1} hunts: {2} total: {3} total*rep: {4})".format(
                self.food, 
                self.reputation,
                self.hunts,
                self.totalfights,
                self.totalfights * self.reputation)
