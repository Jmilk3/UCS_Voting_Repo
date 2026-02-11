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
# Total Preference (Black) = 1.023
# Total Preference (Other) = 0.993
BoE_Black = SimParams("Charlotte Board of Education Black",
                                       Bloc("Black Voters",
                                             0.304673493946315,
                                             ["Juanrique Pallamente Hall", "Lenora Shipp", "Monty Witherspoon", "Omar Harris", "Shamaiye Haynes", "Annette Albright", "Clara Kennedy Witherspoon", "Tigress Sydney Acute McDaniel"],
                                             {"Black Voters": 0.88, "Other Voters": 0.22},
                                             {"Black Voters": {"Juanrique Pallamente Hall": [0.04211925, 0.04840278], "Lenora Shipp": [0.19102275, 0.21112315], "Monty Witherspoon": [0.13307559, 0.15379278], 
                                                               "Omar Harris": [0.10161023, 0.11118226], "Shamaiye Haynes": [0.19487645, 0.21171899], "Annette Albright": [0.08940406, 0.10355329], 
                                                               "Clara Kennedy Witherspoon": [0.05733124, 0.0659007], "Tigress Sydney Acute McDaniel": [0.04032222, 0.04717332]},
                                              "Other Voters": {"Bill Fountain": [2.96617443e-05, 4.96492039e-03], "Brian Kasher": [5.24646415e-05, 4.18897442e-03], "Claire Covington": [0.01233587, 0.02736172], 
                                                               "Liz Monterrey": [0.00145058, 0.02287054], "Michael Johnson": [0.05825117, 0.07210321], "Peggy A. Capehart": [0.02097296, 0.02692058]}}),
                                        Bloc("Other Voters",
                                             1-0.304673493946315,
                                             ["Bill Fountain", "Brian Kasher", "Claire Covington", "Liz Monterrey", "Michael Johnson", "Peggy A. Capehart"],
                                             {"Black Voters": 0.492, "Other Voters": 0.518},
                                             {"Other Voters": {"Bill Fountain": [0.10259963, 0.11268913], "Brian Kasher": [0.0517055, 0.05497276], "Claire Covington": [0.0889824, 0.09678387], 
                                                               "Liz Monterrey": [0.15936541, 0.17104933], "Michael Johnson": [0.06641604, 0.07361925], "Peggy A. Capehart": [0.02346959, 0.02655469]},
                                              "Black Voters": {"Juanrique Pallamente Hall": [0.01466805, 0.01809379], "Lenora Shipp": [0.12056, 0.13106008], "Monty Witherspoon": [0.10903668, 0.11969803], 
                                                               "Omar Harris": [0.01554535, 0.02051489], "Shamaiye Haynes": [0.06346838, 0.07228359], "Annette Albright": [0.07137763, 0.07840789], 
                                                               "Clara Kennedy Witherspoon": [0.04219898, 0.04657213], "Tigress Sydney Acute McDaniel": [0.01544669, 0.01902099]}}),
                                        num_seats=3,
                                        num_ballots=1000)

## White voters vs non-white voters
# Total Preference (White) = 0.999
# Total Preference (Other) = 0.998
BoE_White = SimParams("Charlotte Board of Education White",
                                       Bloc("White Voters",
                                             0.5136125512336799,
                                             ["Bill Fountain", "Brian Kasher", "Claire Covington", "Liz Monterrey", "Michael Johnson",  "Peggy A. Capehart"],
                                             {"White Voters": 0.572, "Other Voters": 0.428},
                                             {"White Voters": {"Bill Fountain": [0.12317829, 0.13727541], "Brian Kasher": [0.05702078, 0.06184019], "Claire Covington": [0.09784881, 0.10730573], 
                                                               "Liz Monterrey": [0.17469759, 0.19091959], "Michael Johnson": [0.06623552, 0.07495561],  "Peggy A. Capehart": [0.02292002, 0.02673481]},
                                              "Other Voters": {"Annette Albright": [0.06789195, 0.0768013], "Clara Kennedy Witherspoon": [0.03935605, 0.04504538], "Juanrique Pallamente Hall": [0.01031419, 0.01418794], 
                                                               "Lenora Shipp": [0.11148781, 0.12499565], "Monty Witherspoon": [0.10563548, 0.11880374], "Omar Harris": [0.00376202, 0.00967287],  
                                                               "Shamaiye Haynes": [0.04651005, 0.05800212], "Tigress Sydney Acute McDaniel": [0.01106719, 0.01525106]}}),
                                        Bloc("Other Voters",
                                             1-0.5136125512336799,
                                             ["Annette Albright", "Clara Kennedy Witherspoon", "Juanrique Pallamente Hall", "Lenora Shipp", "Monty Witherspoon", "Omar Harris",  "Shamaiye Haynes", "Tigress Sydney Acute McDaniel"],
                                             {"White Voters": 0.2, "Other Voters": 0.8},
                                             {"Other Voters": {"Annette Albright": [0.08621231, 0.0958535], "Clara Kennedy Witherspoon": [0.05448515, 0.06061302], "Juanrique Pallamente Hall": [0.03703902, 0.0411782], 
                                                               "Lenora Shipp": [0.17412257, 0.1884635], "Monty Witherspoon": [0.12776569, 0.1422899], "Omar Harris": [0.08280129, 0.08890248],  
                                                               "Shamaiye Haynes": [0.16379202, 0.17628894], "Tigress Sydney Acute McDaniel": [0.03618704, 0.04065743]},
                                              "White Voters": {"Bill Fountain": [0.00436805, 0.01868397], "Brian Kasher": [0.01120373, 0.01636531], "Claire Covington": [0.03148004, 0.04144781], 
                                                               "Liz Monterrey": [0.04098649, 0.05779439], "Michael Johnson": [0.06186561, 0.07113508],  "Peggy A. Capehart": [0.02231001, 0.02634973]}}),
                                        num_seats=3,
                                        num_ballots=1000)

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
