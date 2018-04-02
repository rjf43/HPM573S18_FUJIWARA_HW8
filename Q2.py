import Model as Model
import Parameters as P
import Q2Support as Support

# create multi-cohort for fair coin
FairCoin = Model.MultiSim(
    ids=range(P.NUMBER_SIM_COHORTS),
    number_games=[P.REAL_NUMBER_GAMES]*P.NUMBER_SIM_COHORTS,
    heads_prob=[P.HEADS_PROB_FAIR]*P.NUMBER_SIM_COHORTS
)
# simulate multi-cohort
FairCoin.simulate(P.NUMBER_FLIPS)

# create multi-cohort for unfair coin
UnfairCoin = Model.MultiSim(
    ids=range(P.NUMBER_SIM_COHORTS,2*P.NUMBER_SIM_COHORTS),
    number_games=[P.REAL_NUMBER_GAMES]*P.NUMBER_SIM_COHORTS,
    heads_prob=[P.HEADS_PROB_UNFAIR]*P.NUMBER_SIM_COHORTS
)
# simulate multi-cohort
UnfairCoin.simulate(P.NUMBER_FLIPS)

# print parameters for each cohort
Support.print_payouts(FairCoin, 'Fair coin')
Support.print_payouts(UnfairCoin, 'Unfair coin')

# print comparative statistics
Support.print_comparative_outcomes(FairCoin, UnfairCoin)