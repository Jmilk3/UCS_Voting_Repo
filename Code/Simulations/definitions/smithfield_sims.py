"""
A file which contains simulation definitions based on smithfield data
"""
from definitions.structures.sim_params import SimParams
from definitions.structures.bloc import Bloc

### Town Council 
## Black voters vs Non-black voters
# Black Voter Sum = 1.547
# Other Voter Sum = 0.887
Council_Black = SimParams("Smithfield Council Black",
                        Bloc("Black Voters",
                             0.26221453287197233,
                             ["Doris Louise Wallace", "Felicia C. Baxter", "Stuart Ashby Lee"],
                             {"Black Voters": 0.635, "Other Voters": 0.365},
                             {"Black Voters": {"Doris Louise Wallace": [0.0350471, 0.83714949], "Felicia C. Baxter": [0.05430359, 0.54919671], "Stuart Ashby Lee": [0.02759562, 0.39267972]},
                               "Other Voters": {"John A. Dunn", "Roger A. Wood", "Stephen Rabil"}}),    
                        Bloc("Other Voters",
                             1 - 0.26221453287197233,
                             ["John A. Dunn", "Roger A. Wood", "Stephen Rabil"],
                             {"Black Voters": .248, "Other Voters": .752},
                             {"Other Voters": {"John A. Dunn":[0.00762412, 0.72076492],"Roger A. Wood":[0.048972, 0.39803155],"Stephen Rabil":[0.04642385, 0.33779826]},
                             "Black Voters": {"Doris Louise Wallace": [], "Felicia C. Baxter": [], "Stuart Ashby Lee": []}}
                             ))

## White voters vs non-white voters
# White Voter Sum = 0.269 + 0.307 + 0.289 = 0.865
# Total Voter Sum for White = (0.269 + 0.307 + 0.289) + (0.134 + 0.062 + 0.072)
# Other Voter Sum = 0.134 + 0.062 + 0.072

# Go to non-white credible interval
# Non-White Voter Sum = 0.295 + 0.202 + 0.144 = 0.641
# Total Voter Sum for Other = 0.295 + 0.202 + 0.144 + (0.155 + 0.137 + 0.081) = 1.014
Council_White = SimParams("Smithfield Council White",
                         Bloc("White Voters",
                               0.5539792387543253,
                               ["John A. Dunn", "Roger A. Wood","Stephen Rabil"],
                               {"White Voters": 0.763 , "Other Voters": 0.237},
                               {"White Voters": {"John A. Dunn": [0.04282843, 0.48461719], "Roger A. Wood": [0.06602954, 0.48600886],"Stephen Rabil":[0.08385126, 0.41970593]},
                               "Other Voters": {"Doris Louise Wallace", "Felicia C. Baxter", "Stuart Ashby Lee"}}),
                         Bloc("Other Voters",
                               1-0.5539792387543253,
                               ["Doris Louise Wallace", "Felicia C. Baxter", "Stuart Ashby Lee"],
                               {"White Voters": 0.368 , "Other Voters": 0.632},
                               {"Other Voters":{"Doris Louise Wallace":[0.03244007, 0.56871831], "Felicia C. Baxter": [0.03662972, 0.35616532], "Stuart Ashby Lee":[0.020401, 0.25984401]},
                               "White Voters":{"John A. Dunn", "Roger A. Wood","Stephen Rabil"}}
                              ))

## Hispanic voters vs non-hispanic voters
# Hispanic Voter Sum = 0.515 + 0.564 + 0.477 + 0.421 + 0.468 = 2.445
# Total Voter Sum for Hispanic = 0.515 + 0.564 + 0.477 + 0.421 + 0.468 + (0.475) = 2.92


# Go to non-hispanic intervals
# Non-hispanic voter sum = 0.198
# Total Voter Sum for non-hispanic = 0.198 + (0.167 + 0.080 + 0.180 + 0.168 + 0.072) = 0.865
Council_Hispanic = SimParams("Smithfield Council Hispanic",
                             Bloc("Hispanic Voters",
                                  0.0746712802768166,
                                  ["Doris Louise Wallace","Felicia C. Baxter", "John A. Dunn","Stephen Rabil","Stuart Ashby Lee"],
                                  {"Hispanic Voters": 0.837, "Other Voters": 0.163},
                                  {"Hispanic Voters": {"Doris Louise Wallace":[0.02413195, 0.98277294], "Felicia C. Baxter":[0.03867637, 0.98475652], "John A. Dunn":[0.01931465, 0.97941168], "Stephen Rabil": [0.01590197, 0.95749385], "Stuart Ashby Lee": [0.0200018, 0.96070304]},
                                  "Other Voters": {"Roger A. Wood"}}),
                             Bloc("Other Voters",
                                  1-0.0746712802768166,
                                  ["Roger A. Wood"], # no clear winner, so we just picked the least slope
                                  {"Other Voters": 0.2289, "Hispanic Voters":0.7711},
                                  {"Other Voters": {"Roger A. Wood":[0.07790514, 0.3188984]},
                                  "Hispanic Voters":{"Doris Louise Wallace","Felicia C. Baxter", "John A. Dunn","Stephen Rabil","Stuart Ashby Lee"}}
                             ))


