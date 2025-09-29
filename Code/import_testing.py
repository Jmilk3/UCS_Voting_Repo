import pandas as pd
from pathlib import Path
import csv

# Open one of the voting files
# Path structured to work with current repo file structure (9/28)
# encoding is utf-8, but deals with Byte Order Mark (BOM) correctly if it is present
with open(Path(__file__ + "/../../Election_Data_Sheets/csv/results_pct_20220517.csv").resolve(),
           encoding="utf-8-sig") as file:
    data = pd.read_csv(file)

# Filter for specific data (Mecklenburg county level elections)
county_data = data.query("County == 'MECKLENBURG' and `Contest Type` == 'C'")

# Filter for data about a specific races (Mecklenburg mayor election primaries)
# We'd need to get the name or id of the contests we care about.
contest_data = data.query("County == 'MECKLENBURG' and `Contest Group ID` == 28 or `Contest Group ID` == 30")

# Get the full list of candidates
candidates = contest_data["Choice"].unique()

# Get each candidate's party, add it to their name
# As a fun complication, candidates that aren't dem or rep are left blank in this slot
# I'm not sure why they are listed in the primaries
candidates_with_party = {}
for candidate in candidates:
    # Get index of row with candidate
    index = contest_data[contest_data["Choice"] == candidate].index[0]
    
    # Get the party and add result to list
    candidates_with_party[candidate] = contest_data["Choice Party"][index]

# Get the total votes for each candidate
candidates_with_vote = {}
for candidate in candidates:
    # get the different entries for each candidate
    entries = contest_data[contest_data["Choice"] == candidate]

    # Sum the total votes for the candidate accross all entries
    candidates_with_vote[candidate] = entries["Total Votes"].sum()

# Write relevant data into new, votekit friendly file
with open(Path(__file__ + "/../../Election_Data_Sheets/Specific_Contests/Charlotte_Mayor_Primaries_22.csv").resolve(),
           encoding="utf-8-sig", mode="w", newline='') as file:
    # Open the file with the csv library, write a header
    writer = csv.writer(file)
    writer.writerow(["Candidate", "Party", "Total Votes"])

    # Write each candidate's data to the file
    for candidate in candidates:
        writer.writerow([candidate, candidates_with_party[candidate], candidates_with_vote[candidate]])
