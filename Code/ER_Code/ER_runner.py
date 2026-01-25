from pathlib import Path

from pandas import read_csv
from numpy import array

from pyei.goodmans_er import GoodmansERBayes

from matplotlib.pyplot import savefig, close

def env_reg(election_file, registration_file, condition_code, condition_col = "race_code", election_name="election", group_name="voters"):
    """
    Runs env reg for the election in election_file using the data in registration_file
    election_file (str): A path to the file which has the election data
    registration_file (str): A path to the file which has the registration data
    condition_code (str): The code to use when identifying which voters to include in the group
    condition_col (str): The name of the column to use when finding members of the group
    election_name (str): The name of the election. Used in summary output and graph lables
    group_name (str): The name of the subgroup being investigated. Used in summary output and graph lables
    """
    # Read in the data
    election_data = read_csv(election_file)
    reg_data = read_csv(registration_file)

    # TODO: Set column names for various paramaters
    ELECTION_CANDIDATE_COLUMN = "Choice" # Name of the column in election_data which has candidate names
    ELECTION_PRECINCT_COLUMN = "Precinct" # Name of the column in election_data which has the precinct information
    ELECTION_VOTE_COLUMN = "Total Votes" # Name of the column in election_data which has the number of votes
    REG_PRECINCT_COLUMN = "precinct_abbrv" # Name of the column in reg_data which has the precinct information
    REG_VOTE_COLUMN = "total_voters" # Name of the column in reg_data which has the number of votes

    # Get a list of precincts and candidates for the election
    # NOTE: This assumes that unwanted candidates, such as OVER VOTE or WRITE IN, are already removed
    candidates = election_data[ELECTION_CANDIDATE_COLUMN].unique()
    precincts = election_data[ELECTION_PRECINCT_COLUMN].unique().tolist()

    # Remove any precincts where the number of total votes was 0
    precincts = list(filter(lambda precinct:
        sum(election_data[election_data[ELECTION_PRECINCT_COLUMN] == precinct][ELECTION_VOTE_COLUMN].values) != 0,
        precincts))
    
    ## Run ER for election
    # Get total voters by precinct from reg data
    total_reg_votes = array(list(map(lambda precinct:
        sum(reg_data[reg_data[REG_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values),
        precincts)))

    # Get the percentage of voters that meet the given condition in each precinct
    # TODO: Select a condition that defines your desired group
    voter_data = reg_data[reg_data[condition_col] == condition_code] # This condition gets all voters with race_code B

    # Calculate the percentage of voters that meet your condition by precinct
    voter_percent = array(list(map(lambda precinct, total_votes: 
        sum(voter_data[voter_data[REG_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values)/total_votes,
        precincts, total_reg_votes))) 
    
    # Calculate and print the ratio of voters in demographic to total voters
    voter_ratio = sum(list(map(lambda precinct: 
        sum(voter_data[voter_data[REG_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values),
        precincts)))/sum(total_reg_votes)
    print(f"Demographic Size Ratio ({group_name}): {voter_ratio}")

    # Run environmental reg for each candidate 
    for candidate in candidates:
        # Get a dataframe with only entries for current candidate
        subdata = election_data[election_data[ELECTION_CANDIDATE_COLUMN] == candidate]

        # Calculate the percent of the total vote the candidate got by precinct
        candidate_votes = array(list(map(lambda precinct:
            sum(subdata[subdata[ELECTION_PRECINCT_COLUMN] == precinct][ELECTION_VOTE_COLUMN].values)/ # Gets the sum of votes from subdata
            sum(election_data[election_data[ELECTION_PRECINCT_COLUMN] == precinct][ELECTION_VOTE_COLUMN].values), # divides by sum of all votes in precinct
            precincts)))
        
        # Run ER for target demographic
        ER_plot = GoodmansERBayes()
        ER_plot.fit(voter_percent,
                        candidate_votes,
                        demographic_group_name=group_name, 
                        candidate_name=candidate)

        # Print a summary of the results 
        print(f"{election_name}: {candidate} summary ({group_name})")
        print(ER_plot.summary())

        # plot the graph
        # NOTE: Plot won't display anything if run from terminal. Use savefig to store the result as a file instead.
        ER_plot.plot().set_title(f"{election_name}: {candidate} ({group_name})")

        # TODO: Uncomment this and customize the file name to store graphs
        savefig(f"{election_name}_{candidate}_{group_name}.png")
        close() # TODO: Remove this if you want the graph to stay open

if __name__ == "__main__":
    # Asheboro Board of EDU
    # env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "B", election_name="Asheboro_BoE", group_name="Black")
    # env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "A", election_name="Asheboro_BoE", group_name="Asian")
    # env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "W", election_name="Asheboro_BoE", group_name="White")
    # env_reg(Path("Asheboro ER/asheboro_board_of_edu.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "HL", condition_col="ethnic_code", election_name="Asheboro_BoE", group_name="Hispanic")


    # Asheboro City Council
    # env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "B", election_name="Asheboro_Council", group_name="Black")
    # env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "A", election_name="Asheboro_Council", group_name="Asian")
    # env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "W", election_name="Asheboro_Council", group_name="White")
    # env_reg(Path("Asheboro ER/asheboro_city_council.csv").resolve(), Path("Asheboro ER/Asheboro_Registration_Data.csv").resolve(),
    #         "HL", condition_col="ethnic_code", election_name="Asheboro_Council", group_name="Hispanic")

    # for the smithfield town council at large
    # env_reg(Path("Smithfield ER/smithfield_town_council.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #         "B", election_name="Smithfield_Council", group_name="Black")
    # env_reg(Path("Smithfield ER/smithfield_town_council.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #         "A", election_name="Smithfield_Council", group_name="Asian")
    # env_reg(Path("Smithfield ER/smithfield_town_council.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #         "W", election_name="Smithfield_Council", group_name="White")
    # env_reg(Path("Smithfield ER/smithfield_town_council.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #          "HL", condition_col="ethnic_code", election_name="Smithfield_Council", group_name="Hispanic")

    # for the town of smithfield mayor
    # env_reg(Path("Smithfield ER/smithfield_mayor.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #         "B", election_name="Smithfield_Mayor", group_name="Black")
    # env_reg(Path("Smithfield ER/smithfield_mayor.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #         "A", election_name="Smithfield_Mayor", group_name="Asian")
    # env_reg(Path("Smithfield ER/smithfield_mayor.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #         "W", election_name="Smithfield_Mayor", group_name="White")
    # env_reg(Path("Smithfield ER/smithfield_mayor.csv").resolve(), Path("Smithfield ER/Smithfield_Registration_Data.csv").resolve(),
    #        "HL", condition_col="ethnic_code", election_name="Smithfield_Mayor", group_name="Hispanic")
    
    # for the Charlotte board of education
    # TODO: FIGURE OUT WHY THIS WON'T RUN!!!!
    env_reg(Path("Charlotte ER/charlotte_board_of_education.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "B", election_name="Charlotte_BoE", group_name="Black")
    env_reg(Path("Charlotte ER/charlotte_board_of_education.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "A", election_name="Charlotte_BoE", group_name="Asian")
    env_reg(Path("Charlotte ER/charlotte_board_of_education.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "W", election_name="Charlotte_BoE", group_name="White")
    env_reg(Path("Charlotte ER/charlotte_board_of_education.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "HL", condition_col="ethnic_code", election_name="Charlotte_BoE", group_name="Hispanic")

    # for the Charlotte city council at large
    env_reg(Path("Charlotte ER/charlotte_city_council.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "B", election_name="Charlotte_Council", group_name="Black")
    env_reg(Path("Charlotte ER/charlotte_city_council.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "A", election_name="Charlotte_Council", group_name="Asian")
    env_reg(Path("Charlotte ER/charlotte_city_council.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "W", election_name="Charlotte_Council", group_name="White")
    env_reg(Path("Charlotte ER/charlotte_city_council.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2023.csv").resolve(),
            "HL", condition_col="ethnic_code", election_name="Charlotte_Council", group_name="Hispanic")

    # for the Charlotte city council at large
    env_reg(Path("Charlotte ER/charlotte_mayor_2022.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2022.csv").resolve(),
            "B", election_name="Charlotte_Mayor", group_name="Black")
    env_reg(Path("Charlotte ER/charlotte_mayor_2022.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2022.csv").resolve(),
            "A", election_name="Charlotte_Mayor", group_name="Asian")
    env_reg(Path("Charlotte ER/charlotte_mayor_2022.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2022.csv").resolve(),
            "W", election_name="Charlotte_Mayor", group_name="White")
    env_reg(Path("Charlotte ER/charlotte_mayor_2022.csv").resolve(), Path("Charlotte ER/Charlotte_Registration_Data_2022.csv").resolve(),
            "HL", condition_col="ethnic_code", election_name="Charlotte_Mayor", group_name="Hispanic")