### Mayor
# HS Degree Sum = 0.444 + 0.548 = 0.992
# Non HS Degree = 0.609 + 0.399 = 1.008
## High School Diploma vs all other edu
Mayor_HS = SimParams("Smithfield Mayor HS Degree",
                    Bloc("HS Degree",
                    0.2887571881234597,
                    ["Marlon Lee"],
                    {"HS Degree":0.55242, "Other Voters": 0.44758},
                    {"HS Degree Voters": {"Marlon Lee":[0.04248843, 0.98191341]}},
                    "Other Voters":{"Andy Moore"}),
                    Bloc("Other Voters",
                    1-0.2887571881234597,
                    ["Andy Moore"],
                    {"Other Voters": 0.60417, "HS Degree": 0.39583},
                    {"Other Voters":{"Andy Moore":[0.16628708, 0.95255222]}},
                    {"HS Degree Voters": {"Marlon Lee"}}
                    ))

## Some College vs all other edu

# Some College Degree = 0.496 + 0.493 = 0.989
# Some College Degree (non) = 0.573 + 0.433 = 1.006

Mayor_SC = SimParams("Smithfield Mayor Some College Degree",
                     Bloc("Some College",
                     0.23136955756366623,
                     ["Marlon Lee"],
                     {"Some College Voters":0.50152,"Other Voters": 0.49848},
                     {"Some College Voters": {"Marlon Lee":[0.02026, 0.97089462]}},
                     {"Other Voters":{"Andy Moore"}}),
                     Bloc("Other Voters",
                     1-0.23136955756366623,
                     ["Andy Moore"],
                     {"Other Voters": 0.56958, "Some College Degree":0.43042},
                     {"Other Voters": {"Andy Moore":[0.089, 0.821]}},
                     {"Some College Voters": {"Marlon Lee"}}
                     ))

## 4 year degree vs all other edu

# (0.52900 + 0.46300)
# 0.44600 + 0.55500
Mayor_BD = SimParams("Smithfield Mayor Bachelor’s Degree",
                     Bloc("Bachelor’s Degree",
                     0.16577,
                     ["Andy Moore"],
                     {"Bachelor's Degree": 0.53327, "Other Voters": 0.46673},
                     {"Bachelor's Degree":{"Andy Moore": [0.040278, 0.97413]}},
                     {"Other Voters":{"Marlon Lee"}}),
                     Bloc("Other Voters",
                     1-0.16577,
                     ["Marlon Lee"],
                     {"Other Voters": 0.55444, "Bachelor's Degree":0.44556},
                     {"Other Voters":{"Marlon Lee":[0.083341, 0.84795]}},
                     {"Bachelor’s Degree Voters":{"Andy Moore"}}
                     ))

## Black voters vs Non-black voters

# Black Voters: 0.64700 + 0.36800

# Non: 0.64700 + 0.34800 = 0.995
Mayor_Black = SimParams("Smithfield Mayor Black",
                         Bloc("Black Voters",
                         0.26221,
                         ["Marlon Lee"],
                         {"Black Voters": 0.63744, "Other Voters": 0.36256},
                         {"Black Voters": {"Marlon Lee":[0.07491, 0.98861]}},
                         {"Other Voters": {"Andy Moore"}}),
                         Bloc("Other Voters",
                         1-0.26221,
                         ["Andy Moore"],
                         {"Other Voters": 0.65025, "Black Voters": 0.34975},
                         {"Other Voters": {"Andy Moore":[0.20089, 0.95465]}},
                         {"Black Voters":{"Marlon Lee"}}
                         ))

## White voters vs non-white voters

# White Voters: 0.72800 + 0.28300 = 1.011
# Non white voters: 0.34600 + 0.64100 = 0.987
Mayor_White = SimParams("Smithfield Mayor White",
                         Bloc("White Voters",
                         0.55398,
                         ["Andy Moore"],
                         {"White Voters": 0.72008, "Other Voters": 0.27992},
                         {"White Voters":{"Andy Moore":[0.17443, 0.98745]}},
                         {"Other Voters": {"Marlon Lee"}}),
                         Bloc("Other Voters",
                         1-0.55398,
                         ["Marlon Lee"],
                         {"Other Voters":0.64944, "White Voters": 0.35056},
                         {"Other Voters":{"Marlon Lee":[0.09428, 0.98278]}},
                         {"White Voters":{"Andy Moore"}}
                         ))

