# This file exists because charlotte's board of education is evil and has too many candidates to run math on
from pathlib import Path
from os.path import basename
import csv
from numpy import zeros

file_path = Path(__file__ + f"/../../../New_Simulation_Results").resolve()

for file in (file_path / "BoE_Ballots").iterdir():
    # I could make this nice and create a cli or something, but this is for a very specific task so nah
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header

        # Gather all unique data
        ballots = {}
        for line in reader:
            if (line):
                if line[1] not in ballots:
                    ballots[line[1]] = []
                ballots[line[1]].append([line[0], line[2]])

        with open((file_path / "Clean_BoE" / basename(file.name)), "w", encoding="utf-8", newline="") as outfile:
            print(outfile.name)
            # Write the header to the file
            writer = csv.writer(outfile)
            writer.writerow(["ranking"] + [f"iteration {i}" for i in range(1, 1001)])

            # For each unique ranking, scan the ballot file and set weights accordingly
            for rank in ballots.keys():
                # create a new output array
                output = [0.0] * 1000

                # fill output array
                for entry in ballots[rank]:
                    output[int(entry[0])] = entry[1]
            
                # Write output
                writer.writerow([rank] + output)


