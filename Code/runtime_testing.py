import votekit as vk
import votekit.ballot_generator as bg
import votekit.elections as el
import time
from bloc import Bloc

# Start timing the runtime of the program
start = time.monotonic_ns()

## Create parameters for ballot generation
# Since all of the blocs will only have 1 candidate, I can create a single set of pref intervals for all of them
pref_intervals = {
"Bloc 1": vk.PreferenceInterval({"Candidate One": 1.0}),
"Bloc 2": vk.PreferenceInterval({"Candidate Two": 1.0}),
"Bloc 3": vk.PreferenceInterval({"Candidate Three": 1.0})
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

# Create the generator
generator = bg.name_BradleyTerry(
    slate_to_candidates = candidates,
    bloc_voter_prop = proportions,
    pref_intervals_by_bloc = params,
    cohesion_parameters = cohesion,
)

# Make 30k ballots (equal to people in blocs)
ballots = generator.generate_profile(30000)

# run a RCV election with the fake ballots
result = el.IRV(ballots)

stop = time.monotonic_ns
print(f"Time taken (ns): {stop-start}")