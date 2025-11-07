# A file with functions to extract and display statistics for a given precinct
import pandas as pd
import tabulate
from collections import Counter
import typing

NC_codes = {"A": "Asian", "B":"African American", "I": "Native American", "M": "Two or more races", "O": "Other",
               "P": "Native Hawaiian or Pacific Islander", "U": "Undesignated", "W": "White", "HL": "Hispanic",
                 "NL": "Not Hispanic", "UN": "Undesignated"}

def showRaceStats(dataframe: pd.DataFrame, precinct: str) -> str:
    """
    Displays stats about the race distribution in the given precinct.
    dataframe (DataFrame): The dataframe to pull information from.
    precinct (str): The name of the precinct to get data on.
    output (str): The data table as a python string, in case the user wants to store it
    """
    # Check for invalid precinct type
    if precinct not in dataframe.precinct_name.values:
        print("Precinct is not in the provided dataframe")
        return ""
    else:
        # isolate relevant precinct data
        data = dataframe[dataframe["precinct_name"] == precinct]

        # Get total number of voters in precinct
        total_voters = len(data)

        # Get counts of each different race and ethnicity code
        counts = Counter()

        for race_code in data.race_code.values:
            counts[race_code] += 1

        for eth_code in data.ethnic_code.values:
            counts[eth_code] += 1
        
        # Display the data in a pretty format
        output = [["Precinct:", precinct], ["Total Voters:", total_voters] ,["Race/Ethnicity", "Percentage of voters"]]
        
        # Loop through full list of possible codes, setting values as percentages
        for code in NC_codes.keys():
            output.append([NC_codes[code] + ":", f"{counts[code]/total_voters:.1%}"])

        # Create and output the result table
        final_table = tabulate.tabulate(output, tablefmt="pretty")
        # print(final_table)
        return final_table
    
def showVotingStats(dataframe: pd.DataFrame, precinct: str) -> str:
    """
    Displays stats about the vote distribution by candidate in the given precinct.
    dataframe (DataFrame): The dataframe to pull information from.
    precinct (str): The name of the precinct to get data on.
    output (str): The data table as a python string, in case the user wants to store it
    """
    # Check for invalid precinct type
    if precinct not in dataframe.precinct_name.values:
        print("Precinct is not in the provided dataframe")
        return ""
    else:
        # isolate relevant precinct data
        data = dataframe[dataframe["precinct_name"] == precinct]

        # Get the list of candidates
        candidates = data["candidate_name"].unique()

        # Get vote counts by candidate
        counts = Counter()

        for candidate in candidates:
            subdata = data[data["candidate_name"] == candidate]
            counts[candidate] += sum(subdata.vote_ct)
        
        # Get the total vote count
        total_voters = counts.total()
        if total_voters == 0:
            print("No votes cast in precinct")
            return ""

        # Display the data in a pretty format
        output = [["Precinct:", precinct], ["Total Voters:", total_voters] ,["Candidate", "Percentage of voters"]]

        # Loop through each candidate and get the precentages
        for candidate in counts.keys():
            output.append([candidate + ":", f"{counts[candidate]/total_voters:.1%}"])

        # Create and output the result table
        final_table = tabulate.tabulate(output, tablefmt="pretty")
        # print(final_table)
        return final_table
        

edu_data = pd.read_csv("board_of_edu_data.csv")
council_data = pd.read_csv("city_council_data.csv")
reg_data = pd.read_csv("reg_data_clean.csv")
edu_precincts = edu_data.precinct_name.unique()
council_precincts = council_data.precinct_name.unique()
all_precincts = reg_data.precinct_name.unique()