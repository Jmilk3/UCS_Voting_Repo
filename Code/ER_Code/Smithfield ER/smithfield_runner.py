import sys
sys.path.append("../ER Code")
from ER_Code.env_reg_function import env_reg

# for the town council at large
env_reg("smithfield_town_council.csv", "Smithfield_Registration_Data.csv",
         "B", election_name="TOWN OF SMITHFIELD TOWN COUNCIL MEMBERS AT-LARGE", group_name="Black")
env_reg("smithfield_town_council.csv", "Smithfield_Registration_Data.csv",
         "A", election_name="TOWN OF SMITHFIELD TOWN COUNCIL MEMBERS AT-LARGE", group_name="Asian")
env_reg("smithfield_town_council.csv", "Smithfield_Registration_Data.csv",
         "W", election_name="TOWN OF SMITHFIELD TOWN COUNCIL MEMBERS AT-LARGE", group_name="White")
env_reg("smithfield_town_council.csv", "Smithfield_Registration_Data.csv",
         "HL", election_name="TOWN OF SMITHFIELD TOWN COUNCIL MEMBERS AT-LARGE", group_name="Hispanic")

# for the town of smithfield mayor
env_reg("smithfield_mayor.csv", "Smithfield_Registration_Data.csv",
         "B", election_name="TOWN OF SMITHFIELD MAYOR", group_name="Black")
env_reg("smithfield_mayor.csv", "Smithfield_Registration_Data.csv",
         "A", election_name="TOWN OF SMITHFIELD MAYOR", group_name="Asian")
env_reg("smithfield_mayor.csv", "Smithfield_Registration_Data.csv",
         "W", election_name="TOWN OF SMITHFIELD MAYOR", group_name="White")
env_reg("smithfield_mayor.csv", "Smithfield_Registration_Data.csv",
         "HL", election_name="TOWN OF SMITHFIELD MAYOR", group_name="Hispanic")