"""
A file which contains the simulations based on Charlotte Data.

Model: goodman_er_bayes
        Computed from the raw b_i samples by multiplying by population and then getting
        the proportion of the total pop (total pop=summed across all districts):
        The posterior mean for the district-level voting preference of
        black_voters for Vi is
        0.979
        The posterior mean for the district-level voting preference of
        non-black_voters for Vi is
        0.642
        95% equal-tailed Bayesian credible interval for district-level voting preference of
        black_voters for Vi is
        [0.92046375 0.99954472]
        95% equal-tailed Bayesian credible interval for district-level voting preference of
        non-black_voters for Vi is
        [0.61222822 0.67274433]

Model: goodman_er_bayes
        Computed from the raw b_i samples by multiplying by population and then getting
        the proportion of the total pop (total pop=summed across all districts):
        The posterior mean for the district-level voting preference of
        black_voters for Stephanie is
        0.019
        The posterior mean for the district-level voting preference of
        non-black_voters for Stephanie is
        0.348
        95% equal-tailed Bayesian credible interval for district-level voting preference of
        black_voters for Stephanie is
        [0.00049846 0.07039108]
        95% equal-tailed Bayesian credible interval for district-level voting preference of
        non-black_voters for Stephanie is
        [0.31990464 0.37540694]
"""
from structures.sim_params import SimParams
from structures.bloc import Bloc

# Charlotte Mayor 2023
# Candidates: Stephanie de Sarachaga-Bilbao, Vi Alexander Lyles
char_mayor_all_indifferent = SimParams("Charlotte Mayor All Indifferent",
                                       Bloc(name="Black Voters",
                                             size=0.352,
                                             candidates=["Vi Alexander Lyles"],
                                             cohesion={"Black Voters": 0.979, "Other Voters": 0.021},
                                             preference={"Black Voters": 2, "Other Voters": 2}),
                                        Bloc(name="Other Voters",
                                             size=0.648,
                                             candidates=["Stephanie de Sarachaga-Bilbao"],
                                             cohesion={"Black Voters": 0.652, "Other Voters": 0.348},
                                             preference={"Black Voters": 2, "Other Voters": 2}),
                                        num_seats=1,
                                        num_ballots=1000)
