from pandas import read_csv
from pathlib import Path

# Helper function to help clean Charlotte Data
def addLeadingZeros(value):
    if (len(value) == 1):
        return "00" + value
    elif (len(value) == 2):
        return "0" + value
    else:
        return value

# Open 2022 elections and get charlotte mayor data
with open("All_Elections_7-26-22.csv", "r", encoding="utf-8-sig") as file:
    df = read_csv(file)
df = df[df["County"] == "MECKLENBURG"] # isolate relevant county
df = df[df["Contest Name"] == "CITY OF CHARLOTTE MAYOR"] # isolate relevant contest
df = df[df["Choice"].str.contains("Write-In") == False] # remove write-ins

# Additional cleaning to match precinct codes to reg data
df["Precinct"] = df["Precinct"].map(addLeadingZeros)
df = df[df["Precinct"] != "ABSENTEE"]
df = df[df["Precinct"] != "PROVISIONAL"]
with open("charlotte_mayor_2022.csv", "w", encoding="utf-8-sig") as file:
    df.to_csv(file)

# Open 2023 elections and get other contest's data
with open("All_Elections_11-7-23.csv", "r", encoding="utf-8-sig") as file:
    df = read_csv(file)

df = df[df["Choice"].str.contains("Write-In") == False] # remove write-ins
charlotte_df = df[df["County"] == "MECKLENBURG"] # isolate charlotte elections
smithfield_df = df[df["County"] == "JOHNSTON"] # isolate smithfield elections
asheboro_df = df[df["County"] == "RANDOLPH"] # isolate asheboro elections

# Smithfield town council 2023
out_df = smithfield_df[smithfield_df["Contest Name"] == "TOWN OF SMITHFIELD TOWN COUNCIL MEMBERS AT-LARGE"]
with open("smithfield_town_council.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Smithfield mayor 2023
out_df = smithfield_df[smithfield_df["Contest Name"] == "TOWN OF SMITHFIELD MAYOR"]
with open("smithfield_mayor.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Asheboro Board of Education 2023
out_df = asheboro_df[asheboro_df["Contest Name"] == "ASHEBORO CITY SCHOOLS BOARD OF EDUCATION"]
with open("asheboro_board_of_edu.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Asheboro City Council 2023
out_df = asheboro_df[asheboro_df["Contest Name"] == "CITY OF ASHEBORO CITY COUNCIL"]
with open("asheboro_city_council.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Charlotte City Council 2023
out_df = charlotte_df[charlotte_df["Contest Name"] == "CITY OF CHARLOTTE CITY COUNCIL AT-LARGE"]
out_df["Precinct"] = df["Precinct"].map(addLeadingZeros)
out_df = df[df["Precinct"] != "ABSENTEE"]
out_df = df[df["Precinct"] != "PROVISIONAL"]
with open("charlotte_city_council.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Charlotte Board of Education 2023
out_df = charlotte_df[charlotte_df["Contest Name"] == "CHARLOTTE-MECKLENBURG SCHOOLS BOARD OF EDUCATION AT-LARGE"]
out_df["Precinct"] = df["Precinct"].map(addLeadingZeros)
out_df = df[df["Precinct"] != "ABSENTEE"]
out_df = df[df["Precinct"] != "PROVISIONAL"]
with open("charlotte_board_of_education.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)



# Additional cleaning for Charlotte: add leading zeros to election data
with open(Path("Charlotte ER/charlotte_board_of_education.csv").resolve(), "r+", encoding="utf-8-sig") as file:
    df = read_csv(file)
    
    file.seek(0)
    df.to_csv(file)

with open(Path("Charlotte ER/charlotte_city_council.csv").resolve(), "r+", encoding="utf-8-sig") as file:
    df = read_csv(file)
    df["Precinct"] = df["Precinct"].map(addLeadingZeros)
    df = df[df["Precinct"] != "ABSENTEE"]
    df = df[df["Precinct"] != "PROVISIONAL"]
    file.seek(0)
    df.to_csv(file)

with open(Path("Charlotte ER/charlotte_mayor_2022.csv").resolve(), "r+", encoding="utf-8-sig") as file:
    df = read_csv(file)
    df["Precinct"] = df["Precinct"].map(addLeadingZeros)
    df = df[df["Precinct"] != "ABSENTEE"]
    df = df[df["Precinct"] != "PROVISIONAL"]
    file.seek(0)
    df.to_csv(file)

