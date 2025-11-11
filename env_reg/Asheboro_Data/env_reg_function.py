"""
Similar to env_reg_runner, but in a function format that makes it easier to use elsewhere.
Still makes assumptions about the input data that will need to be modified for non-race based seperations
Don't forget to uncomment the safefig function if you want the output files.

NOTE indicates places where the code makes assumptions about how the data was cleaned
TODO indictes places where you may need to change the code for it to work with different data
"""
import pandas as pd
import numpy as np

from pyei.goodmans_er import GoodmansER

from matplotlib.pyplot import savefig, close

def env_reg(election_file, registration_file, election_name="election", group_name="voters"):
    """
    Runs env reg for the election in election_file using the data in registration_file
    election_file (str): A path to the file which has the election data
    registration_file (str): A path to the file which has the registration data
    election_name (str): The name of the election. Used in summary output and graph lables
    group_name (str): The name of the subgroup being investigated. Used in summary output and graph lables
    """
    # Read in the data
    election_data = pd.read_csv(election_file)
    reg_data = pd.read_csv(registration_file)

    # TODO: Set column names for various paramaters
    ELECTION_CANDIDATE_COLUMN = "candidate_name" # Name of the column in election_data which has candidate names
    ELECTION_PRECINCT_COLUMN = "precinct_name" # Name of the column in election_data which has the precinct information
    ELECTION_VOTE_COLUMN = "vote_ct" # Name of the column in election_data which has the number of votes
    REG_PRECINCT_COLUMN = "precinct_name" # Name of the column in reg_data which has the precinct information
    REG_VOTE_COLUMN = "total_voters" # Name of the column in reg_data which has the number of votes

    # Get a list of precincts and candidates for the election
    # NOTE: This assumes that unwanted candidates, such as OVER VOTE or WRITE IN, are already removed
    candidates = election_data[ELECTION_CANDIDATE_COLUMN].unique()
    precincts = election_data[ELECTION_PRECINCT_COLUMN].unique().tolist()

    # Remove any precincts where the number of total votes was 0
    precincts = list(filter(lambda precinct:
        sum(election_data[election_data[ELECTION_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values) != 0,
        precincts))
    
    ## Run ER for election
    # Get total voters by precinct from reg data
    total_reg_votes = np.array(list(map(lambda precinct:
        sum(reg_data[reg_data[REG_PRECINCT_COLUMN] == precinct][ELECTION_VOTE_COLUMN].values),
        precincts)))

    # Get the percentage of voters that meet the given condition in each precinct
    # TODO: Select a condition that defines your desired group
    voter_data = reg_data[reg_data["race_code"] == "B"] # This condition gets all voters with race_code B

    # Calculate the percentage of voters that meet your condition by precinct
    voter_percent = np.array(list(map(lambda precinct, total_votes: 
        sum(voter_data[voter_data[REG_PRECINCT_COLUMN] == precinct][ELECTION_VOTE_COLUMN].values)/total_votes,
        precincts, total_reg_votes))) 

    # Run environmental reg for each candidate 
    for candidate in candidates:
        # Get a dataframe with only entries for current candidate
        subdata = election_data[election_data[ELECTION_CANDIDATE_COLUMN] == candidate]

        # Calculate the percent of the total vote the candidate got by precinct
        candidate_votes = np.array(list(map(lambda precinct:
            sum(subdata[subdata[ELECTION_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values)/ # Gets the sum of votes from subdata
            sum(election_data[election_data[ELECTION_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values), # divides by sum of all votes in precinct
            precincts)))
        
        # Run ER for target demographic
        ER_plot = GoodmansER()
        ER_plot.fit(voter_percent,
                        candidate_votes,
                        demographic_group_name=group_name, 
                        candidate_name=candidate)

        # Print a summary of the results 
        print(f"{election_name}: {candidate} summary ({group_name})")
        print(ER_plot.summary())

        # plot the graph
        # NOTE: Plot won't display anything if run from terminal. Use savefig to store the result as a file instead.
        ER_plot.plot(line_kws={"title": f"{election_name}: {candidate} ({group_name})"})

        # TODO: Uncomment this and customize the file name to store graphs
        # savefig(f"{election_name}_{candidate}_{group_name}.png")
        close() # TODO: Remove this if you want the graph to stay open
