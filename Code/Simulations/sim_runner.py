# Primary simulation runner file with CLI interface
# Classes that store simulation data in a consistent format
from definitions.structures.bloc import Bloc 
from definitions.structures.sim_params import SimParams

# VoteKit data classes and elections
from votekit.elections import Plurality, STV
from votekit.pref_profile.pref_profile import RankProfile, ProfileError
# import csv for ballot writer function
import csv

# Function that runs PL, BT, and Cambridge ballot generators
from definitions.structures.ballot_generators import generateAll

# IO libraries
import argparse
from pathlib import Path
import tabulate

# For now, sim definitions can go here
# TODO: Update this to actually import the definitions
import definitions.asheboro_sims as ashe
#import definitions.smithfield_sims as smith
#import definitions.charlotte_sims as char

# TODO: Change the sim list to include all of the sims from the definition files
# This is the list of sims that the sim runner can see. Be sure to add any new sims here
sim_list = ashe.BoE_Black + ashe.BoE_White

# TODO: Create a list for each of the cities
# ashe_list
# smith_list
# char_list

def main(args):
    """
    Main sim running function. Handles flag parsing and main interaction loop.
    """
    output_path = Path(__file__ + f"/../../../Results").resolve() # Path to Results folder

    # Handle run all sims flag
    if (args.all):
        print(f"Running {len(sim_list)} sims:")
        for sim in sim_list:
            runSim(sim, output_path, args.filename, args.number)
            print('    ' + sim.sim_name + " Done!")
        return
    
    # Main interaction loop
    print(tabulate.tabulate([[sim.sim_name] for sim in sim_list], tablefmt="pretty", showindex=True)) # Print available sims
    sim_names = [sim.sim_name for sim in sim_list] # Get a list of names to resolve name inputs 
    print("Input quit or q to exit") # inform the user of how to exit the program
    print("Input setn n to change the number of iterations to the number n")
    print("Input getn to see the current value of n")
    while True:
        # Get the user input
        selection = input("Input the index or name of a simulation to run: ")

        # Check if the user wants to quit
        if selection == "q" or selection == "quit":
            break

        # Check if user is changing n
        if selection.split() and selection.split()[0] == "setn" and len(selection) > 1:
            if selection.split()[1].isnumeric():
                args.number = int(selection.split()[1])
                print(f"Number of Iterations is now {args.number}")
                continue
            else:
                print("Invalid value for n")
                continue

        # Show n on request
        if selection == "getn":
            print(args.number)
            continue

        # Resolve index input
        if selection.isnumeric():
            index = int(selection)
            if index < len(sim_list) and index >= 0:
                runSim(sim_list[index], output_path, args.filename, args.number)
            else:
                print("Invalid index")
                continue
        
        # Resolve name input
        else:
            if selection in sim_names:
                runSim(sim_list[sim_names.index(selection)], output_path, args.filename, args.number)
            else:
                print("Invalid simulation name")
                continue
        

    
    

