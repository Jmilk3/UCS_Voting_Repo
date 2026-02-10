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
# Total Preference (Black Voters) = 1 
# Total Preference (Other) = 1
Mayor_Black = SimParams("Charlotte Mayor Black",
                                       Bloc("Black Voters",
                                             0.3523913769145377,
                                             ["Vi Alexander Lyles"],
                                             {"Black Voters": 0.993, "Other Voters": 0.021},
                                             {"Black Voters": {"Vi Alexander Lyles": [0.97756713, 0.99981511]},
                                              "Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.00016144, 0.02326686]}}),
                                        Bloc("Other Voters",
                                             1-0.3523913769145377,
                                             ["Stephanie de Sarachaga-Bilbao"],
                                             {"Black Voters": 0.568, "Other Voters": 0.432},
                                             {"Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.41249206, 0.45195974]},
                                              "Black Voters": {"Vi Alexander Lyles": [0.54883942, 0.58658622]}}),
                                        num_seats=1,
                                        num_ballots=1000)

## White voters vs non-white voters
# Total Preference (White Voters) = 1 
# Total Preference (Other) = 1
Mayor_White = SimParams("Charlotte Mayor White",
                                       Bloc("White Voters",
                                             0.46812610136860816,
                                             ["Stephanie de Sarachaga-Bilbao"],
                                             {"White Voters": 0.504, "Other Voters": 0.496},
                                             {"White Voters": {"Stephanie de Sarachaga-Bilbao": [0.47505643, 0.5333203]},
                                              "Other Voters": {"Vi Alexander Lyles": [0.46697165, 0.52628899]}}),
                                        Bloc("Other Voters",
                                             1-0.46812610136860816,
                                             ["Vi Alexander Lyles"],
                                             {"White Voters": 0.068, "Other Voters": 0.932},
                                             {"Other Voters": {"Vi Alexander Lyles": [0.90371388, 0.96076984]},
                                              "White Voters": {"Stephanie de Sarachaga-Bilbao": [0.03866245, 0.09649718]}}),
                                        num_seats=1,
                                        num_ballots=1000)

## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic Voters) = 1 
# Total Preference (Other) = 1
Mayor_Hispanic = SimParams("Charlotte Mayor Hispanic",
                                       Bloc("Hispanic Voters",
                                             0.05572245899221376,
                                             ["Vi Alexander Lyles"],
                                             {"Hispanic Voters": 0.901, "Other Voters": 0.098},
                                             {"Hispanic Voters": {"Vi Alexander Lyles": [0.64638844, 0.99720473]},
                                              "Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.00226044, 0.33978224]}}),
                                        Bloc("Other Voters",
                                             1-0.05572245899221376,
                                             ["Stephanie de Sarachaga-Bilbao"],
                                             {"Hispanic Voters": 0.706, "Other Voters": 0.294},
                                             {"Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.26694011, 0.32023033]},
                                              "Hispanic Voters": {"Vi Alexander Lyles": [0.68113962, 0.73268707]}}),
                                        num_seats=1,
                                        num_ballots=1000)

## High School Diploma vs all other edu
# Total Preference (High School Diploma Voters) = 1 
# Total Preference (Other) = 1
Mayor_HS = SimParams("Charlotte Mayor High School Diploma",
                                       Bloc("HS Diploma Voters",
                                             0.17701866824164159,
                                             ["Vi Alexander Lyles"],
                                             {"HS Diploma Voters": 0.984, "Other Voters": 0.016},
                                             {"HS Diploma Voters": {"Vi Alexander Lyles": [0.94323307, 0.99954274]},
                                              "Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.00042225, 0.05667088]}}),
                                        Bloc("Other Voters",
                                             1-0.17701866824164159,
                                             ["Stephanie de Sarachaga-Bilbao"],
                                             {"HS Diploma Voters": 0.651, "Other Voters": 0.348},
                                             {"Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.323149, 0.37399287]},
                                              "HS Diploma Voters": {"Vi Alexander Lyles": [0.62603827, 0.6772586]}}),
                                        num_seats=1,
                                        num_ballots=1000)


## Some College vs all other edu
# Total Preference (Some College Voters) = 1 
# Total Preference (Other) = 1
Mayor_SC = SimParams("Charlotte Mayor Some College",
                                       Bloc("Some College Voters",
                                             0.21886458142114884,
                                             ["Vi Alexander Lyles"],
                                             {"Some College Voters": 0.979, "Other Voters": 0.021},
                                             {"Some College Voters": {"Vi Alexander Lyles": [0.92521609, 0.99950133]},
                                              "Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.00060816, 0.07057249]}}),
                                        Bloc("Other Voters",
                                             1-0.21886458142114884,
                                             ["Stephanie de Sarachaga-Bilbao"],
                                             {"Some College Voters": 0.641, "Other Voters": 0.359},
                                             {"Other Voters": {"Stephanie de Sarachaga-Bilbao": [0.33014193, 0.38800133]},
                                              "Some College Voters": {"Vi Alexander Lyles": [0.61391905, 0.67124188]}}),
                                        num_seats=1,
                                        num_ballots=1000)

## 4 year degree vs all other edu
# Total Preference (Bachelors Degree Voters) = 1 
# Total Preference (Other) = 1
Mayor_BD = SimParams("Charlotte Mayor Bachelors Degree",
                                       Bloc("Bachelors Degree Voters",
                                             0.3019721772166043,
                                             ["Stephanie de Sarachaga-Bilbao"],
                                             {"Bachelors Degree Voters": 0.764, "Other Voters": 0.236},
                                             {"Bachelors Degree Voters": {"Stephanie de Sarachaga-Bilbao": [0.66695495, 0.85770879]},
                                              "Other Voters": {"Vi Alexander Lyles": [0.13976433, 0.330838]}}),
                                        Bloc("Other Voters",
                                             1-0.3019721772166043,
                                             ["Vi Alexander Lyles"],
                                             {"Bachelors Degree Voters": 0.072, "Other Voters": 0.929},
                                             {"Other Voters": {"Vi Alexander Lyles": [0.88415057, 0.97381907]},
                                              "Bachelors Degree Voters": {"Stephanie de Sarachaga-Bilbao": [0.02803376, 0.11680264]}}),
                                        num_seats=1,
                                        num_ballots=1000)

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
Council_BD = SimParams()
