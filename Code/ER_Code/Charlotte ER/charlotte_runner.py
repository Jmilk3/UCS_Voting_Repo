import sys
sys.path.append("../ER Code")
from ER_Code.env_reg_function import env_reg

# for the board of education
env_reg("charlotte_board_of_education.csv", "Charlotte_Registration_Data_2023.csv",
         "B", election_name="CHARLOTTE-MECKLENBURG SCHOOLS BOARD OF EDUCATION AT-LARGE", group_name="Black")
env_reg("charlotte_board_of_education.csv", "Charlotte_Registration_Data_2023.csv",
         "A", election_name="CHARLOTTE-MECKLENBURG SCHOOLS BOARD OF EDUCATION AT-LARGE", group_name="Asian")
env_reg("charlotte_board_of_education.csv", "Charlotte_Registration_Data_2023.csv",
         "W", election_name="CHARLOTTE-MECKLENBURG SCHOOLS BOARD OF EDUCATION AT-LARGE", group_name="White")
env_reg("charlotte_board_of_education.csv", "Charlotte_Registration_Data_2023.csv",
         "HL", election_name="CHARLOTTE-MECKLENBURG SCHOOLS BOARD OF EDUCATION AT-LARGE", group_name="Hispanic")



# for the city council at large
env_reg("charlotte_city_council.csv", "Charlotte_Registration_Data_2023.csv",
         "B", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="Black")
env_reg("charlotte_city_council.csv", "Charlotte_Registration_Data_2023.csv",
         "A", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="Asian")
env_reg("charlotte_city_council.csv", "Charlotte_Registration_Data_2023.csv",
         "W", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="White")
env_reg("charlotte_city_council.csv", "Charlotte_Registration_Data_2023.csv",
         "HL", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="Hispanic")


# for the city council at large
env_reg("charlotte_mayor_2022.csv", "Charlotte_Registration_Data_2022.csv",
         "B", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="Black")
env_reg("charlotte_mayor_2022.csv", "Charlotte_Registration_Data_2022.csv",
         "A", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="Asian")
env_reg("charlotte_mayor_2022.csv", "Charlotte_Registration_Data_2022.csv",
         "W", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="White")
env_reg("charlotte_mayor_2022.csv", "Charlotte_Registration_Data_2022.csv",
         "HL", election_name="CITY OF CHARLOTTE CITY COUNCIL AT-LARGE", group_name="Hispanic")
















# City Council
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "B", election_name="Asheboro_Council", group_name="Black")
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "A", election_name="Asheboro_Council", group_name="Asian")
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "W", election_name="Asheboro_Council", group_name="White")
env_reg("asheboro_city_council.csv", "Asheboro_Registration_Data.csv",
         "HL", condition_col="ethnic_code", election_name="Asheboro_Council", group_name="Hispanic")