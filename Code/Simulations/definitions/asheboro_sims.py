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
BoE_Black = SimParams("Asheboro BoE Black",
                         Bloc("Black Voters",
                                0.08338515110060937,
                                ["Gwen Williams", "Todd Dulaney"],
                                {"Black Voters": 0.714, "Other Voters": 0.286},
                                {"Black Voters": {"Gwen Williams": [0.22874522 0.97154735], "Todd Dulaney": [0.16165885 0.77868366]},
                                "Other Voters": {"Gidget Kidd": [0.00435943 0.51336022], "Melissa Calloway":  [0.00478881 0.38278192], "Ryan Patton": [0.00374693 0.57359206]}},
                                ),
                         Bloc("Other Voters",
                                1 - 0.08338515110060937,
                                ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                                {"Black Voters": 0.152, "Other Voters": 0.848},
                                {"Other Voters": {"Gidget Kidd": [0.2106026  0.29764881], "Melissa Calloway": [0.24321702 0.29700696], "Ryan Patton": [0.21607189 0.31094888]},
                                "Black Voters": {"Gwen Williams": [0.03203704 0.13910114], "Todd Dulaney": [0.02419918 0.09730923]}},
                                ),
                         num_seats=3,
                         num_ballots=1000)

## White voters vs non-white voters
# Total Preference (White) = 0.991
# Total Preference (Other) = 1.059
BoE_White = SimParams("Asheboro BoE White",
                         Bloc("White Voters",
                              0.7698669319736351,
                              ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                              {"White Voters": 0.894, "Other Voters": 0.106},
                              {"White Voters": {"Gidget Kidd": [0.22351507 0.34069674], "Melissa Calloway": [0.2187334  0.33439373], "Ryan Patton": [0.24842178 0.35483339]}, 
                               "Other Voters": {"Gwen Williams": [0.00355029 0.15352465], "Todd Dulaney": [0.00502122 0.10340298]}}),
                         Bloc("Other Voters",
                              1-0.7698669319736351,
                              ["Gwen Williams", "Todd Dulaney"],
                              {"White Voters": 0.371, "Other Voters": 0.629},
                              {"Other Voters": {"Gwen Williams": [0.11136165 0.62420179], "Todd Dulaney": [0.0872557  0.40582457]},
                               "White Voters": {"Gidget Kidd": [0.00746813 0.32177862], "Melissa Calloway": [0.04096903 0.37900508], "Ryan Patton": [0.0032809  0.27158158]}}),
                         num_seats=3,
                         num_ballots=1000)

## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic) = 2.108
# Total Preference (Other) = 
BoE_Hispanic = SimParams("Asheboro BoE Hispanic",
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
BoE_HS = SimParams()

## Some College vs all other edu
BoE_SC = SimParams()

## 4 year degree vs all other edu
BoE_BD = SimParams()

# BoE_List = BoE_Black + BoE_White + BoE_Hispanic + BoE_HS + BoE_SC + BoE_BD 
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

## 4 year degree vs all other edusy
Council_BD = SimParams()