import argparse
from pathlib import Path
import csv
from os.path import basename

file_path = Path(__file__ + f"/../../../New_Simulation_Results").resolve()

for file in (file_path / "BoE_Ballots").iterdir():
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        with open((file_path / "Clean_BoE" / basename(file.name)), "w", encoding="utf-8", newline="") as outfile:
            print(outfile.name)
            writer = csv.writer(outfile)
            for line in reader:
                for i in range(0, len(line)):
                    if line[i] == "0.0":
                        line[i] = ""
                writer.writerow(line)
