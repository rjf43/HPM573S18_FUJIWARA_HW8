import Model as Model
import Parameters as P
import Q1Support as Support

# determine the steady-state

# create cohort for fair coin
FairCoin = Model.Simulation(
    id=1,
    number_games=P.SIM_NUMBER_GAMES,
    heads_prob=P.HEADS_PROB_FAIR
)
# simulate the cohort with fair coin
Fair_simulation = FairCoin.simulate(P.NUMBER_FLIPS)

# create cohort for unfair coin
UnfairCoin = Model.Simulation(
    id=2,
    number_games=P.SIM_NUMBER_GAMES,
    heads_prob=P.HEADS_PROB_UNFAIR
)
# simulate the cohort with unfair coin
Unfair_simulation = UnfairCoin.simulate(P.NUMBER_FLIPS)

# Print parameters of each cohort
Support.print_payouts(Fair_simulation,'Fair coin')
Support.print_payouts(Unfair_simulation,'Unfair coin')

# Print difference in payouts
Support.print_comparative_outcomes(Fair_simulation, Unfair_simulation)

Support.draw_histogram(Fair_simulation, Unfair_simulation)