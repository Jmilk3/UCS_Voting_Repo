# This file contains code used to generate a list of different contests in our dataset
# It generates an output file for each of the 3 counties with contest name and date

from pathlib import Path
import pandas as pd

# Get a collection of paths to each file in the csv directory
pathlist = Path(__file__ + "/../../Election_Data_Sheets/csv/").resolve().rglob("*.csv")

# Iterate through each file, reading the data, filtering for county contests, and printing the results
for path in pathlist:
    with open(path, encoding="utf-8-sig") as file:
        # Read the data
        data = pd.read_csv(file)

        # Save the date of this file's elections
        date = data.head(1)["Election Date"][0] # just gets date from top entry, date is constant in each file

        # Filter data for mecklenburg, randolph, and johnston counties
        mecklenburg_data = data.query("County == 'MECKLENBURG' and `Contest Type` == 'C'")
        randolph_data = data.query("County == RANDOLPH and `Contest Type` == 'C'")
        johnston_data = data.query("County == JOHNSTON and `Contest Type` == 'C'")

        # Get a list of unique contest names for each county
        mecklenburg_contests = mecklenburg_data["Contest Name"].unique()
        randolph_contests = randolph_data["Contest Name"].unique()
        johnston_contests = johnston_data["Contest Name"].unique()

        # Output the list of contests to their respective files under a date header 
        with open(Path(__file__ + "/../../Election_Data_Sheets/Contest_Lists/Mecklenburg_List").resolve(),
                   "a", encoding="utf-8-sig") as file:
            file.write(f"{date}\n")
            file.write("\n".join(mecklenburg_contests) + "\n\n")

        with open(Path(__file__ + "/../../Election_Data_Sheets/Contest_Lists/Randolph_List").resolve(),
                   "a", encoding="utf-8-sig") as file:
            file.write(f"{date}\n")
            file.write("\n".join(randolph_contests) + "\n\n")

        with open(Path(__file__ + "/../../Election_Data_Sheets/Contest_Lists/Johnston_List").resolve(),
                   "a", encoding="utf-8-sig") as file:
            file.write(f"{date}\n")
            file.write("\n".join(johnston_contests) + "\n\n")


        


