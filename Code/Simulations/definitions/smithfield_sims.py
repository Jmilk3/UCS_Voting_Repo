"""
A file which contains simulation definitions based on smithfield data
"""
from structures.sim_params import SimParams
from structures.bloc import Bloc

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

## High School Diploma vs all other edu
Mayor_HS = SimParams("Smithfield Mayor HS Degree",
                    Bloc("HS Degree",
                    0.2887571881234597,
                    ["Doris Louise Wallace", "Felicia C. Baxter", "John A. Dunn","Stephen Rabil"],
                    {"HS Degree Voters": }

                    )

)

## Some College vs all other edu
Mayor_SC = SimParams()

## 4 year degree vs all other edu
Mayor_BD = SimParams()

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