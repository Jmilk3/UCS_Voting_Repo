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
# Total Preference (Hispanic) = 2.218
# Total Preference (Other) = 0.929
BoE_Hispanic = SimParams("Charlotte Board of Education Hispanic",
                                       Bloc("Hispanic Voters",
                                             0.05633604382281128,
                                             ["Annette Albright", "Clara Kennedy Witherspoon", "Juanrique Pallamente Hall", "Lenora Shipp", "Michael Johnson", 
                                                  "Omar Harris", "Peggy A. Capehart", "Shamaiye Haynes", "Tigress Sydney Acute McDaniel"],
                                             {"Hispanic Voters": 0.927, "Other Voters": 0.073},
                                             {"Hispanic Voters": {"Annette Albright": [0.1034564, 0.23607751], "Clara Kennedy Witherspoon": [0.0825332, 0.16398849], "Juanrique Pallamente Hall": [0.13725857, 0.20583245],
                                                                 "Lenora Shipp": [0.16802121, 0.3976457], "Michael Johnson": [0.02938147, 0.15296326], "Omar Harris": [0.36443793, 0.51330224], 
                                                                 "Peggy A. Capehart": [0.02046192, 0.07388189], "Shamaiye Haynes": [0.38881949, 0.66313968], "Tigress Sydney Acute McDaniel": [0.16980914, 0.2312324]},
                                              "Other Voters": {"Bill Fountain": [0.00044219, 0.0549015], "Brian Kasher": [0.0001714, 0.026125], "Claire Covington": [0.00027685, 0.03270691], 
                                                               "Liz Monterrey": [0.000254, 0.05946609], "Monty Witherspoon": [0.02324701, 0.21177767]}}),
                                        Bloc("Other Voters",
                                             1-0.05633604382281128,
                                             ["Bill Fountain", "Brian Kasher", "Claire Covington", "Liz Monterrey", "Monty Witherspoon"],
                                             {"Hispanic Voters": 0.524, "Other Voters": 0.476},
                                             {"Other Voters": {"Bill Fountain": [0.07112338, 0.08337395], "Brian Kasher": [0.03721439, 0.04189248], "Claire Covington": [0.07137325, 0.07855081], 
                                                               "Liz Monterrey": [0.11870552, 0.13266713], "Monty Witherspoon": [0.11692371, 0.13010112]},
                                              "Hispanic Voters": {"Annette Albright": [0.07147533, 0.08058374], "Clara Kennedy Witherspoon": [0.04225919, 0.04797588], "Juanrique Pallamente Hall": [0.01396952, 0.01863866],
                                                                 "Lenora Shipp": [0.13244394, 0.14818668], "Michael Johnson": [0.06298293, 0.0714706], "Omar Harris": [0.01573411, 0.02641745], 
                                                                 "Peggy A. Capehart": [0.02141676, 0.02512911], "Shamaiye Haynes": [0.07418624, 0.09307679], "Tigress Sydney Acute McDaniel": [0.01256425, 0.01684948]}}),
                                        num_seats=3,
                                        num_ballots=1000)

