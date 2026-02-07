# This file contains a first pass attempt at making an outline for what a test might look like
# I am assuming a mayoral style race, so IRV and STV are equivlant

from bloc import Bloc
from votekit import PreferenceInterval
from ballot_generators import generateAll
from votekit.elections import IRV, Plurality

## Outline the blocs for this election
# For this example, I will create 2 blocs; A majority and a minority
# This feels like an oversimplification, but it's what the MA study did.
majorityBloc = Bloc(name="majorityBloc",
                     size=0.8,
                     candidates={"A","B"},
                     cohesion={"majorityBloc":0.8, "minorityBloc":0.2},
                     preference={"majorityBloc": PreferenceInterval({"A":0.7, "B":0.5}),
                                "minorityBloc": PreferenceInterval({"C":0.5})})

minorityBloc = Bloc(name="minorityBloc",
                    size=0.2,
                    candidates={"C"},
                    cohesion={"minorityBloc":0.9, "majorityBloc":0.1},
                    preference={"majorityBloc": PreferenceInterval({"A":0.1, "B":0.5}),
                                "minorityBloc": PreferenceInterval({"C":0.7})})

## Call the ballot generators for this election. I created some helper functions in ballot_generators.py
ballots = generateAll(Bloc.outputVars([majorityBloc, minorityBloc], 5000))

## Call the elections and print the results
print("Plackett-Luce results:")
print("IRV:")
print(IRV(ballots[0]),"\n")
print("Plurality:")
print(Plurality(ballots[0]),"\n")

print("Bradley-Terry results:")
print("IRV:")
print(IRV(ballots[1]),"\n")
print("Plurality:")
print(Plurality(ballots[1]),"\n")

print("Cambridge Sampler results:")
print("IRV:")
print(IRV(ballots[2]),"\n")
print("Plurality:")
print(Plurality(ballots[2]))