# This file contains the functions used to clean and split our education data into subfiles
from pandas import read_csv
from pathlib import Path

# Open 2022 data
with open(Path(__file__ + 
               "/../../../Clean Data/Merged Education and Income Shapefiles/EDU_reg_data_2022.csv").resolve(),
                 "r", encoding="utf-8-sig") as file:
    df = read_csv(file)

# Remove unwanted income data columns
df = df.drop(columns=["less_10k","10k_15k","15k_20k","20k_25k","25k_30k",
                      "30k_35k","35k_40k","40k_45k","45k_50k","50k_60k",
                      "60k_75k","75k_100k","100k_125k","125k_150k","150k_200k","200k_plus"])

# remove unwanted edu data columns
df = df.drop(columns=["under_9g","9_to_12_nd","grad_deg_p","assoc_deg"])

# remove empty

# Filter for charlotte and output result
out_df = df[df["county_nam"] == "MECKLENBURG"]
with open("charlotte_edu_reg_2022.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Open 2023 data
with open(Path(__file__ + "/../../../Clean Data/Merged Education and Income Shapefiles/EDU_reg_data_2023.csv").resolve(), "r", encoding="utf-8-sig") as file:
    df = read_csv(file)

# Remove unwanted income data columns
df = df.drop(columns=["less_10k","10k_15k","15k_20k","20k_25k","25k_30k",
                      "30k_35k","35k_40k","40k_45k","45k_50k","50k_60k",
                      "60k_75k","75k_100k","100k_125k","125k_150k","150k_200k","200k_plus"])

# remove unwanted edu data columns
df = df.drop(columns=["under_9g","9_to_12_nd","grad_deg_p","assoc_deg"])

# Filter for charlotte and output result
out_df = df[df["county_nam"] == "MECKLENBURG"]
with open("charlotte_edu_reg_2023.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Filter for asheboro and output result
out_df = df[df["county_nam"] == "RANDOLPH"]
with open("asheboro_edu_reg_2023.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)

# Filter for smithfield and output result
out_df = df[df["county_nam"] == "JOHNSTON"]
with open("smithfield_edu_reg_2023.csv", "w", encoding="utf-8-sig") as file:
    out_df.to_csv(file)