## High School Diploma vs all other edu
# Total Preference (High School Diploma) = 1.284
# Total Preference (Other) = 0.942
BoE_HS = SimParams("Charlotte Board of Education High School Diploma",
                                       Bloc("Hispanic Voters",
                                             0.17619197855664082,
                                             ["Annette Albright", "Clara Kennedy Witherspoon", "Juanrique Pallamente Hall", "Lenora Shipp", "Michael Johnson", 
                                                  "Monty Witherspoon", "Omar Harris", "Peggy A. Capehart", "Shamaiye Haynes", "Tigress Sydney Acute McDaniel"],
                                             {"HS Diploma Voters": 0.935, "Other Voters": 0.065},
                                             {"HS Diploma Voters": {"Annette Albright": [0.10832458, 0.14381066], "Clara Kennedy Witherspoon": [0.0641808, 0.08807037], "Juanrique Pallamente Hall": [0.0597993, 0.07921744], 
                                                                    "Lenora Shipp": [0.20236662, 0.26563822], "Michael Johnson": [0.05543787, 0.09195079], "Monty Witherspoon": [0.10302583, 0.16109317], 
                                                                    "Omar Harris": [0.15949882, 0.19973066], "Peggy A. Capehart": [0.02263642, 0.03895224], "Shamaiye Haynes": [0.24395966, 0.31946786], 
                                                                    "Tigress Sydney Acute McDaniel": [0.0546183, 0.07502047]},
                                              "Other Voters": {"Bill Fountain": [0.00012716, 0.01685915], "Brian Kasher": [4.95359905e-05, 7.58914743e-03], "Claire Covington": [0.00011682, 0.01360936], "Liz Monterrey": [0.00016559, 0.01593462]}}),
                                        Bloc("Other Voters",
                                             1-0.17619197855664082,
                                             ["Bill Fountain", "Brian Kasher", "Claire Covington", "Liz Monterrey"],
                                             {"HS Diploma Voters": 0.609, "Other Voters": 0.391},
                                             {"Other Voters": {"Bill Fountain": [0.08344722, 0.09672401], "Brian Kasher": [0.04346639, 0.04839166], "Claire Covington": [0.08237453, 0.09019571], "Liz Monterrey": [0.1393355, 0.15335571]},
                                              "HS Diploma Voters": {"Annette Albright": [0.06721553, 0.07600306], "Clara Kennedy Witherspoon": [0.04073136, 0.04658573], "Juanrique Pallamente Hall": [0.01296231, 0.01779978], 
                                                                    "Lenora Shipp": [0.12186529, 0.1375638], "Michael Johnson": [0.06291125, 0.07199411], "Monty Witherspoon": [0.11407531, 0.12841285], 
                                                                    "Omar Harris": [0.01006711, 0.02011595], "Peggy A. Capehart": [0.02125809, 0.02531302], "Shamaiye Haynes": [0.06139062, 0.07985358], 
                                                                    "Tigress Sydney Acute McDaniel": [0.01404047, 0.01911583]}}),
                                        num_seats=3,
                                        num_ballots=1000)

## Some College vs all other edu
# Total Preference (Some College) = 1.256
# Total Preference (Other) = 0.939
BoE_SC = SimParams("Charlotte Board of Education Some College",
                                       Bloc("Some College Voters",
                                             0.20768039382356163,
                                             ["Annette Albright", "Clara Kennedy Witherspoon", "Juanrique Pallamente Hall", "Lenora Shipp", "Michael Johnson", 
                                                  "Monty Witherspoon", "Omar Harris", "Peggy A. Capehart", "Shamaiye Haynes", "Tigress Sydney Acute McDaniel"],
                                             {"Some College Voters": 0.98, "Other Voters": 0.02},
                                             {"Some College Voters": {"Annette Albright": [0.09185972, 0.13852781], "Clara Kennedy Witherspoon": [0.05941069, 0.08900966], "Juanrique Pallamente Hall": [0.06610786, 0.0889527], 
                                                                    "Lenora Shipp": [0.1853316, 0.26705338], "Michael Johnson": [0.05618369, 0.10120483], "Monty Witherspoon": [0.09222719, 0.16227187], 
                                                                    "Omar Harris": [0.15261047, 0.20640865], "Peggy A. Capehart": [0.02204241, 0.0416127], "Shamaiye Haynes": [0.19994711, 0.2990489], 
                                                                    "Tigress Sydney Acute McDaniel": [0.05873863, 0.08456181]},
                                              "Other Voters": {"Bill Fountain": [0.00025393, 0.03109058], "Brian Kasher": [0.00011992, 0.01256871], "Claire Covington": [0.00016555, 0.01418002], "Liz Monterrey": [0.00019441, 0.02950302]}}),
                                        Bloc("Other Voters",
                                             1-0.20768039382356163,
                                             ["Bill Fountain", "Brian Kasher", "Claire Covington", "Liz Monterrey"],
                                             {"Some College Voters": 0.602, "Other Voters": 0.398},
                                             {"Other Voters": {"Bill Fountain": [0.08227184, 0.0983126], "Brian Kasher": [0.04350065, 0.04915515], "Claire Covington": [0.08425046, 0.09263074], "Liz Monterrey": [0.13962302, 0.15624762]},
                                              "Some College Voters": {"Annette Albright": [0.06649202, 0.07911062], "Clara Kennedy Witherspoon": [0.03937671, 0.04731823], "Juanrique Pallamente Hall": [0.00867895, 0.01497443], 
                                                                    "Lenora Shipp": [0.11784588, 0.13952454], "Michael Johnson": [0.06009566, 0.07197742], "Monty Witherspoon": [0.11267891, 0.13153558], 
                                                                    "Omar Harris": [0.00320508, 0.01751386], "Peggy A. Capehart": [0.02017298, 0.02538363], "Shamaiye Haynes": [0.05972037, 0.08653379], 
                                                                    "Tigress Sydney Acute McDaniel": [0.0099611, 0.01700932]}}),
                                        num_seats=3,
                                        num_ballots=1000)

