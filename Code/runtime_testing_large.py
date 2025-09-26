from votekit import PreferenceInterval
from votekit.ballot_generator import name_BradleyTerry
from votekit.elections import IRV
from time import monotonic_ns
from bloc import Bloc
from votekit.cleaning import clean_ranked_profile

# This code is meant to examine the runtime of a BT ballot generator using Marcov Chain Monte Carlo
# This setting is required when running an election with more than 12 candidates
# I will be selecting random numbers for everything
# I will be using 8 blocs and 23 candidates for these tests

## Results
# When running with 53k ballots, generation took several minutes, then my program crashed
# I am decreasing the number of ballots to 10k
# 

# My reference for cohesion params
# 1 is moderate left
# 2 is moderate right
# 3 is moderate left w/ specific focus
# 4 is moderate right w/ specific focus
# 5 is far left
# 6 is far right
# 7 is centrist w/ niche issue
# 8 is a cult

# Start timing the runtime of the program
start = monotonic_ns()

## Create parameters for ballot generation
# I will first be creating preference profiles for the different blocs
# To save time, all blocs will have the same preferences
# In a real version, we'd need to create one of these for each bloc
# Note that the intervals don't need to sum to one, VoteKit will normalize them
pref_intervals = {
"Bloc 1": PreferenceInterval({"1":0.8, "9":0.5, "10":0.3, "11":0.2, "12":0.1}), 
"Bloc 2": PreferenceInterval({"2":0.9, "13":0.5, "14":0.3, "15":0.3, "16": 0.1}),
"Bloc 3": PreferenceInterval({"3":0.7, "17":0.6, "18":0.3}),
"Bloc 4": PreferenceInterval({"4":0.4, "19":0.4, "20":0.1}),
"Bloc 5": PreferenceInterval({"5":1.0, "21":0.1}),
"Bloc 6": PreferenceInterval({"6":0.5, "22":0.5}),
"Bloc 7": PreferenceInterval({"7":0.1, "23":0.1}),
"Bloc 8": PreferenceInterval({"8":.2}),
}

# Create the blocs
# Largest bloc, members tend to wander a bit
bloc1 = Bloc(name="Bloc 1", size=15000,
              candidates=["1","9","10","11","12"],
              cohesion={"Bloc 1":0.65, "Bloc 2":0.05, "Bloc 3":0.15, "Bloc 4":0.05,
                         "Bloc 5":0.05, "Bloc 6":0.0, "Bloc 7":0.05, "Bloc 8":0.0},
              preference=pref_intervals)

# Next largest bloc, somewhat strong party ties
bloc2 = Bloc(name="Bloc 2", size=12000,
              candidates=["2","13","14","15","16"],
              cohesion={"Bloc 1":0.1, "Bloc 2":0.65, "Bloc 3":0.0, "Bloc 4":0.1,
                         "Bloc 5":0.0, "Bloc 6":0.1, "Bloc 7":0.05, "Bloc 8":0.0},
              preference=pref_intervals)

# mid size party, strong party ties
bloc3 = Bloc(name="Bloc 3", size=8500,
              candidates=["3","17","18"],
              cohesion={"Bloc 1":0.05, "Bloc 2":0.0, "Bloc 3":0.8, "Bloc 4":0.1,
                         "Bloc 5":0.0, "Bloc 6":0.0, "Bloc 7":0.05, "Bloc 8":0.0},
              preference=pref_intervals)

# mid size party, strong party ties
bloc4 = Bloc(name="Bloc 4", size=8000,
              candidates=["4","19","20"],
              cohesion={"Bloc 1":0.0, "Bloc 2":0.05, "Bloc 3":0.1, "Bloc 4":0.8,
                         "Bloc 5":0.0, "Bloc 6":0.0, "Bloc 7":0.05, "Bloc 8":0.0},
              preference=pref_intervals)

# Small party, very strong ties
bloc5 = Bloc(name="Bloc 5", size=3000,
              candidates=["5","21"],
              cohesion={"Bloc 1":0.0, "Bloc 2":0.0, "Bloc 3":0.05, "Bloc 4":0.0,
                         "Bloc 5":0.9, "Bloc 6":0.0, "Bloc 7":0.05, "Bloc 8":0.0},
              preference=pref_intervals)

# Small party, very strong ties
bloc6 = Bloc(name="Bloc 6", size=3000,
              candidates=["6","22"],
              cohesion={"Bloc 1":0.0, "Bloc 2":0.0, "Bloc 3":0.0, "Bloc 4":0.05,
                         "Bloc 5":0.0, "Bloc 6":0.9, "Bloc 7":0.05, "Bloc 8":0.0},
              preference=pref_intervals)

# Small party, somewhat strong ties
bloc7 = Bloc(name="Bloc 7", size=2000,
              candidates=["7","23"],
              cohesion={"Bloc 1":0.1, "Bloc 2":0.1, "Bloc 3":0.05, "Bloc 4":0.05,
                         "Bloc 5":0.0, "Bloc 6":0.0, "Bloc 7":0.7, "Bloc 8":0.0},
              preference=pref_intervals)

# Cult (VoteKit won't let me say that they only vote for 1 candidate)
bloc8 = Bloc(name="Bloc 8", size=800,
              candidates=["8"],
              cohesion={"Bloc 1":0.0, "Bloc 2":0.0, "Bloc 3":0.0, "Bloc 4":0.0,
                         "Bloc 5":0.0, "Bloc 6":0.01, "Bloc 7":0.0, "Bloc 8":.99},
              preference=pref_intervals)

# condense values into arguments for generator
candidates, proportions, cohesion, params = Bloc.outputVars([bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8])

# Create the generator
generator = name_BradleyTerry(
    slate_to_candidates = candidates,
    bloc_voter_prop = proportions,
    pref_intervals_by_bloc = params,
    cohesion_parameters = cohesion,
)

# Make a set of ballots using MCMC method
ballots = generator.generate_profile_MCMC(10000)

# resolve ties by removing tied entries (not a good method, but the best I've got at 1 AM)
cleanBallots = clean_ranked_profile(ballots, lambda rankings : tuple(i if len(i) <= 1 else frozenset() for i in rankings))

# run IRV election with these ballots
result = IRV(cleanBallots)

# print time taken
stop = monotonic_ns()
print(f"Time taken (ns): {stop-start}")
