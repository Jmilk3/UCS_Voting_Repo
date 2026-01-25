from pathlib import Path
from env_reg_function import env_reg

# Asheboro Board of EDU
env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "B", election_name="Asheboro_BoE", group_name="Black")
env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "A", election_name="Asheboro_BoE", group_name="Asian")
env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "W", election_name="Asheboro_BoE", group_name="White")
env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "HL", condition_col="ethnic_code", election_name="Asheboro_BoE", group_name="Hispanic")


# Asheboro City Council
env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "B", election_name="Asheboro_Council", group_name="Black")
env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "A", election_name="Asheboro_Council", group_name="Asian")
env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "W", election_name="Asheboro_Council", group_name="White")
env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
         "HL", condition_col="ethnic_code", election_name="Asheboro_Council", group_name="Hispanic")