## 4 year degree vs all other edu
# Total Preference (Bachelors Degree) = 1.075
# Total Preference (Other) = 0.969
BoE_BD = SimParams("Charlotte Board of Education Bachelor's Degree",
                                       Bloc("Bachelors Degree Voters",
                                             0.3128933933385829,
                                             ["Bill Fountain", "Brian Kasher", "Claire Covington", "Liz Monterrey"],
                                             {"Bachelors Degree Voters": 0.655, "Other Voters": 0.345},
                                             {"Bachelors Degree Voters": {"Bill Fountain": [0.16091161, 0.21544726], "Brian Kasher": [0.07530621, 0.09469024], "Claire Covington": [0.13066082, 0.16260416], "Liz Monterrey": [0.25721573, 0.31211131]},
                                              "Other Voters": {"Annette Albright": [0.03844405, 0.06381179], "Clara Kennedy Witherspoon": [0.02184409, 0.03806674],  "Juanrique Pallamente Hall": [3.13382795e-05, 4.01219521e-03], 
                                                               "Lenora Shipp": [0.06227997, 0.10471232], "Michael Johnson": [0.05254577, 0.07679623], "Monty Witherspoon": [0.09118553, 0.1303884 ],
                                                            "Omar Harris": [3.67249969e-05, 3.94662577e-03], "Peggy A. Capehart": [0.0155778, 0.02582608], "Shamaiye Haynes": [0.00027124, 0.02310895], 
                                                            "Tigress Sydney Acute McDaniel": [6.40034649e-05, 6.09460415e-03]}}),
                                        Bloc("Other Voters",
                                             1-0.3128933933385829,
                                             ["Annette Albright", "Clara Kennedy Witherspoon",  "Juanrique Pallamente Hall", "Lenora Shipp", "Michael Johnson", "Monty Witherspoon", 
                                                  "Omar Harris", "Peggy A. Capehart", "Shamaiye Haynes", "Tigress Sydney Acute McDaniel"],
                                             {"Bachelors Degree Voters": 0.123, "Other Voters": 0.877},
                                             {"Other Voters": {"Annette Albright": [0.08882584, 0.10100631], "Clara Kennedy Witherspoon": [0.05438123, 0.06220832],  "Juanrique Pallamente Hall": [0.03416646, 0.03792549], 
                                                               "Lenora Shipp": [0.1674175, 0.18798358], "Michael Johnson": [0.06448216, 0.07632652], "Monty Witherspoon": [0.1194147, 0.13780449], 
                                                               "Omar Harris": [0.06269719, 0.07046096], "Peggy A. Capehart": [0.0238638, 0.02882289], "Shamaiye Haynes": [0.14647092, 0.16238214], 
                                                               "Tigress Sydney Acute McDaniel": [0.03360548, 0.03806372]},
                                              "Bachelors Degree Voters": {"Bill Fountain": [0.00769415, 0.03459642], "Brian Kasher": [0.01162932, 0.02092585], "Claire Covington": [0.02915439, 0.04470262], "Liz Monterrey": [0.03096796, 0.0566572 ]}}),
                                        num_seats=3,
                                        num_ballots=1000)


