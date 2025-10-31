# Primary test runner file with CLI interface
# Classes that store testing data in a consistent format
from bloc import Bloc 
from test import Test

# VoteKit data classes and elections
from votekit.elections import IRV, Plurality, STV
from votekit import PreferenceInterval

# Function that runs PL, BT, and Cambridge ballot generators
from ballot_generators import generateAll

# IO libraries
import argparse
from pathlib import Path
import tabulate

# For now, test definitions can go here
# If we want to seperate them out, we can place the tests in a different file then import them

# This is the list of tests that the test runner can see. Be sure to add any new tests here
test_list = []

def main(args):
    """
    Main test running function. Handles flag parsing and main interaction loop.
    """
    output_path = Path(__file__ + f"/../../Results").resolve() # Path to Results folder

    # Handle run all tests flag
    if (args.a):
        for test in test_list:
            runTest(test, output_path / args.filename, args.n)
    
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
                runTest(test_list[index], output_path / args.filename, args.n)
            else:
                print("Invalid index")
                continue
        # Resolve name input
        else:
            if selection in test_names:
                runTest(test[test_names.index(selection)], output_path / args.filename, args.n)
            else:
                print("Invalid test name")
                continue
        

    
    

def runTest(test, output_path, num_tests):
    """Helper function that runs a given test n times and prints the results to the output file"""
    # Turn the blocs into generator inputs
    generator_inputs = Bloc.outputVars(test.bloc1, test.bloc2, test.num_ballots)

    # Generate ballots and run elections on them num_tests times, outputting results as we go
    with open(output_path, "+a", encoding="utf-8-sig") as file:
        for i in range(0, num_tests):
            ballots = generateAll(generator_inputs) # I am not currently storing every ballot, since that would take up way too much space
            
            # Run the elections using the 3 ballot sets
            plurality_results = [Plurality(ballots[0], test.num_seats), Plurality(ballots[1], test.num_seats), Plurality(ballots[2], test.num_seats)]
            stv_results = [STV(ballots[0], test.num_seats), STV(ballots[1], test.num_seats), STV(ballots[2], test.num_seats)]

            # Print the winners TODO: Update this to reflect whatever results we actually want
            for results in plurality_results:
                winners = []

                # Elected candidates are stored in a tuple of frozensets, so we extract them to winners
                for cold_set in results.get_elected():
                    for candidate in cold_set:
                        winners.append(candidate)

                # Output the winning candidates TODO: Decide on output format
            
            # TODO: Make a loop that does the STV results
    
    # TODO: Decide on whether or not we want to do data analysis while the tests are running
    # We could just output everything and analyze later


    
if __name__ == "__main__":
    # Parse CLI arguments and pass them to main
    parser = argparse.ArgumentParser(prog="test_runner",
                                      description="Interface for running voting tests." \
                                      " By default, lists available tests and asks user to input desired test.")
    parser.add_argument("filename", type=str, help="The filename where test results will be stored. It should be a csv file")
    parser.add_argument("--number","-n", default=1, type=int, help="The number of times each test should be run. Defaults to 1.")
    parser.add_argument("--all", "-a", action="store_true", help="If this flag is set, the program will run all tests then exit.")
    args = parser.parse_args()

    main(args)