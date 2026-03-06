# Primary simulation runner file with CLI interface
# Classes that store simulation data in a consistent format
from definitions.structures.bloc import Bloc 
from definitions.structures.sim_params import SimParams

# VoteKit data classes and elections
from votekit.elections import Plurality, STV
from votekit.pref_profile.pref_profile import RankProfile, ProfileError
from votekit.ballot_generator import BlocSlateConfig
from votekit.pref_interval import PreferenceInterval
# import csv for ballot writer function
import csv

# Function that runs PL, BT, and Cambridge ballot generators
from definitions.structures.ballot_generators import generateAll

# IO libraries
import argparse
from pathlib import Path
import tabulate

# Random for selecting within confidence interval
from random import uniform

# For now, sim definitions can go here
# Update this to actually import the definitions
import definitions.asheboro_sims as ashe
import definitions.smithfield_sims as smith
import definitions.charlotte_sims as char

# Create a list for each of the cities
ashe_list = ashe.BoE_List + ashe.Council_List
smith_list = smith.Mayor_List + smith.Council_List
char_list = char.BoE_List + char.Council_List + char.Mayor_List

# Change the sim list to include all of the sims from the definition files
# This is the list of sims that the sim runner can see. Be sure to add any new sims here
sim_list = ashe_list + smith_list + char_list



