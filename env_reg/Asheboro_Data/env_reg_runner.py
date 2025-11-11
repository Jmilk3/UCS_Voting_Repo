import pandas as pd
import numpy as np

from pyei.data import Datasets
from pyei.two_by_two import TwoByTwoEI
from pyei.goodmans_er import GoodmansER
from pyei.goodmans_er import GoodmansERBayes

from matplotlib.pyplot import savefig, close

# Import my data
edu_data = pd.read_csv("board_of_edu_data_clean.csv")
reg_data = pd.read_csv("reg_data_clean.csv")

# Edu candidates are Gidget Kidd, Gwen Williams, Melissa Calloway, Ryan Patton, Todd Dulaney
edu_candidates = edu_data["candidate_name"].unique()

# Get lists of precincts for edu election
edu_precincts = edu_data["precinct_name"].unique().tolist()

# Remove any precincts where the number of total votes was 0
edu_precincts = list(filter(lambda precinct:
                             sum(edu_data[edu_data["precinct_name"] == precinct]["vote_ct"].values) != 0,
                               edu_precincts))

## Run ER for board of education election
# Get total votes by precinct from reg data
total_reg_votes = np.array(list(map(lambda precinct:
                               sum(reg_data[reg_data["precinct_name"] == precinct]["total_voters"].values),
                                 edu_precincts)))

# Calculate percentage of black voters by precinct
black_voter_data = reg_data[reg_data["race_code"] == "B"]
black_voter_percent = np.array(list(map(lambda precinct, total_votes: # get number of black voters then divide by total voters in precinct
    sum(black_voter_data[black_voter_data["precinct_name"] == precinct]["total_voters"].values)/total_votes,
      edu_precincts, total_reg_votes))) 

# Calculate percentage of white voters by precinct
white_voter_data = reg_data[reg_data["race_code"] == "W"]
white_voter_percent = np.array(list(map(lambda precinct, total_votes: # get number of black voters then divide by total voters in precinct
    sum(white_voter_data[white_voter_data["precinct_name"] == precinct]["total_voters"].values)/total_votes,
      edu_precincts, total_reg_votes)))

# Calculate percentage of hispanic voters by precinct
hispanic_voter_data = reg_data[reg_data["ethnic_code"] == "HL"]
hispanic_voter_percent = np.array(list(map(lambda precinct, total_votes: # get number of black voters then divide by total voters in precinct
    sum(hispanic_voter_data[hispanic_voter_data["precinct_name"] == precinct]["total_voters"].values)/total_votes,
      edu_precincts, total_reg_votes))) 

# Run environmental reg for each candidate 
for candidate in edu_candidates:
    # Get a dataframe with only votes for the current candidate
    subdata = edu_data[edu_data["candidate_name"] == candidate]

    # Calculate the percent of the total vote the candidate got by precinct
    candidate_votes = np.array(list(map(lambda precinct:
                             sum(subdata[subdata["precinct_name"] == precinct]["vote_ct"].values)/ # Get the sum of votes from subdata
                             sum(edu_data[edu_data["precinct_name"] == precinct]["vote_ct"].values), # divide by sum of all votes in precinct
                               edu_precincts)))
    
    ## Run ER for black voters
    black_plot = GoodmansER()
    black_plot.fit(black_voter_percent,
                    candidate_votes,
                    demographic_group_name="black_voters",
                    candidate_name=candidate)

    # Print a summary of the results and plot the graph
    print(f"Board of EDU: {candidate} summary (Black Voters)")
    print(black_plot.summary())
    black_plot.plot(line_kws={"title": f"Board of EDU: {candidate} (Black Voters)"})
    # savefig(f"EDU_{candidate}_Black.png")
    close()


    ## Run ER for white voters
    white_plot = GoodmansER()
    white_plot.fit(white_voter_percent,
                    candidate_votes,
                    demographic_group_name="white_voters",
                    candidate_name=candidate)

    # Print a summary of the results and plot the graph
    print(f"Board of EDU: {candidate} summary (White Voters)")
    print(white_plot.summary())
    white_plot.plot(line_kws={"title": f"Board of EDU: {candidate} (White Voters)"})
    # savefig(f"EDU_{candidate}_White.png")
    close()

    ## Run ER for hispanic voters
    hispanic_plot = GoodmansER()
    hispanic_plot.fit(hispanic_voter_percent,
                    candidate_votes,
                    demographic_group_name="hispanic_voters",
                    candidate_name=candidate)
    
    # Print a summary of the results and plot the graph
    print(f"Board of EDU: {candidate} summary (Hispanic Voters)")
    print(hispanic_plot.summary())
    hispanic_plot.plot(line_kws={"title": f"Board of EDU: {candidate} (Hispanic Voters)"})
    # savefig(f"EDU_{candidate}_Hispanic.png")
    close()


