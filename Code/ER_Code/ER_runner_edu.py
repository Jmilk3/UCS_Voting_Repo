from pathlib import Path

from pandas import read_csv
from numpy import array

from pyei.goodmans_er import GoodmansERBayes

from matplotlib.pyplot import savefig, close

def env_reg(election_file, registration_file, condition_col = "race_code", election_name="election", group_name="voters"):
    """
    Runs env reg for the election in election_file using the data in registration_file
    election_file (str): A path to the file which has the election data
    registration_file (str): A path to the file which has the registration data
    condition_col (str): The name of the column to use when finding members of the group
    election_name (str): The name of the election. Used in summary output and graph lables
    group_name (str): The name of the subgroup being investigated. Used in summary output and graph lables
    """
    # Set column names for various paramaters
    ELECTION_CANDIDATE_COLUMN = "Choice" # Name of the column in election_data which has candidate names
    ELECTION_PRECINCT_COLUMN = "Precinct" # Name of the column in election_data which has the precinct information
    ELECTION_VOTE_COLUMN = "Total Votes" # Name of the column in election_data which has the number of votes
    REG_PRECINCT_COLUMN = "prec_id" # Name of the column in reg_data which has the precinct information
    REG_VOTE_COLUMN = "total_vap" # Name of the column in reg_data which has the number of votes

    # Read in the data
    election_data = read_csv(election_file, dtype={ELECTION_PRECINCT_COLUMN: str})
    reg_data = read_csv(registration_file,  dtype={REG_PRECINCT_COLUMN: str})

    # Get a list of precincts and candidates for the election
    # NOTE: This assumes that unwanted candidates, such as OVER VOTE or WRITE IN, are already removed
    # It also assumes that the precinct designations are the same in both the election and reg data
    candidates = election_data[ELECTION_CANDIDATE_COLUMN].unique()
    precincts = election_data[ELECTION_PRECINCT_COLUMN].unique().tolist()

    # Remove any precincts where the number of total votes was 0
    precincts = list(filter(lambda precinct:
        sum(election_data[election_data[ELECTION_PRECINCT_COLUMN] == precinct][ELECTION_VOTE_COLUMN].values) != 0,
        precincts))
    
    # Remove any precincts that are missing from reg file
    reg_precincts = reg_data[REG_PRECINCT_COLUMN].unique()
    precincts = list(filter(lambda precinct:
                            precinct in reg_precincts,
                            precincts))
    
    ## Run ER for election
    # Get total voters by precinct from reg data
    total_reg_votes = array(list(map(lambda precinct:
        sum(reg_data[reg_data[REG_PRECINCT_COLUMN] == precinct][REG_VOTE_COLUMN].values),
        precincts)))

    # Calculate the percentage of voters that meet your condition by precinct
    voter_percent = array(list(map(lambda precinct, total_votes: 
        sum(reg_data[reg_data[REG_PRECINCT_COLUMN] == precinct][condition_col].values)/total_votes,
        precincts, total_reg_votes))) 
    
    # Calculate and print the ratio of voters in demographic to total voters
    voter_ratio = sum(list(map(lambda precinct: 
        sum(reg_data[reg_data[REG_PRECINCT_COLUMN] == precinct][condition_col].values),
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
        # NOTE: Currently saves graph as png in active directory.
        ER_plot.plot().set_title(f"{election_name}: {candidate} ({group_name})")
        savefig(f"{election_name}_{candidate}_{group_name}.png")
        close()

if __name__ == "__main__":
    # Asheboro Board of EDU
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Asheboro/asheboro_board_of_edu.csv").resolve(),
            Path(__file__ + "/../../../Clean Data/Registration Data/Asheboro/asheboro_edu_reg_2023.csv").resolve(),
            "hs_grad", election_name="Asheboro_BoE", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Asheboro/asheboro_board_of_edu.csv").resolve(),
            Path(__file__ + "/../../../Clean Data/Registration Data/Asheboro/asheboro_edu_reg_2023.csv").resolve(),
            "scol_nd", election_name="Asheboro_BoE", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Asheboro/asheboro_board_of_edu.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Asheboro/asheboro_edu_reg_2023.csv").resolve(),
            "bach_deg", election_name="Asheboro_BoE", group_name="Bachelor's Degree")


    # Asheboro City Council
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Asheboro/asheboro_city_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Asheboro/asheboro_edu_reg_2023.csv").resolve(),
            "hs_grad", election_name="Asheboro_Council", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Asheboro/asheboro_city_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Asheboro/asheboro_edu_reg_2023.csv").resolve(),
            "scol_nd", election_name="Asheboro_Council", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Asheboro/asheboro_city_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Asheboro/asheboro_edu_reg_2023.csv").resolve(),
            "bach_deg", election_name="Asheboro_Council", group_name="Bachelor's Degree")

    # for the smithfield town council at large
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Smithfield/smithfield_town_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Smithfield/smithfield_edu_reg_2023.csv").resolve(),
            "hs_grad", election_name="Smithfield_Council", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Smithfield/smithfield_town_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Smithfield/smithfield_edu_reg_2023.csv").resolve(),
            "scol_nd", election_name="Smithfield_Council", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Smithfield/smithfield_town_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Smithfield/smithfield_edu_reg_2023.csv").resolve(),
            "bach_deg", election_name="Smithfield_Council", group_name="Bachelor's Degree")

    # for the town of smithfield mayor
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Smithfield/smithfield_mayor.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Smithfield/smithfield_edu_reg_2023.csv").resolve(),
            "hs_grad", election_name="Smithfield_Mayor", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Smithfield/smithfield_mayor.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Smithfield/smithfield_edu_reg_2023.csv").resolve(),
            "scol_nd", election_name="Smithfield_Mayor", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Smithfield/smithfield_mayor.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Smithfield/smithfield_edu_reg_2023.csv").resolve(),
            "bach_deg", election_name="Smithfield_Mayor", group_name="Bachelor's Degree")

    # for the Charlotte board of education
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_board_of_education.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2023.csv").resolve(),
            "hs_grad", election_name="Charlotte_BoE", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_board_of_education.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2023.csv").resolve(),
            "scol_nd", election_name="Charlotte_BoE", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_board_of_education.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2023.csv").resolve(),
            "bach_deg", election_name="Charlotte_BoE", group_name="Bachelor's Degree")

    # for the Charlotte city council at large
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_city_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2023.csv").resolve(),
            "hs_grad", election_name="Charlotte_Council", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_city_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2023.csv").resolve(),
            "scol_nd", election_name="Charlotte_Council", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_city_council.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2023.csv").resolve(),
            "bach_deg", election_name="Charlotte_Council", group_name="Bachelor's Degree")

    # for the Charlotte city council at large
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_mayor_2022.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2022.csv").resolve(),
            "hs_grad", election_name="Charlotte_Mayor", group_name="HS Degree")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_mayor_2022.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2022.csv").resolve(),
            "scol_nd", election_name="Charlotte_Mayor", group_name="Some College")
    env_reg(Path(__file__ + "/../../../Clean Data/Election Data/Charlotte/charlotte_mayor_2022.csv").resolve(), 
            Path(__file__ + "/../../../Clean Data/Registration Data/Charlotte/charlotte_edu_reg_2022.csv").resolve(),
            "bach_deg", election_name="Charlotte_Mayor", group_name="Bachelor's Degree")
    