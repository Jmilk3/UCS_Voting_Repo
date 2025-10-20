from votekit import PreferenceInterval
from votekit.ballot_generator import BlocSlateConfig, name_bt_profile_generator
from votekit.elections import IRV
from time import monotonic_ns
from bloc import Bloc

# This code is meant to simulate a straightforward ballot generation and election testing cycle
# It times the code, to give us an idea of how long the programs might take to run.
# On my device, the timing I usually got was about 0.19 seconds
# I'd suggest doing a larger number of trials than 1 (To reduce the risk of random variance messing with our results)
# Even still, running 100 tests would still take less than a minute

# Start timing the runtime of the program
start = monotonic_ns()

## Create parameters for ballot generation
# Since all of the blocs will only have 1 candidate, I can create a single set of pref intervals for all of them
pref_intervals = {
"Bloc One": PreferenceInterval({"Candidate One": 1.0}),
"Bloc Two": PreferenceInterval({"Candidate Two": 1.0}),
"Bloc Three": PreferenceInterval({"Candidate Three": 1.0})
}


# There are 3 blocs, each with 1 candidate
# Each bloc has a name, a size, a list of candidates, and a list of cohesion paramaters for each bloc
# I made the numbers up
bloc1 = Bloc("Bloc One", 10000, ["Candidate One"],
              {"Bloc One": 0.7, "Bloc Two": 0.2, "Bloc Three": 0.1},
              pref_intervals)

bloc2 = Bloc("Bloc Two", 15000, ["Candidate Two"],
              {"Bloc One": 0.3, "Bloc Two": 0.6, "Bloc Three": 0.1},
              pref_intervals)

bloc3 = Bloc("Bloc Three", 5000, ["Candidate Three"],
             {"Bloc One": 0.1, "Bloc Two": 0.0, "Bloc Three": 0.9},
             pref_intervals)

# Get the values that from_params wants
candidates, proportions, cohesion, params = Bloc.outputVars([bloc1, bloc2, bloc3])

# Create the generator paramater object
slate = BlocSlateConfig(n_voters=30000,
                         slate_to_candidates = candidates,
                         bloc_proportions=proportions,
                         preference_mapping=params,
                         cohesion_mapping=cohesion)

# Run the generator to get the ballots
ballots = name_bt_profile_generator(slate)

# run a RCV election with the fake ballots
result = IRV(ballots)

stop = monotonic_ns()
print(f"Time taken (ns): {stop-start}")