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
                              ["Ryan Patton", "Gidget Kidd", "Gwen Williams", "Todd Dulaney"],
                              {"Some College Voters": 0.822, "Other Voters": 0.178},
                              {"Some College Voters": {"Ryan Patton": [0.03998989, 0.97063398], "Gidget Kidd": [0.01784363, 0.94347151], "Gwen Williams": [0.01489316, 0.66603107],  "Todd Dulaney": [0.00869823, 0.44740058]}, 
                               "Other Voters": {"Melissa Calloway": [0.00646395, 0.85665243]}}),
                         Bloc("Other Voters",
                              1-0.2388778761950167,
                              ["Melissa Calloway"],
                              {"Some College Voters": 0.688, "Other Voters": 0.312},
                              {"Other Voters": {"Melissa Calloway": [0.07278013, 0.35000336]}, 
                               "Some College Voters": {"Ryan Patton": [0.02464772, 0.33932567], "Gidget Kidd": [0.03372966, 0.33761305], "Gwen Williams": [0.00531348, 0.21100252], "Todd Dulaney": [0.00423588, 0.14598128]}}),
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

BoE_List = [BoE_Black, BoE_White, BoE_Hispanic, BoE_HS, BoE_SC, BoE_BD]

# BoE_List = BoE_Black + BoE_White + BoE_Hispanic + BoE_HS + BoE_SC + BoE_BD 
### City Council
## Black voters vs Non-black voters
# Total Preference (Black) = 1.377
# Total Preference (Other) = 0.963
Council_Black = SimParams("Asheboro Council Black",
                         Bloc("Black Voters",
                              0.0864183348171975,
                              ["Harry Okeke", "Jane Hughes Redding", "Joey Trogdon"],
                              {"Black Voters": 0.73, "Other Voters": 0.27},
                              {"Black Voters": {"Harry Okeke": [0.05577107, 0.64408479], "Jane Hughes Redding": [0.03521222, 0.82337719], "Joey Trogdon": [0.01809975, 0.78902473]}, 
                               "Other Voters": {"Charles Swiers": [0.01213238, 0.53042225], "Eddie Burks":[0.0046174, 0.61357316]}}),
                         Bloc("Other Voters",
                              1-0.0864183348171975,
                              ["Charles Swiers", "Eddie Burks"],
                              {"Black Voters": 0.402, "Other Voters": 0.598},
                              {"Other Voters": {"Charles Swiers": [0.17706238, 0.25060158], "Eddie Burks": [0.21389197, 0.30652327]}, 
                               "Black Voters": {"Harry Okeke": [0.01029616, 0.08216653], "Jane Hughes Redding": [0.133542, 0.24670457], "Joey Trogdon": [0.17101543, 0.28521844]}}),
                         num_seats=3,
                         num_ballots=1000)

## White voters vs non-white voters
# Total Preference (White) = 0.983
# Total Preference (Other) = 1.069
Council_White = SimParams("Asheboro Council White",
                         Bloc("White Voters",
                              0.7645251155978058,
                              ["Charles Swiers", "Eddie Burks", "Joey Trogdon"],
                              {"White Voters": 0.764, "Other Voters": 0.236},
                              {"White Voters": {"Charles Swiers": [0.16745076, 0.28561935], "Eddie Burks": [0.16423757, 0.35141166], "Joey Trogdon": [0.12494525, 0.32068388]}, 
                               "Other Voters": {"Harry Okeke": [0.00245648, 0.09298636], "Jane Hughes Redding": [0.08540226, 0.28570741]}}),
                         Bloc("Other Voters",
                              1-0.7645251155978058,
                              ["Harry Okeke", "Jane Hughes Redding"],
                              {"White Voters": 0.579, "Other Voters": 0.421},
                              {"Other Voters": {"Harry Okeke": [0.03597439, 0.31988792], "Jane Hughes Redding": [0.02533838, 0.59022345]}, 
                               "White Voters": {"Charles Swiers": [0.02767887, 0.3736132], "Eddie Burks": [0.01718188, 0.51618317], "Joey Trogdon": [0.02241388, 0.57458407]}}),
                         num_seats=3,
                         num_ballots=1000)

## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic) = 1.992
# Total Preference (Other) = 0.926
Council_Hispanic = SimParams("Asheboro Council Hispanic",
                         Bloc("Hispanic Voters",
                              0.06869812458715069,
                              ["Harry Okeke", "Jane Hughes Redding", "Eddie Burks", "Joey Trogdon"],
                              {"Hispanic Voters": 0.85, "Other Voters": 0.15},
                              {"Hispanic Voters": {"Harry Okeke": [0.03257464, 0.92046228], "Jane Hughes Redding": [0.01843058, 0.94682347], "Eddie Burks": [0.02107622, 0.94965655], "Joey Trogdon": [0.02084265, 0.94249973]}, 
                               "Other Voters": {"Charles Swiers": [0.01114578, 0.84662559]}}),
                         Bloc("Other Voters",
                              1-0.06869812458715069,
                              ["Charles Swiers"],
                              {"Hispanic Voters": 0.77, "Other Voters": 0.23},
                              {"Other Voters": {"Charles Swiers": [0.16141744, 0.24630181]}, 
                               "Hispanic Voters": {"Harry Okeke": [0.00489417, 0.08709355], "Jane Hughes Redding": [0.13798984, 0.24636218], "Eddie Burks": [0.19212537, 0.29727978], "Joey Trogdon": [0.17401018, 0.27722708]}}),
                         num_seats=3,
                         num_ballots=1000)

