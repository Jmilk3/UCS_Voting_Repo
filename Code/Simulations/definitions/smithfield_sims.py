"""
A file which contains simulation definitions based on smithfield data
"""
from structures.sim_params import SimParams
from structures.bloc import Bloc

### Mayor
## Black voters vs Non-black voters
# Black Voter Sum = 1.547
# Other Voter Sum = 0.887
Mayor_Black = SimParams("Smithfield Council Black",
                        Bloc("Black Voters",
                             0.26221453287197233,
                             ["Doris Louise Wallace", "Felicia C. Baxter", "Stuart Ashby Lee"],
                             {"Black Voters": 0.635, "Other Voters": 0.365},
                             {"Black Voters": {"Doris Louise Wallace": [0.0350471  0.83714949], "Felicia C. Baxter": [0.05430359 0.54919671], "Stuart Ashby Lee": [0.02759562 0.39267972]},
                               "Other Voters": {"John A. Dunn", "Roger A. Wood", "Stephen Rabil"}}),    
                        Bloc("Other Voters",
                             1 - 0.26221453287197233,
                             ["John A. Dunn", "Roger A. Wood", "Stephen Rabil"],
                             {"Black Voters": .248, "Other Voters": .752},
                             {}
                             ))

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

### Town Council
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