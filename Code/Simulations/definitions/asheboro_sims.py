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
# Total preference (Black) = 1.547
# Total preference (Other) = 0.952
BoE_Black = SimParams("Asheboro BoE Black",
                         Bloc("Black Voters",
                                0.08338515110060937,
                                ["Gwen Williams", "Todd Dulaney"],
                                {"Black Voters": 0.747, "Other Voters": 0.253},
                                {"Black Voters": {"Gwen Williams": [0.22874522, 0.97154735], "Todd Dulaney": [0.16165885, 0.77868366]},
                                "Other Voters": {"Gidget Kidd": [0.00435943, 0.51336022], "Melissa Calloway":  [0.00478881, 0.38278192], "Ryan Patton": [0.00374693, 0.57359206]}},
                                ),
                         Bloc("Other Voters",
                                1 - 0.08338515110060937,
                                ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                                {"Black Voters": 0.152, "Other Voters": 0.848},
                                {"Other Voters": {"Gidget Kidd": [0.2106026,  0.29764881], "Melissa Calloway": [0.24321702, 0.29700696], "Ryan Patton": [0.21607189, 0.31094888]},
                                "Black Voters": {"Gwen Williams": [0.03203704, 0.13910114], "Todd Dulaney": [0.02419918, 0.09730923]}},
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
                              {"White Voters": {"Gidget Kidd": [0.22351507, 0.34069674], "Melissa Calloway": [0.2187334, 0.33439373], "Ryan Patton": [0.24842178, 0.35483339]}, 
                               "Other Voters": {"Gwen Williams": [0.00355029, 0.15352465], "Todd Dulaney": [0.00502122, 0.10340298]}}),
                         Bloc("Other Voters",
                              1-0.7698669319736351,
                              ["Gwen Williams", "Todd Dulaney"],
                              {"White Voters": 0.371, "Other Voters": 0.629},
                              {"Other Voters": {"Gwen Williams": [0.11136165, 0.62420179], "Todd Dulaney": [0.0872557, 0.40582457]},
                               "White Voters": {"Gidget Kidd": [0.00746813, 0.32177862], "Melissa Calloway": [0.04096903, 0.37900508], "Ryan Patton": [0.0032809, 0.27158158]}}),
                         num_seats=3,
                         num_ballots=1000)

## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic) = 2.108
# Total Preference (Other) = 0.922
BoE_Hispanic = SimParams("Asheboro BoE Hispanic",
                         Bloc("Hispanic Voters",
                              0.06721800771048377,
                              ["Gidget Kidd", "Melissa Calloway", "Gwen Williams", "Todd Dulaney"],
                              {"Hispanic Voters": 0.863, "Other Voters": 0.137},
                              {"Hispanic Voters": {"Gidget Kidd": [0.01139289, 0.91053331], "Melissa Calloway": [0.0143132, 0.89089179], "Gwen Williams": [0.04626673, 0.98212229], "Todd Dulaney": [0.0605872, 0.96751213]}, 
                               "Other Voters": {"Ryan Patton": [0.00780188, 0.88187521]}}),
                         Bloc("Other Voters",
                              1-0.06721800771048377,
                              ["Ryan Patton"],
                              {"Hispanic Voters": 0.723, "Other Voters": 0.277},
                              {"Other Voters": {"Ryan Patton": [0.18103949, 0.30824469]}, 
                               "Hispanic Voters": {"Gidget Kidd": [0.18838425, 0.29254635], "Melissa Calloway": [0.20456451, 0.29545573], "Gwen Williams": [0.03998576, 0.17439706], "Todd Dulaney": [0.01600647, 0.11221274]}}),
                         num_seats=3,
                         num_ballots=1000)

