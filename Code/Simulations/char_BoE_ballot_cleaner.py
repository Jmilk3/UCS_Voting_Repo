from pathlib import Path
from os.path import basename
import csv

file_path = Path(__file__ + f"/../../../New_Simulation_Results").resolve()

for file in (file_path / "BoE_Ballots").iterdir():
    # I could make this nice and create a cli or something, but this is for a very specific task so nah
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        with open((file_path / "Clean_BoE" / basename(file.name)), "w", encoding="utf-8", newline="") as outfile:
            print(outfile.name)
            writer = csv.writer(outfile)
            for line in reader:
                if line:
                    writer.writerow(line)

