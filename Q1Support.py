import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P
import scr.FigureSupport as Fig

def print_payouts(sim_output, strategy_name):
    """
    :param sim_output: simulated cohort output
    :param strategy_name: name of type of coin used
    """

    # mean and confidence interval text of payouts
    Payout = Format.format_estimate_interval(
        estimate=sim_output.get_expected_payout(),
        interval=sim_output.get_payout_t_CI_(P.ALPHA),
        deci=2
    )

    # print payout statistics
    print(strategy_name)
    print('Estimate of mean payout (dollars) and {:.{prec}%} confidence interval:'.format(1-P.ALPHA, prec=0), Payout)

def print_comparative_outcomes(sim_output_fair, sim_output_unfair):
    """ prints expected and percentage increase in payout when unfair coin is used"""

    # increase in payout
    increase = Stat.DifferenceStatIndp(
        name='Difference in payout',
        x=sim_output_unfair.get_payouts(),
        y_ref=sim_output_fair.get_payouts()
    )
    # estimate and CI
    Estimate = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(P.ALPHA),
        deci=2
    )
    print('Average change in payout (dollars) and {:.{prec}%} confidence interval:'.format(1-P.ALPHA, prec=0), Estimate)

def draw_histogram(sim_output_fair, sim_output_unfair):

    # histograms of payouts
    set_of_payouts = [
        sim_output_fair.get_payouts(),
        sim_output_unfair.get_payouts()
    ]

    # graph histograms
    Fig.graph_histograms(
        data_sets=set_of_payouts,
        title='Histogram of payouts',
        x_label='Payouts',
        y_label='Counts',
        bin_width=50,
        legend=['Fair Coin', 'Unfair Coin'],
        transparency=0.6
    )