## High School Diploma vs all other edu
# Total Preference (HS) = 1.397
# Total Preference (Other) = 0.814
BoE_HS = SimParams("Asheboro BoE High School Diploma",
                         Bloc("HS Diploma Voters",
                              0.3385441497503325,
                              ["Gidget Kidd", "Melissa Calloway"],
                              {"HS Diploma Voters": 0.588, "Other Voters": 0.412},
                              {"HS Diploma Voters": {"Gidget Kidd": [0.0726379, 0.69204236], "Melissa Calloway": [0.13486879, 0.6643687 ]}, 
                               "Other Voters": {"Ryan Patton": [0.01481381, 0.67349809], "Gwen Williams": [0.00731166, 0.45436697], "Todd Dulaney": [0.00525687, 0.29982127]}}),
                         Bloc("Other Voters",
                              1-0.3385441497503325,
                              ["Ryan Patton", "Gwen Williams", "Todd Dulaney"],
                              {"HS Diploma Voters": 0.435, "Other Voters": 0.565},
                              {"Other Voters": {"Ryan Patton": [0.04392796, 0.40114991], "Gwen Williams": [0.00625728, 0.24785003], "Todd Dulaney": [0.00809163, 0.1669663]}, 
                               "HS Diploma Voters": {"Gidget Kidd": [0.02616888, 0.34354905], "Melissa Calloway": [0.04922923, 0.3237556]}}),
                         num_seats=3,
                         num_ballots=1000)

## Some College vs all other edu
# Total Preference (Some College) = 1.736
# Total Preference (Other) = 0.788
BoE_SC = SimParams("Asheboro BoE Some College",
                         Bloc("Some College Voters",
                              0.2388778761950167,
                              ["Ryan Patton", "Gidget Kidd", "Gwen Williams"],
                              {"Some College Voters": 0.711, "Other Voters": 0.289},
                              {"Some College Voters": {"Ryan Patton": [0.03998989, 0.97063398], "Gidget Kidd": [0.01784363, 0.94347151], "Gwen Williams": [0.01489316, 0.66603107]}, 
                               "Other Voters": {"Melissa Calloway": [0.00646395, 0.85665243], "Todd Dulaney": [0.00869823, 0.44740058]}}),
                         Bloc("Other Voters",
                              1-0.2388778761950167,
                              ["Melissa Calloway", "Todd Dulaney"],
                              {"Some College Voters": 0.599, "Other Voters": 0.401},
                              {"Other Voters": {"Melissa Calloway": [0.07278013, 0.35000336], "Todd Dulaney": [0.00423588, 0.14598128]}, 
                               "Some College Voters": {"Ryan Patton": [0.02464772, 0.33932567], "Gidget Kidd": [0.03372966, 0.33761305], "Gwen Williams": [0.00531348, 0.21100252]}}),
                         num_seats=3,
                         num_ballots=1000)
## 4 year degree vs all other edu
# Total Preference (Bachelors Degree) = 1.631
# Total Preference (Other) = 0.92
BoE_BD = SimParams("Asheboro BoE Bachelors Degree",
                         Bloc("Bachelors Degree Voters",
                              0.13512157177627782,
                              ["Ryan Patton", "Todd Dulaney", "Gwen Williams"],
                              {"Bachelors Degree Voters": 0.765, "Other Voters": 0.235},
                              {"Bachelors Degree Voters": {"Ryan Patton": [0.02463028, 0.92905369], "Todd Dulaney": [0.02263961, 0.72490493], "Gwen Williams": [0.04156607, 0.95872544]}, 
                               "Other Voters": {"Melissa Calloway": [0.00521031, 0.57579724], "Gidget Kidd": [0.00705057, 0.76901157]}}),
                         Bloc("Other Voters",
                              1-0.13512157177627782,
                              ["Melissa Calloway", "Gidget Kidd"],
                              {"Bachelors Degree Voters": 0.422, "Other Voters": 0.578},
                              {"Other Voters": {"Melissa Calloway": [0.20896676, 0.31280688], "Gidget Kidd": [0.15903938, 0.31146682]}, 
                               "Bachelors Degree Voters": {"Ryan Patton": [0.13238917, 0.31623319], "Todd Dulaney": [0.00363666, 0.12099312], "Gwen Williams": [0.00765606, 0.17638661]}}),
                         num_seats=3,
                         num_ballots=1000)

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