### City Council
## Black voters vs Non-black voters
# Total Preference (Black) = 1.017
# Total Preference (Other) = 0.996
Council_Black = SimParams("Charlotte City Council Black",
                                       Bloc("Black Voters",
                                             0.3456372710884585,
                                             ["Dimple Ajmera", "James (Smuggie) Mitchell", "LaWana Slack-Mayfield", "Victoria Watlington"],
                                             {"Black Voters": 0.998, "Other Voters": 0.002},
                                             {"Black Voters": {"Dimple Ajmera": [0.24250015, 0.2527775], "James (Smuggie) Mitchell": [0.25416623, 0.25963468], 
                                                               "LaWana Slack-Mayfield": [0.25924997, 0.26724538], "Victoria Watlington": [0.24246559, 0.25230486]},
                                              "Other Voters": {"Steven J. DiFiore II": [5.13808674e-05, 6.55776635e-03]}}),
                                        Bloc("Other Voters",
                                             1-0.3456372710884585,
                                             ["Steven J. DiFiore II"],
                                             {"Black Voters": 0.872, "Other Voters": 0.128},
                                             {"Other Voters": {"Steven J. DiFiore II": [0.12098695, 0.13222964]},
                                              "Black Voters": {"Dimple Ajmera": [0.22469793, 0.23055083], "James (Smuggie) Mitchell": [0.21005555, 0.21309987], 
                                                               "LaWana Slack-Mayfield": [0.1974704, 0.20216055], "Victoria Watlington": [0.2261124, 0.23164437]}}),
                                        num_seats=4,
                                        num_ballots=1000)

## White voters vs non-white voters
# Total Preference (White) = 1.002
# Total Preference (Other) = 0.999
Council_White = SimParams("Charlotte City Council White",
                                       Bloc("White Voters",
                                             0.4654730851690758,
                                             ["Steven J. DiFiore II"],
                                             {"White Voters": 0.15, "Other Voters": 0.85},
                                             {"White Voters": {"Steven J. DiFiore II": [0.14123088, 0.15765464]},
                                              "Other Voters": {"Dimple Ajmera": [0.22165781, 0.22925065], "James (Smuggie) Mitchell": [0.20444084, 0.20861742], 
                                                               "LaWana Slack-Mayfield": [0.18911953, 0.19458965], "Victoria Watlington": [0.2229721, 0.23009154]}}),
                                        Bloc("Other Voters",
                                             1-0.4654730851690758,
                                             ["Dimple Ajmera", "James (Smuggie) Mitchell", "LaWana Slack-Mayfield", "Victoria Watlington"],
                                             {"White Voters": 0.02, "Other Voters": 0.98},
                                             {"Other Voters": {"Dimple Ajmera": [0.23875721, 0.24617175], "James (Smuggie) Mitchell": [0.2436244, 0.24765979], 
                                                               "LaWana Slack-Mayfield": [0.24576349, 0.25101606], "Victoria Watlington": [0.23957066, 0.24646372]},
                                              "White Voters": {"Steven J. DiFiore II": [0.01237651, 0.02888434]}}),
                                        num_seats=4,
                                        num_ballots=1000)

## Hispanic voters vs non-hispanic voters
# Total Preference (Hispanic) = 1.397
# Total Preference (Other) = 0.976
Council_Hispanic = SimParams("Charlotte City Council Hispanic",
                                       Bloc("Black Voters",
                                             0.05965326942005653,
                                             ["Dimple Ajmera", "James (Smuggie) Mitchell", "LaWana Slack-Mayfield", "Victoria Watlington"],
                                             {"Hispanic Voters": 0.987, "Other Voters": 0.013},
                                             {"Hispanic Voters": {"Dimple Ajmera": [0.21445526, 0.31762784], "James (Smuggie) Mitchell": [0.32174117, 0.41716091], 
                                                               "LaWana Slack-Mayfield": [0.38853288, 0.51443045], "Victoria Watlington": [0.24141378, 0.33914275]},
                                              "Other Voters": {"Steven J. DiFiore II": [0.00049256, 0.0748105 ]}}),
                                        Bloc("Other Voters",
                                             1-0.05965326942005653,
                                             ["Steven J. DiFiore II"],
                                             {"Hispanic Voters": 0.91, "Other Voters": 0.09},
                                             {"Other Voters": {"Steven J. DiFiore II": [0.08103011, 0.09548557]},
                                              "Hispanic Voters": {"Dimple Ajmera": [0.22830829, 0.23586507], "James (Smuggie) Mitchell": [0.21432933, 0.2211202 ], 
                                                               "LaWana Slack-Mayfield": [0.20170815, 0.21093938], "Victoria Watlington": [0.2281314, 0.23517389]}}),
                                        num_seats=4,
                                        num_ballots=1000)


## High School Diploma vs all other edu
Council_HS = SimParams()

## Some College vs all other edu
Council_SC = SimParams()

## 4 year degree vs all other edu
Council_BD = SimParams()