## Hispanic voters vs non-hispanic voters

# 0.48500 + 0.51500 
# 0.56900 + 0.43500
Mayor_Hispanic = SimParams("Smithfield Mayor Hispanic",
                           Bloc("Hispanic Voters",
                           0.07467,
                           ["Marlon Lee"],
                           {"Hispanic Voters":0.51500, "Other Voters": 0.48500},
                           {"Hispanic Voters": {"Marlon Lee":[0.02214, 0.97411]}},
                           {"Other Voters":{"Andy Moore"}}),
                           Bloc("Other Voters",
                           1-0.07467,
                           ["Andy Moore"],
                           {"Other Voters": 0.56673, "Hispanic Voters": 0.43327},
                           {"Other Voters":{"Andy Moore":[0.21599, 0.88442]}},
                           {"Hispanic Voters": {"Marlon Lee"}}
                         ))

## High School Diploma vs all other edu 
Council_HS = SimParams("Smithfield Council HS Degree",
                       Bloc("HS Degree",
                       0.2888,
                       ["Doris Louise Wallace","Felicia C. Baxter","Roger A. Wood"],
                       {"HS Degree": 0.58787, "Other Voters": 0.41211},
                       {"HS Degree":{"Doris Louise Wallace":[0.030284, 0.85110] , "Felicia C. Baxter": [0.013147, 0.60010],"Roger A. Wood":[0.011462, 0.84301]}},
                       {"Other Voters":{"John A. Dunn","Stephen Rabil","Stuart Ashby Lee"}}),
                       Bloc("Other Voters",
                       1-0.2888,
                       ["John A. Dunn","Stephen Rabil","Stuart Ashby Lee"],
                       {"Other Voters":0.52448, "HS Degree":0.47552},
                       {"Other Voters":{"John A. Dunn": [0.018790, 0.38832],"Stephen Rabil": [0.015358, 0.34312], "Stuart Ashby Lee": [0.0053917, 0.17584]}},
                       {"HS Degree":{"Doris Louise Wallace","Felicia C. Baxter","Roger A. Wood"}},
                       ))

## Some College vs all other edu --- I AM UNSURE IF I DID THIS RIGHT
Council_SC = SimParams("Smithfield Council Some College Degree",
                       0.23137,
                       Bloc(["John A. Dunn", "Felicia C. Baxter", "Roger A. Wood", "Doris Louise Wallace"],
                       {"Some College Voters": 0.75135, "Other Voters":0.24865},
                       {"Some College Voters":{"John A. Dunn": [0.015118, 0.91618], "Felicia C. Baxter": [0.016189, 0.76686], "Roger A. Wood": [0.016813, 0.93152], "Doris Louise Wallace": [0.023719, 0.92268]}},
                       {"Other Voters":{"Stephen Rabil","Stuart Ashby Lee"}}),
                       Bloc("Other Voters",
                       1-0.23137,
                       ["Stephen Rabil","Stuart Ashby Lee"],
                       {"Other Voters": 0.30012, "Some College Degree": 0.69988},
                       {"Other Voters":{"Stephen Rabil":[0.019573, 0.32314], "Stuart Ashby Lee": [0.0053042, 0.16695]}},
                       {"Some College Degree Voters":{"John A. Dunn", "Felicia C. Baxter", "Roger A. Wood", "Doris Louise Wallace"}}
                       ))

## 4 year degree vs all other edu --- I AM UNSURE IF I DID THIS RIGHT
Council_BD = SimParams("Smithfield Council Bachelor's Degree",
                       0.16577,
                       Bloc(["Doris Louise Wallace","Felicia C. Baxter", "John A. Dunn","Roger A. Wood", "Stephen Rabil"],
                       {"Bachelor's Degree Voters":0.90547,"Other Voters":0.09452975048},
                       {"Bachelor's Degree Voters":{"Doris Louise Wallace":[0.017149, 0.90484], "Felicia C. Baxter":[0.010762, 0.77634], "John A. Dunn":[0.033391, 0.93514], "Roger A. Wood":[0.022337, 0.92073],"Stephen Rabil":[0.029503, 0.88917]}},
                       {"Other Voters":{"Stuart Ashby Lee"}})
                       Bloc("Other Voters",
                       1-0.16577,
                       ["Stuart Ashby Lee"],
                       {"Other Voters":0.1067, "Bachelor's Degree Voters":0.8933},
                       {"Other Voters":{"Stuart Ashby Lee": [0.010332, 0.17375]}},
                       {"Bachelor's Degree Voters":{"Doris Louise Wallace","Felicia C. Baxter", "John A. Dunn","Roger A. Wood", "Stephen Rabil"}} 
                       ))