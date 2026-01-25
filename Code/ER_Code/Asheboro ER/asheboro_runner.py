import sys
sys.path.append("../ER Code")
from env_reg_function import env_reg

# Board of EDU
env_reg("asheboro_board_of_edu.csv", "Asheboro_Registration_Data.csv",
         "B", election_name="Asheboro_BoE", group_name="Black")
env_reg("asheboro_board_of_edu.csv", "Asheboro_Registration_Data.csv",
         "A", election_name="Asheboro_BoE", group_name="Asian")
env_reg("asheboro_board_of_edu.csv", "Asheboro_Registration_Data.csv",
         "W", election_name="Asheboro_BoE", group_name="White")
env_reg("asheboro_board_of_edu.csv", "Asheboro_Registration_Data.csv",
         "HL", condition_col="ethnic_code", election_name="Asheboro_BoE", group_name="Hispanic")

# City Council
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "B", election_name="Asheboro_Council", group_name="Black")
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "A", election_name="Asheboro_Council", group_name="Asian")
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "W", election_name="Asheboro_Council", group_name="White")
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "HL", condition_col="ethnic_code", election_name="Asheboro_Council", group_name="Hispanic")