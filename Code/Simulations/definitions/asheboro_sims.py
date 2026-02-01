"""
A file which contains the tests based on Asheboro election data

Approach to gathering the values:
Bloc size is directly gathered from data by calculating demographic voters/total voters
Candidates are considered part of a demographic bloc if they have a positive slope in the ER graph
Cohesion is calculated by taking sum of voting preferences for candidates in bloc/sum of preferences for all candidates
"""
from structures.sim_params import SimParams
from structures.bloc import Bloc

### Board of EDU
# Candidates: "Gwen Williams" "Todd Dulaney" "Gidget Kidd" "Melissa Calloway" "Ryan Patton"
## Black voters vs Non-black voters
# Total preference (Black) = 1.617
# Total preference (Other) = 0.952
# All choosy
BoE_Black_ac = SimParams("Asheboro BoE Black AC",
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

# All indifferent
BoE_Black_ai = SimParams("Asheboro BoE Black AI",
                         Bloc("Black Voters",
                                0.08338515110060937,
                                ["Gwen Williams", "Todd Dulaney"],
                                {"Black Voters": 0.714, "Other Voters": 0.286},
                                {"Black Voters": 2, "Other Voters": 2}),
                         Bloc("Other Voters",
                                1 - 0.08338515110060937,
                                ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                                {"Black Voters": 0.152, "Other Voters": 0.848},
                                {"Black Voters": 2, "Other Voters": 2}),
                         num_seats=3,
                         num_ballots=1000)

# Demographic choosy, Other indifferent
BoE_Black_mic = SimParams("Asheboro BoE Black DC",
                         Bloc("Black Voters",
                                0.08338515110060937,
                                ["Gwen Williams", "Todd Dulaney"],
                                {"Black Voters": 0.714, "Other Voters": 0.286},
                                {"Black Voters": 0.5, "Other Voters": 0.5}),
                         Bloc("Other Voters",
                                1 - 0.08338515110060937,
                                ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                                {"Black Voters": 0.152, "Other Voters": 0.848},
                                {"Black Voters": 2, "Other Voters": 2}),
                         num_seats=3,
                         num_ballots=1000)

# Other choosy, Demographic indifferent
BoE_Black_mac = SimParams("Asheboro BoE Black OC",
                         Bloc("Black Voters",
                                0.08338515110060937,
                                ["Gwen Williams", "Todd Dulaney"],
                                {"Black Voters": 0.714, "Other Voters": 0.286},
                                {"Black Voters": 2, "Other Voters": 2}),
                         Bloc("Other Voters",
                                1 - 0.08338515110060937,
                                ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                                {"Black Voters": 0.152, "Other Voters": 0.848},
                                {"Black Voters": 0.5, "Other Voters": 0.5}),
                         num_seats=3,
                         num_ballots=1000)
BoE_Black = [BoE_Black_ac, BoE_Black_ai, BoE_Black_mic, BoE_Black_mac]

## White voters vs non-white voters
# Total Preference (White) = 0.991
# Total Preference (Other) = 1.059
# All choosy
BoE_White_ac = SimParams("Asheboro BoE White AC",
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

# All indifferent
BoE_White_ai = SimParams("Asheboro BoE White AI",
                         Bloc("White Voters",
                              0.7698669319736351,
                              ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                              {"White Voters": 0.894, "Other Voters": 0.106},
                              {"White Voters": 2, "Other Voters": 2}),
                         Bloc("Other Voters",
                              1-0.7698669319736351,
                              ["Gwen Williams", "Todd Dulaney"],
                              {"White Voters": 0.371, "Other Voters": 0.629},
                              {"White Voters": 2, "Other Voters": 2}),
                         num_seats=3,
                         num_ballots=1000)

# Demographic choosy, Other indifferent
BoE_White_mic = SimParams("Asheboro BoE White DC",
                         Bloc("White Voters",
                              0.7698669319736351,
                              ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                              {"White Voters": 0.894, "Other Voters": 0.106},
                              {"White Voters": 0.5, "Other Voters": 0.5}),
                         Bloc("Other Voters",
                              1-0.7698669319736351,
                              ["Gwen Williams", "Todd Dulaney"],
                              {"White Voters": 0.371, "Other Voters": 0.629},
                              {"White Voters": 2, "Other Voters": 2}),
                         num_seats=3,
                         num_ballots=1000)

# Other choosy, Demographic indifferent
BoE_White_mac = SimParams("Asheboro BoE White OC",
                         Bloc("White Voters",
                              0.7698669319736351,
                              ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
                              {"White Voters": 0.894, "Other Voters": 0.106},
                              {"White Voters": 2, "Other Voters": 2}),
                         Bloc("Other Voters",
                              1-0.7698669319736351,
                              ["Gwen Williams", "Todd Dulaney"],
                              {"White Voters": 0.371, "Other Voters": 0.629},
                              {"White Voters": 0.5, "Other Voters": 0.5}),
                         num_seats=3,
                         num_ballots=1000)
BoE_White = [BoE_White_ac, BoE_White_ai, BoE_White_mic, BoE_White_mac]

"""
## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic) = 
# Total Preference (Other) = 
# All choosy
# TODO: Decide on what to do when all candidates have slopes that put them in the same bloc
# BoE_Hispanic_ac = SimParams("Asheboro BoE Hispanic AC",
#                          Bloc("Hispanic Voters",
#                               0.7698669319736351,
#                               ["Gidget Kidd", "Melissa Calloway", "Ryan Patton"],
#                               {"Hispanic Voters": 0.894, "Other Voters": 0.106},
#                               {"Hispanic Voters": 0.5, "Other Voters": 0.5}),
#                          Bloc("Other Voters",
#                               1-0.7698669319736351,
#                               ["Gwen Williams", "Todd Dulaney"],
#                               {"Hispanic Voters": 0.371, "Other Voters": 0.629},
#                               {"Hispanic Voters": 0.5, "Other Voters": 0.5}),
#                          num_seats=3,
#                          num_ballots=1000)

# All indifferent
BoE_Hispanic_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_Hispanic_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_Hispanic_mac = SimParams()

## High School Diploma vs all other edu
# Total Preference (HS) = 
# Total Preference (Other) = 
# All choosy
BoE_HS_ac = SimParams()

# All indifferent
BoE_HS_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_HS_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_HS_mac = SimParams()

## Some College vs all other edu
# All choosy
BoE_SC_ac = SimParams()

# All indifferent
BoE_SC_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_SC_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_SC_mac = SimParams()

## 4 year degree vs all other edu
# All choosy
BoE_BD_ac = SimParams()

# All indifferent
BoE_BD_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_BD_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_BD_mac = SimParams()


# BoE_List = BoE_Black + BoE_White + BoE_Hispanic + BoE_HS + BoE_SC + BoE_BD 
### City Council
## Black voters vs Non-black voters
# All choosy
Council_Black_ac = SimParams()

# All indifferent
Council_Black_ai = SimParams()

# Demographic choosy, Other indifferent
Council_Black_mic = SimParams()

# Other choosy, Demographic indifferent
Council_Black_mac = SimParams()

## White voters vs non-white voters
# All choosy
Council_White_ac = SimParams()

# All indifferent
Council_White_ai = SimParams()

# Demographic choosy, Other indifferent
Council_White_mic = SimParams()

# Other choosy, Demographic indifferent
Council_White_mac = SimParams()

## Hispanic voters vs non-hispanic voters
# All choosy
Council_Hispanic_ac = SimParams()

# All indifferent
Council_Hispanic_ai = SimParams()

# Demographic choosy, Other indifferent
Council_Hispanic_mic = SimParams()

# Other choosy, Demographic indifferent
Council_Hispanic_mac = SimParams()

## High School Diploma vs all other edu
# All choosy
Council_HS_ac = SimParams()

# All indifferent
Council_HS_ai = SimParams()

# Demographic choosy, Other indifferent
Council_HS_mic = SimParams()

# Other choosy, Demographic indifferent
Council_HS_mac = SimParams()

## Some College vs all other edu
# All choosy
Council_SC_ac = SimParams()

# All indifferent
Council_SC_ai = SimParams()

# Demographic choosy, Other indifferent
Council_SC_mic = SimParams()

# Other choosy, Demographic indifferent
Council_SC_mac = SimParams()

## 4 year degree vs all other edu
# All choosy
Council_BD_ac = SimParams()

# All indifferent
Council_BD_ai = SimParams()

# Demographic choosy, Other indifferent
Council_BD_mic = SimParams()

# Other choosy, Demographic indifferent
Council_BD_mac = SimParams()
"""