def runSim(sim, output_path, filename, num_sims):
    """Helper function that runs a given sim n times and prints the results to the output file"""
    # Turn the blocs into generator inputs
    generator_inputs = Bloc.outputVars([sim.bloc1, sim.bloc2], sim.num_ballots)

    # Open the output files for these sims before starting the loop
    with open(output_path / f"Elections" / f"{filename}_{sim.sim_name}_PL.csv", "+a", encoding="utf-8-sig") as pl_file,\
          open(output_path / f"Elections" / f"{filename}_{sim.sim_name}_BT.csv", "+a", encoding="utf-8-sig") as bt_file, \
          open(output_path / f"Elections" / f"{filename}_{sim.sim_name}_Cam.csv", "+a", encoding="utf-8-sig") as cam_file:
        # Create an array of file objects to make iteration easier
        files = [pl_file, bt_file, cam_file]

        # Check if the files are empty, and add a header line if they are
        for file in files:
            if file.tell() == 0:
                file.write("Candidate,Plurality Result,STV Result,Difference\n")

        # Store a sorted list of candidates to ensure consistent results ordering between runs
        candidates = generator_inputs.candidates
        candidates.sort()

        # Print a status update to terminal
        print(f"    Now Running {sim.sim_name}")

        # Generate ballots and run elections on them num_sims times, outputting results as we go
        for i in range(0, num_sims):
            # Generate ballots
            ballots = generateAll(generator_inputs)

            # Store the ballots for each iteration
            ballot_to_csv(ballots[0], output_path / f"Ballots" / f"{filename}_{sim.sim_name}_ballots_PL.csv", i)
            ballot_to_csv(ballots[1], output_path / f"Ballots" / f"{filename}_{sim.sim_name}_ballots_BT.csv", i)
            ballot_to_csv(ballots[2], output_path / f"Ballots" / f"{filename}_{sim.sim_name}_ballots_Cam.csv", i)
            
            # Run the elections using the 3 ballot sets
            plurality_results = [Plurality(ballots[0], sim.num_seats, "borda"), Plurality(ballots[1], sim.num_seats, "borda"), Plurality(ballots[2], sim.num_seats, "borda")]
            stv_results = [STV(ballots[0], sim.num_seats, tiebreak="borda"), STV(ballots[1], sim.num_seats, tiebreak="borda"), STV(ballots[2], sim.num_seats, tiebreak="borda")]

            # Output results for each set of ballots
            for j in range(3):
                plurality_winners = []
                stv_winners = []

                # Elected candidates are stored in a tuple of frozensets, so we extract them all into a list
                for cold_set in plurality_results[j].get_elected():
                    for candidate in cold_set:
                        plurality_winners.append(candidate)

                # Same thing as above but for STV results
                for cold_set in stv_results[j].get_elected():
                    for candidate in cold_set:
                        stv_winners.append(candidate)

                # Write a result line for each candidate
                for candidate in candidates:
                    # Get results from each election, check if they are the same
                    plurality_win = candidate in plurality_winners
                    stv_win = candidate in stv_winners
                    difference = plurality_win != stv_win

                    # Write the results to the output file
                    files[j].write(f"{candidate},{plurality_win},{stv_win},{difference}\n")

                # Add a gap between results for each iteration
                files[j].write(",,,\n")
            
            # Print a status update to terminal
            print(f"      {i+1}/{num_sims} iterations completed!")

            # Get a new preference profile for the next iteration
            # NOTE: I love the name of this function
            generator_inputs.resample_preference_intervals_from_dirichlet_alphas()

def ballot_to_csv(ballots:RankProfile,
        fpath: Path,
        iteration: int,
        include_voter_set: bool = False,
        weight_precision: int = 2,):
    """
    Saves PreferenceProfile to a custom CSV format based on the built-in Votekit method.

        Args:
            fpath (Path): Path to the saved csv.
            iteration (int): Current iteration value, used for determining if header should be included
            include_voter_set (bool, optional): Whether or not to include the voter set of each
                ballot. Defaults to False.
            weight_precision (int): Number of decimals to round float weights to. Defaults to 2.
        Raises:
            ProfileError: Cannot write a profile with no ballots to a csv.
            ValueError: File path must be provided.
    """
    if fpath == "":
            raise ValueError("File path must be provided.")

    if len(ballots.ballots) == 0:
        raise ProfileError("Cannot write a profile with no ballots to a csv.")
    
    prefix_idx = 1
    candidate_mapping = {c: c[:prefix_idx] for c in ballots.candidates}
    while len(set(candidate_mapping.values())) < len(candidate_mapping.values()):
        prefix_idx += 1
        candidate_mapping = {c: c[:prefix_idx] for c in ballots.candidates}

    data_col_names = ballots._RankProfile__to_rank_csv_data_column_names(
        include_voter_set, candidate_mapping
    )
    ballot_rows = [
        ballots._RankProfile__to_rank_csv_ballot_row(
            b, include_voter_set, candidate_mapping, weight_precision
        )
        for b in ballots.ballots
    ]

    # Only include header if this is the first iteration for this test.
    if iteration == 0:
        header = ballots._RankProfile__to_rank_csv_header(candidate_mapping, include_voter_set)
        rows = header + [data_col_names] + ballot_rows + [[""] * 10]
    else:
        rows = [data_col_names] + ballot_rows + [[""] * 10]

    # Write result to output file
    with open(
        str(fpath),
        "+a",
        newline="",
        encoding="utf-8",
    ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    
if __name__ == "__main__":
    # Parse CLI arguments and pass them to main
    parser = argparse.ArgumentParser(prog="sim_runner",
                                      description="Interface for running voting simulations." \
                                      " By default, lists available simulations and asks user to select the desired one.")
    parser.add_argument("filename", type=str, help="The filename will be used to distinguish the output files from previous results.")
    parser.add_argument("--number","-n", default=1, type=int, help="The number of times each simulation should be run. Defaults to 1.")
    parser.add_argument("--all", "-a", action="store_true", help="If this flag is set, the program will run all simulations then exit.")

    # TODO: Add a way to run each city list independently, for concurrency's sake

    args = parser.parse_args()
    print(args)

    main(args)