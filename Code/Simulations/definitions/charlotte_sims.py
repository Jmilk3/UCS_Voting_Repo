"""
A file which contains the simulations based on Charlotte Data.
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

### Mayor 2022
## Black voters vs Non-black voters
Mayor_Black = SimParams()

## White voters vs non-white voters
Mayor_White = SimParams()

## Hispanic voters vs non-hispanic voters
Mayor_Hispanic = SimParams()

## High School Diploma vs all other edu
Mayor_HS = SimParams()

## Some College vs all other edu
Mayor_SC = SimParams()

## 4 year degree vs all other edu
Mayor_BD = SimParams()

### Board of Education
## Black voters vs Non-black voters
BoE_Black = SimParams()

## White voters vs non-white voters
BoE_White = SimParams()

## Hispanic voters vs non-hispanic voters
BoE_Hispanic = SimParams()

## High School Diploma vs all other edu
BoE_HS = SimParams()

## Some College vs all other edu
BoE_SC = SimParams()

## 4 year degree vs all other edu
BoE_BD = SimParams()

### City Council
## Black voters vs Non-black voters
Council_Black = SimParams()

## White voters vs non-white voters
Council_White = SimParams()

## Hispanic voters vs non-hispanic voters
Council_Hispanic = SimParams()

## High School Diploma vs all other edu
Council_HS = SimParams()

## Some College vs all other edu
Council_SC = SimParams()

## 4 year degree vs all other edu
# All choosy
Council_BD = SimParams()
