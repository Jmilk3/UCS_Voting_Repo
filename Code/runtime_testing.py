import votekit as vk
import votekit.ballot_generator as bg
import time
from bloc import Bloc

# Start timing the runtime of the program
start = time.monotonic_ns()

## Create parameters for preference interval generation
# There are 3 blocs, each with 1 candidate
# Each bloc has a name, a size, a list of candidates, and a list of cohesion paramaters for each bloc
# I made the numbers up
bloc1 = Bloc("Bloc One", 10000, ["Candidate One"],
              {"Bloc One": 0.7, "Bloc Two": 0.2, "Bloc Three": 0.1})

bloc2 = Bloc("Bloc Two", 15000, ["Candidate Two"],
              {"Bloc One": 0.3, "Bloc Two": 0.6, "Bloc Three": 0.1})

bloc3 = Bloc("Bloc Three", 5000, ["Candidate Three"],
             {"Bloc One": 0.1, "Bloc Two": 0.0, "Bloc Three": 0.9})

# Get the values that from_params wants
candidates, proportions, cohesion = Bloc.outputVars([bloc1, bloc2, bloc3])

# Create the generator
bg.name_BradleyTerry(
    slate_to_candidates = candidates,
    bloc_voter_prop = proportions,
    pref_intervals_by_bloc = {},
    cohesion_parameters = cohesion,
)
