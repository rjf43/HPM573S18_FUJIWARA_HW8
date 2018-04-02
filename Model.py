from enum import Enum
import numpy as np
import scr.StatisticalClasses as Stat

class CoinFlip(Enum):
    """ outcome of each coin flip"""
    HEADS = 1
    TAILS = 0

class Game:
    def __init__(self, id, heads_prob):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)

        self.heads_prob = heads_prob
        self._flipList = []

    def simulate(self, numberFlips):
        """ simulate a game of numberFlips coin flips """
        for i in range(numberFlips):
            toss = self._rnd.binomial(1, self.heads_prob)
            if toss == 1:
                toss = CoinFlip.HEADS # convert binary output to H
            else:
                toss = CoinFlip.TAILS
            self._flipList.append(toss) # convert binary output to T

    def get_payout(self):
        """ determine how many times desired series of coin flip arises
        and calculate payout"""
        payout = -250
        n = 0 # number of times that [Tails, Tails, Heads] occurs
        for i in range(len(self._flipList)-2):
            if self._flipList[i] == CoinFlip.TAILS and self._flipList[i+1] == CoinFlip.TAILS and self._flipList[i+2] == CoinFlip.HEADS:
                n +=1
        payout += 100*n
        return payout

class Simulation:
    def __init__(self, id, number_games, heads_prob):
        """

        :param id: cohort ID
        :param number_games: number of games, each of which consist of number of coin flips according to numberFlips
        :param heads_prob: probability of heads on coin toss
        """

        self._games = []
        self._payouts = []

        # simulate multiple games and populate lists
        for i in range(number_games):
            game = Game(id*number_games+i, heads_prob)
            self._games.append(game)

    def simulate(self, numberFlips):
        for game in self._games:
            game.simulate(numberFlips) # run each of the games included in the games list

            payout = game.get_payout() # calculate payout for each game in the list
            self._payouts.append(payout) # add payout for each game to payouts list

        return SimOutcomes(self)

    def get_payouts(self):
        return self._payouts

    def get_losses(self):
        losses = []
        for i in range(len(self._payouts)):
            if self._payouts[i] < 0:
                losses.append(1)
            else:
                losses.append(0)
        return losses

class SimOutcomes:
    def __init__(self, simulated_cohort):
        self._simulated_cohort = simulated_cohort

        self._sumstat_expectedvalue = Stat.SummaryStat('expected value', self._simulated_cohort.get_payouts())
        self._sumstat_losses = Stat.SummaryStat('losses', self._simulated_cohort.get_losses())

    def get_expected_payout(self):
        return self._sumstat_expectedvalue.get_mean()

    def get_payout_t_CI_(self, alpha):
        return self._sumstat_expectedvalue.get_t_CI(alpha)

    def get_probability_of_loss(self):
    # calculate the probability of losing money in this game
        return self._sumstat_losses.get_mean()

    def get_probability_t_CI(self, alpha):
        return self._sumstat_losses.get_t_CI(alpha)

    def get_payouts(self):
        return self._simulated_cohort.get_payouts()

class MultiSim:
    """ simulates multiple simulations of the game for transition state estimates """
    def __init__(self, ids, number_games, heads_prob):
        """

        :param ids: list of ids
        :param number_games: list of number of games within each simulation
        :param heads_prob: probability of heads in each game
        """

        self._ids = ids
        self._number_games = number_games
        self._heads_prob = heads_prob

        self._payouts = []
        self._mean_payouts = []
        self._sumStat_meanPayouts = None

    def simulate(self, numberFlips):
        for i in range(len(self._ids)):
            # create the game
            game = Simulation(self._ids[i], self._number_games[i], self._heads_prob[i])
            # simulate the game
            game_outcome = game.simulate(numberFlips)
            # store payout for each game
            self._payouts.append(game.get_payouts())
            # store mean payout for games of set i
            self._mean_payouts.append(game_outcome.get_expected_payout())

        # summary statistics for means
        self._sumStat_meanPayouts = Stat.SummaryStat('Mean payouts', self._mean_payouts)

    def get_all_mean_payouts(self):
        return self._mean_payouts

    def get_overall_mean_payout(self):
        return self._sumStat_meanPayouts.get_mean()

    def get_PI_mean_payouts(self, alpha):
        return self._sumStat_meanPayouts.get_PI(alpha)