def main(args):
    """
    Main sim running function. Handles flag parsing and main interaction loop.
    """
    output_path = Path(__file__ + f"/../../../Simulation_Results").resolve() # Path to Results folder

    # Handle run all sims flag
    if (args.all):
        print(f"Running {len(sim_list)} sims:")
        for sim in sim_list:
            runSim(sim, output_path, args.filename, args.number)
            print('    ' + sim.sim_name + " Done!")
        return
    
    # Handle city input
    match args.city.lower():
        case "asheboro":
            # run contents of ashe_list
            print(f"Running {len(ashe_list)} sims:")
            for sim in ashe_list:
                runSim(sim, output_path, args.filename, args.number)
                print('    ' + sim.sim_name + " Done!")
            return
        case "smithfield":
            # run contents of smith_list
            print(f"Running {len(smith_list)} sims:")
            for sim in smith_list:
                runSim(sim, output_path, args.filename, args.number)
                print('    ' + sim.sim_name + " Done!")
            return
        case "charlotte":
            # run contents of char_list
            print(f"Running {len(char_list)} sims:")
            for sim in char_list:
               runSim(sim, output_path, args.filename, args.number)
               print('    ' + sim.sim_name + " Done!")
            return
        case _:
            pass
    
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
    config_inputs = Bloc.outputVars([sim.bloc1, sim.bloc2], sim.num_ballots)

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
        candidates = []
        for key in config_inputs[4].keys():
            candidates += config_inputs[1][key]
        candidates.sort()
        
        # Store the ballots which appear in each iteration in the order PL, BT, Cam
        ballot_data = [{}, {}, {}]

        # Print a status update to terminal
        print(f"    Now Running {sim.sim_name}")

        # Generate ballots and run elections on them num_sims times, outputting results as we go
        for i in range(0, num_sims):
            # Create a preference mapping by sampling from ranges in config_inputs
            prefs = config_inputs[3]
            sampled_pref_mapping = {prefs[0]: {}, prefs[2]: {}}

            # loop through bloc 1 mappings and get values
            for key in prefs[1].keys():
                current = {} # create a dict for each bloc
                for candidate in prefs[1][key]:
                    # Set candidate value to random value in its given range
                    current[candidate] = uniform(prefs[1][key][candidate][0], prefs[1][key][candidate][1])
                # Add preference interval to mapping
                sampled_pref_mapping[prefs[0]][key] = PreferenceInterval(current)
            
            # loop through bloc 2 mappings and get values
            for key in prefs[3].keys():
                current = {} # create a dict for each bloc
                for candidate in prefs[3][key]:
                    # Set candidate value to random value in its given range
                    current[candidate] = uniform(prefs[3][key][candidate][0], prefs[3][key][candidate][1])
                # Add preference interval to mapping
                sampled_pref_mapping[prefs[2]][key] = PreferenceInterval(current)

           # Create preference intervals for each bloc
            # Create the blocSlateConfig for this iteration
            generator_config = BlocSlateConfig(n_voters=config_inputs[0],
                                               slate_to_candidates=config_inputs[1],
                                               bloc_proportions=config_inputs[2],
                                               preference_mapping=sampled_pref_mapping,
                                               cohesion_mapping=config_inputs[4])

            # Generate ballots in order PL, BT, Cam
            ballots = generateAll(generator_config)

            # Add the ballots to their respective dictionaries
            for j in range(3):
                # iterate through the tuple of ballots
                for ballot in ballots[j].ballots:
                    # Get the ranking from the ballot
                    ranking = ""
                    for fset in ballot.ranking:
                        ranking += list(fset)[0]
                        ranking += ","
                    ranking = ranking[:-1] # remove spare comma at end

                    # Add ranking to dictionary if needed
                    if ranking not in ballot_data[j]:
                        ballot_data[j][ranking] = [0.0] * num_sims
                    
                    # Set ballot weight in column corresponding to current iteration
                    ballot_data[j][ranking][i] = ballot.weight
            
            # Run the elections using the 3 ballot sets
            plurality_results = [Plurality(ballots[0], sim.num_seats, "borda"),
                                  Plurality(ballots[1], sim.num_seats, "borda"),
                                  Plurality(ballots[2], sim.num_seats, "borda")]
            stv_results = [STV(ballots[0], sim.num_seats, tiebreak="borda"),
                            STV(ballots[1], sim.num_seats, tiebreak="borda"),
                            STV(ballots[2], sim.num_seats, tiebreak="borda")]

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


    ## Write the ballots to output file
    # Create shared header and lables
    labels = ["ranking"] + [f"iteration_{i}" for i in range(1, num_sims + 1)]

    # Write PL results
    with open(output_path / f"Ballots" / f"{filename}_{sim.sim_name}_ballots_PL.csv", "+a", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Add header and lables if file is currently empty
        if file.tell() == 0:
            writer.writerows([labels])
        
        # Write a row for each ballot with the weights from each iteration
        for ballot in ballot_data[0].keys():
            writer.writerow([ballot] + ballot_data[0][ballot])

    # Write BT results
    with open(output_path / f"Ballots" / f"{filename}_{sim.sim_name}_ballots_BT.csv", "+a", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Add header and lables if file is currently empty
        if file.tell() == 0:
            writer.writerows([labels])
        
        # Write a row for each ballot with the weights from each iteration
        for ballot in ballot_data[1].keys():
            writer.writerow([ballot] + ballot_data[1][ballot])

    # Write cambridge results
    with open(output_path / f"Ballots" / f"{filename}_{sim.sim_name}_ballots_Cam.csv", "+a", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Add header and lables if file is currently empty
        if file.tell() == 0:
            writer.writerows([labels])
        
        # Write a row for each ballot with the weights from each iteration
        for ballot in ballot_data[2].keys():
            writer.writerow([ballot + "," * (len(candidates) - len(ballot.split(",")))] + ballot_data[2][ballot])

if __name__ == "__main__":
    # Parse CLI arguments and pass them to main
    parser = argparse.ArgumentParser(prog="sim_runner",
                                      description="Interface for running voting simulations." \
                                      " By default, lists available simulations and asks user to select the desired one.")
    parser.add_argument("filename", type=str, help="The filename will be used to distinguish the output files from previous results.")
    parser.add_argument("--number","-n", default=1, type=int, help="The number of times each simulation should be run. Defaults to 1.")
    parser.add_argument("--all", "-a", action="store_true", help="If this flag is set, the program will run all simulations then exit.")
    parser.add_argument("--city", type=str, default="", help="Pass a city name to run all simulations from that city")

    args = parser.parse_args()
    print(args)

    main(args)