## High School Diploma vs all other edu
# Total Preference (High School Diploma) = 1.397
# Total Preference (Other) = 0.795
Council_HS = SimParams("Asheboro Council High School Diploma",
                         Bloc("HS Diploma Voters",
                              0.34703521645175844,
                              ["Jane Hughes Redding", "Eddie Burks", "Joey Trogdon"],
                              {"HS Diploma Voters": 0.829, "Other Voters": 0.171},
                              {"HS Diploma Voters": {"Jane Hughes Redding": [0.02111793, 0.55761631], "Eddie Burks": [0.41916432, 0.73649781], "Joey Trogdon": [0.03265398, 0.62962327]}, 
                               "Other Voters": {"Harry Okeke": [0.00239436, 0.20824458], "Charles Swiers": [0.01016136, 0.46854336]}}),
                         Bloc("Other Voters",
                              1-0.34703521645175844,
                              ["Harry Okeke", "Charles Swiers"],
                              {"HS Diploma Voters": 0.595, "Other Voters": 0.405},
                              {"Other Voters": {"Harry Okeke": [0.00853178, 0.1335127], "Charles Swiers": [0.0775494, 0.33873071]}, 
                               "HS Diploma Voters": {"Jane Hughes Redding": [0.03037961, 0.3265113], "Eddie Burks": [0.00510627, 0.17522283], "Joey Trogdon": [0.03633622, 0.36030934]}}),
                         num_seats=3,
                         num_ballots=1000)

## Some College vs all other edu
# Total Preference (Some College) = 1.743
# Total Preference (Other) = 0.778
Council_SC = SimParams("Asheboro Council Some College",
                         Bloc("Some College Voters",
                              0.23782384650091426,
                              ["Jane Hughes Redding", "Harry Okeke", "Charles Swiers", "Joey Trogdon"],
                              {"Some College Voters": 0.825, "Other Voters": 0.175},
                              {"Some College Voters": {"Jane Hughes Redding": [0.03039714, 0.86766365], "Harry Okeke": [0.00846267, 0.35290744], "Charles Swiers": [0.02753901, 0.88304371], "Joey Trogdon": [0.02222617, 0.93391998]}, 
                               "Other Voters": {"Eddie Burks": [0.00765325, 0.90484033]}}),
                         Bloc("Other Voters",
                              1-0.23782384650091426,
                              ["Eddie Burks"],
                              {"Some College Voters": 0.683, "Other Voters": 0.317},
                              {"Other Voters": {"Eddie Burks": [0.05438047, 0.35320245]}, 
                               "Some College Voters": {"Jane Hughes Redding": [0.01184565, 0.27419021], "Harry Okeke": [0.00197304, 0.10588938], "Charles Swiers": [0.01535895, 0.28166984], "Joey Trogdon": [0.02629866, 0.31709421]}}),
                         num_seats=3,
                         num_ballots=1000)

## 4 year degree vs all other edu
# Total Preference (Bachelors Degree) = 1.583
# Total Preference (Other) = 0.919
Council_BD = SimParams("Asheboro Council Bachelors Degree",
                         Bloc("Bachelors Degree Voters",
                              0.12958609389470685,
                              ["Jane Hughes Redding", "Harry Okeke", "Charles Swiers", "Joey Trogdon"],
                              {"Bachelors Degree Voters": 0.919, "Other Voters": 0.081},
                              {"Bachelors Degree Voters": {"Jane Hughes Redding": [0.01918516, 0.91534275], "Harry Okeke": [0.03133763, 0.61234722], "Charles Swiers": [0.06794483, 0.81703388], "Joey Trogdon": [0.02719456, 0.83167083]}, 
                               "Other Voters": {"Eddie Burks": [0.0040409, 0.53774829]}}),
                         Bloc("Other Voters",
                              1-0.12958609389470685,
                              ["Eddie Burks"],
                              {"Bachelors Degree Voters": 0.697, "Other Voters": 0.303},
                              {"Other Voters": {"Eddie Burks": [0.21149928, 0.31515252]}, 
                               "Bachelors Degree Voters": {"Jane Hughes Redding": [0.09877894, 0.25446935], "Harry Okeke": [0.00201875, 0.08735622], "Charles Swiers": [0.12899007, 0.24713222], "Joey Trogdon": [0.14701774, 0.28892669]}}),
                         num_seats=3,
                         num_ballots=1000)
Council_List = [Council_Black, Council_White, Council_Hispanic, Council_HS, Council_SC, Council_BD]