## Run ER for Council election
# import council data
council_data = pd.read_csv("council_data_clean.csv")

# Get a list of candidates for the council election
council_candidates = council_data["candidate_name"].unique()

# Get a list of precincts with votes > 0 for the council election
council_precincts = council_data["precinct_name"].unique().tolist()
council_precincts = list(filter(lambda precinct:
                             sum(council_data[council_data["precinct_name"] == precinct]["vote_ct"].values) != 0,
                               council_precincts))

## Run ER for council election
# Get total votes by precinct from reg data
total_reg_votes = np.array(list(map(lambda precinct:
                               sum(reg_data[reg_data["precinct_name"] == precinct]["total_voters"].values),
                                 council_precincts)))

# Calculate percentage of black voters by precinct
black_voter_data = reg_data[reg_data["race_code"] == "B"]
black_voter_percent = np.array(list(map(lambda precinct, total_votes: # get number of black voters then divide by total voters in precinct
    sum(black_voter_data[black_voter_data["precinct_name"] == precinct]["total_voters"].values)/total_votes,
      council_precincts, total_reg_votes))) 

# Calculate percentage of white voters by precinct
white_voter_data = reg_data[reg_data["race_code"] == "W"]
white_voter_percent = np.array(list(map(lambda precinct, total_votes: # get number of black voters then divide by total voters in precinct
    sum(white_voter_data[white_voter_data["precinct_name"] == precinct]["total_voters"].values)/total_votes,
      council_precincts, total_reg_votes)))

# Calculate percentage of hispanic voters by precinct
hispanic_voter_data = reg_data[reg_data["ethnic_code"] == "HL"]
hispanic_voter_percent = np.array(list(map(lambda precinct, total_votes: # get number of black voters then divide by total voters in precinct
    sum(hispanic_voter_data[hispanic_voter_data["precinct_name"] == precinct]["total_voters"].values)/total_votes,
      council_precincts, total_reg_votes)))

# Run environmental reg for each candidate 
for candidate in council_candidates:
    # Get a dataframe with only votes for the current candidate
    subdata = council_data[council_data["candidate_name"] == candidate]

    # Calculate the percent of the total vote the candidate got by precinct
    candidate_votes = np.array(list(map(lambda precinct:
                             sum(subdata[subdata["precinct_name"] == precinct]["vote_ct"].values)/ # Get the sum of votes from subdata
                             sum(council_data[council_data["precinct_name"] == precinct]["vote_ct"].values), # divide by sum of all votes in precinct
                               council_precincts)))
    
    ## Run ER for black voters
    black_plot = GoodmansER()
    black_plot.fit(black_voter_percent,
                    candidate_votes,
                    demographic_group_name="black_voters",
                    candidate_name=candidate)

    # Print a summary of the results and plot the graph
    print(f"City Council: {candidate} summary (Black Voters)")
    print(black_plot.summary())
    black_plot.plot(line_kws={"title": f"City Council: {candidate} (Black Voters)"})
    # savefig(f"Council_{candidate}_Black.png")
    close()

    ## Run ER for white voters
    white_plot = GoodmansER()
    white_plot.fit(white_voter_percent,
                    candidate_votes,
                    demographic_group_name="white_voters",
                    candidate_name=candidate)

    # Print a summary of the results and plot the graph
    print(f"City Council: {candidate} summary (White Voters)")
    print(white_plot.summary())
    white_plot.plot(line_kws={"title": f"City Council: {candidate} (White Voters)"})
    # savefig(f"Council_{candidate}_White.png")
    close()

    ## Run ER for hispanic voters
    hispanic_plot = GoodmansER()
    hispanic_plot.fit(hispanic_voter_percent,
                    candidate_votes,
                    demographic_group_name="hispanic_voters",
                    candidate_name=candidate)
    
    # Print a summary of the results and plot the graph
    print(f"City Council: {candidate} summary (Hispanic Voters)")
    print(hispanic_plot.summary())
    hispanic_plot.plot(line_kws={"title": f"City Council: {candidate} (Hispanic Voters)"})
    # savefig(f"Council_{candidate}_Hispanic.png")
    close()


