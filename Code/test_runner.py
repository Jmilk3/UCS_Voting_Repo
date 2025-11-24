# Primary test runner file with CLI interface
# Classes that store testing data in a consistent format
from bloc import Bloc 
from test_params import TestParams

# VoteKit data classes and elections
from votekit.elections import Plurality, STV

# Function that runs PL, BT, and Cambridge ballot generators
from ballot_generators import generateAll

# IO libraries
import argparse
from pathlib import Path
import tabulate

# For now, test definitions can go here


# Make up some blocs
debug_bloc_1 = Bloc(name="Majority Bloc",
                     size=0.8,
                     candidates={"A","B","C"},
                     cohesion={"Majority Bloc":0.7, "Minority Bloc":0.3},
                     preference={"Majority Bloc": 0.5,
                                "Minority Bloc": 2})

debug_bloc_2 = Bloc(name="Minority Bloc",
                    size=0.2,
                    candidates={"D","E"},
                    cohesion={"Minority Bloc":0.9, "Majority Bloc":0.1},
                    preference={"Majority Bloc": 0.5,
                                "Minority Bloc": 2})

# Create several near-identical tests for debugging
debug_test_1 = TestParams("debug_test_1", debug_bloc_1, debug_bloc_2, 2, 1000)
debug_test_2 = TestParams("debug_test_2", debug_bloc_1, debug_bloc_2, 2, 1000)
debug_test_3 = TestParams("debug_test_3", debug_bloc_1, debug_bloc_2, 2, 1000)


# This is the list of tests that the test runner can see. Be sure to add any new tests here
test_list = [debug_test_1]

def main(args):
    """
    Main test running function. Handles flag parsing and main interaction loop.
    """
    output_path = Path(__file__ + f"/../../Results").resolve() # Path to Results folder

    # Handle run all tests flag
    if (args.all):
        print(f"Running {len(test_list)} tests:")
        for test in test_list:
            runTest(test, output_path, args.filename, args.number)
            print('    ' + test.test_name + " Done!")
        return
    
    # Main interaction loop
    print(tabulate.tabulate([[test.test_name] for test in test_list], tablefmt="pretty", showindex=True)) # Print available tests
    test_names = [test.test_name for test in test_list] # Get a list of names to resolve name inputs 
    print("Input quit or q to exit") # inform the user of how to exit the program
    while True:
        # Get the user input
        selection = input("Input the index or name of a test to run: ")

        # Check if the user wants to quit
        if (selection == "q" or selection == "quit"):
            break

        # Resolve index input
        if selection.isnumeric():
            index = int(selection)
            if index < len(test_list) and index >= 0:
                runTest(test_list[index], output_path, args.filename, args.number)
            else:
                print("Invalid index")
                continue
        # Resolve name input
        else:
            if selection in test_names:
                runTest(test_list[test_names.index(selection)], output_path, args.filename, args.number)
            else:
                print("Invalid test name")
                continue
        

    
    

def runTest(test, output_path, filename, num_tests):
    """Helper function that runs a given test n times and prints the results to the output file"""
    # Turn the blocs into generator inputs
    generator_inputs = Bloc.outputVars([test.bloc1, test.bloc2], test.num_ballots)

    # Open the output files for these tests before starting the loop
    with open(output_path / f"{filename}_{test.test_name}_PL.csv", "+a", encoding="utf-8-sig") as pl_file,\
          open(output_path / f"{filename}_{test.test_name}_BT.csv", "+a", encoding="utf-8-sig") as bt_file, \
          open(output_path / f"{filename}_{test.test_name}_Cam.csv", "+a", encoding="utf-8-sig") as cam_file:
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
        print(f"    Now Running {test.test_name}")

        # Generate ballots and run elections on them num_tests times, outputting results as we go
        for i in range(0, num_tests):
            # Generate ballots
            ballots = generateAll(generator_inputs) # I am not currently storing every ballot, since that would take up way too much space
            
            # Run the elections using the 3 ballot sets
            plurality_results = [Plurality(ballots[0], test.num_seats, "borda"), Plurality(ballots[1], test.num_seats, "borda"), Plurality(ballots[2], test.num_seats, "borda")]
            stv_results = [STV(ballots[0], test.num_seats, tiebreak="borda"), STV(ballots[1], test.num_seats, tiebreak="borda"), STV(ballots[2], test.num_seats, tiebreak="borda")]

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
            print(f"      {i+1}/{num_tests} iterations completed!")

            # Get a new preference profile for the next iteration
            # NOTE: I love the name of this function
            generator_inputs.resample_preference_intervals_from_dirichlet_alphas()


    
if __name__ == "__main__":
    # Parse CLI arguments and pass them to main
    parser = argparse.ArgumentParser(prog="test_runner",
                                      description="Interface for running voting tests." \
                                      " By default, lists available tests and asks user to input desired test.")
    parser.add_argument("filename", type=str, help="The filename will be used to distinguish the output files from previous results.")
    parser.add_argument("--number","-n", default=1, type=int, help="The number of times each test should be run. Defaults to 1.")
    parser.add_argument("--all", "-a", action="store_true", help="If this flag is set, the program will run all tests then exit.")
    args = parser.parse_args()
    print(args)

    main(args)