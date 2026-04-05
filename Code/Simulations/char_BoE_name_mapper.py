import argparse
from pathlib import Path
import csv
from os.path import basename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="name mapper",
                            description="replaces BoE candidate names or reverts them")
    parser.add_argument("--revert", action="store_true", help="Set if you want to revert files")
    args = parser.parse_args()
    file_path = Path(__file__ + f"/../../../New_Simulation_Results").resolve()

    if (args.revert):
        reverse_mapping = {"A":"Claire Covington","B":"Bill Fountain","C":"Brian Kasher","D":"Liz Monterrey",
            "E":"Monty Witherspoon","F":"Lenora Shipp","G":"Tigress Sydney Acute McDaniel",
            "H":"Annette Albright","I":"Clara Kennedy Witherspoon","J":"Michael Johnson",
            "K":"Omar Harris","L":"Peggy A. Capehart","M":"Juanrique Pallamente Hall","N":"Shamaiye Haynes","":""}
        for file in (file_path / "BoE_Ballots").iterdir():
            with open(file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader) #skip header
                with open((file_path / "Clean_BoE" / basename(file.name)), "w", encoding="utf-8", newline="") as outfile:
                    print(outfile.name)
                    writer = csv.writer(outfile)
                    for line in reader:
                        if line:
                            line[0] = ",".join(list(map(lambda x: reverse_mapping[x], line[0].split(","))))
                            writer.writerow(line)
    else:
        forward_mapping = {"Claire Covington":"A","Bill Fountain":"B","Brian Kasher":"C","Liz Monterrey":"D",
            "Monty Witherspoon":"E","Lenora Shipp":"F","Tigress Sydney Acute McDaniel":"G",
            "Annette Albright":"H","Clara Kennedy Witherspoon":"I","Michael Johnson":"J",
            "Omar Harris":"K","Peggy A. Capehart":"L","Juanrique Pallamente Hall":"M","Shamaiye Haynes":"N","":""}
        for file in (file_path / "BoE_Ballots").iterdir():
            with open(file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader) #skip header
                with open((file_path / "Clean_BoE" / basename(file.name)), "w", encoding="utf-8", newline="") as outfile:
                    print(outfile.name)
                    writer = csv.writer(outfile)
                    for line in reader:
                        if line:
                            line[1] = ",".join(list(map(lambda x: forward_mapping[x], line[1].split(","))))
                            writer.writerow(line)