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
# All choosy
Mayor_Black_ac = SimParams()

# All indifferent
Mayor_Black_ai = SimParams()

# Demographic choosy, Other indifferent
Mayor_Black_mic = SimParams()

# Other choosy, Demographic indifferent
Mayor_Black_mac = SimParams()

## White voters vs non-white voters
# All choosy
Mayor_White_ac = SimParams()

# All indifferent
Mayor_White_ai = SimParams()

# Demographic choosy, Other indifferent
Mayor_White_mic = SimParams()

# Other choosy, Demographic indifferent
Mayor_White_mac = SimParams()

## Hispanic voters vs non-hispanic voters
# All choosy
Mayor_Hispanic_ac = SimParams()

# All indifferent
Mayor_Hispanic_ai = SimParams()

# Demographic choosy, Other indifferent
Mayor_Hispanic_mic = SimParams()

# Other choosy, Demographic indifferent
Mayor_Hispanic_mac = SimParams()

## High School Diploma vs all other edu
# All choosy
Mayor_HS_ac = SimParams()

# All indifferent
Mayor_HS_ai = SimParams()

# Demographic choosy, Other indifferent
Mayor_HS_mic = SimParams()

# Other choosy, Demographic indifferent
Mayor_HS_mac = SimParams()

## Some College vs all other edu
# All choosy
Mayor_SC_ac = SimParams()

# All indifferent
Mayor_SC_ai = SimParams()

# Demographic choosy, Other indifferent
Mayor_SC_mic = SimParams()

# Other choosy, Demographic indifferent
Mayor_SC_mac = SimParams()

## 4 year degree vs all other edu
# All choosy
Mayor_BD_ac = SimParams()

# All indifferent
Mayor_BD_ai = SimParams()

# Demographic choosy, Other indifferent
Mayor_BD_mic = SimParams()

# Other choosy, Demographic indifferent
Mayor_BD_mac = SimParams()

### Board of Education
## Black voters vs Non-black voters
# All choosy
BoE_Black_ac = SimParams()

# All indifferent
BoE_Black_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_Black_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_Black_mac = SimParams()

## White voters vs non-white voters
# All choosy
BoE_White_ac = SimParams()

# All indifferent
BoE_White_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_White_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_White_mac = SimParams()

## Hispanic voters vs non-hispanic voters
# All choosy
BoE_Hispanic_ac = SimParams()

# All indifferent
BoE_Hispanic_ai = SimParams()

# Demographic choosy, Other indifferent
BoE_Hispanic_mic = SimParams()

# Other choosy, Demographic indifferent
BoE_Hispanic_mac = SimParams()

## High School Diploma vs all other edu
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