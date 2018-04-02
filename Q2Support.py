import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P
import scr.FigureSupport as Fig

def print_payouts(multi_cohort, strategy_name):

    # mean and prediction intervals of payouts
    Payout = Format.format_estimate_interval(
        estimate=multi_cohort.get_overall_mean_payout(),
        interval=multi_cohort.get_PI_mean_payouts(P.ALPHA),
        deci=2
    )

    # print payout statistics
    print(strategy_name)
    print('Estimate of mean payout (dollars) and {:.{prec}%} PI:'.format(1-P.ALPHA, prec=0), Payout)

def print_comparative_outcomes(sim_output_fair, sim_output_unfair):

    # increase in payout
    increase = Stat.DifferenceStatIndp(
        name='Difference in payout',
        x=sim_output_unfair.get_all_mean_payouts(),
        y_ref=sim_output_fair.get_all_mean_payouts()
    )
    # estimate and CI
    estimate = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(P.ALPHA),
        deci=2
    )
    print('Expected difference in payout (dollars) and {:.{prec}%} PI:'.format(1-P.ALPHA, prec=0), estimate)

