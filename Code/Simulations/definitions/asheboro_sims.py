"""
A file which contains the tests based on Asheboro election data

Approach to gathering the values:
Bloc size is directly gathered from data by calculating demographic voters/total voters
Candidates are considered part of a demographic bloc if they have a positive slope in the ER graph
Cohesion is calculated by taking sum of voting preferences for candidates in bloc/sum of preferences for all candidates
"""
from definitions.structures.sim_params import SimParams
from definitions.structures.bloc import Bloc

### Board of EDU
# Candidates: "Gwen Williams" "Todd Dulaney" "Gidget Kidd" "Melissa Calloway" "Ryan Patton"
## Black voters vs Non-black voters
# Total preference (Black) = 1.617
# Total preference (Other) = 0.952
# All choosy
BoE_Black = SimParams("Asheboro BoE Black AC",
                         Bloc("Black Voters",
                                0.08338515110060937,
                                ["Gwen Williams", "Todd Dulaney"],
                                {"Black Voters": 0.714, "Other Voters": 0.286},
                                {"Black Voters": 0.5, "Other Voters": 0.5}),
                         Bloc("Other Voters",
                                1 - 0.08338515110060937,
                                ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                                {"Black Voters": 0.152, "Other Voters": 0.848},
                                {"Black Voters": 0.5, "Other Voters": 0.5}),
                         num_seats=3,
                         num_ballots=1000)

## White voters vs non-white voters
# Total Preference (White) = 0.991
# Total Preference (Other) = 1.059
# All choosy
BoE_White = SimParams("Asheboro BoE White AC",
                         Bloc("White Voters",
                              0.7698669319736351,
                              ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                              {"White Voters": 0.894, "Other Voters": 0.106},
                              {"White Voters": 0.5, "Other Voters": 0.5}),
                         Bloc("Other Voters",
                              1-0.7698669319736351,
                              ["Gwen Williams", "Todd Dulaney"],
                              {"White Voters": 0.371, "Other Voters": 0.629},
                              {"White Voters": 0.5, "Other Voters": 0.5}),
                         num_seats=3,
                         num_ballots=1000)

## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic) = 2.108
# Total Preference (Other) = 
# All choosy
BoE_Hispanic = SimParams("Asheboro BoE Hispanic AC",
                         Bloc("Hispanic Voters",
                              0.06721800771048377,
                              ["Gidget Kidd", "Melissa Calloway", "Gwen Williams", "Todd Dulaney"],
                              {"Hispanic Voters": 0.894, "Other Voters": 0.106},
                              {"Hispanic Voters": 0.5, "Other Voters": 0.5}),
                         Bloc("Other Voters",
                              1-0.06721800771048377,
                              ["Ryan Patton"],
                              {"Hispanic Voters": 0.371, "Other Voters": 0.629},
                              {"Hispanic Voters": 0.5, "Other Voters": 0.5}),
                         num_seats=3,
                         num_ballots=1000)

## High School Diploma vs all other edu
# Total Preference (HS) = 
# Total Preference (Other) = 
# All choosy
BoE_HS = SimParams()

## Some College vs all other edu
# All choosy
BoE_SC = SimParams()

## 4 year degree vs all other edu
# All choosy
BoE_BD = SimParams()

# BoE_List = BoE_Black + BoE_White + BoE_Hispanic + BoE_HS + BoE_SC + BoE_BD 
### City Council
## Black voters vs Non-black voters
# All choosy
Council_Black = SimParams()

## White voters vs non-white voters
# All choosy
Council_White = SimParams()

## Hispanic voters vs non-hispanic voters
# All choosy
Council_Hispanic = SimParams()

## High School Diploma vs all other edu
# All choosy
Council_HS = SimParams()

## Some College vs all other edu
# All choosy
Council_SC = SimParams()

## 4 year degree vs all other edu
# All choosy
Council_BD = SimParams()