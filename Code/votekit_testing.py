import votekit as vk
import pathlib
import pandas as pd

with open(pathlib.Path("../Election_Data_Sheets/results_pct_20220517.txt").resolve()) as file:
    frame = pd.read_csv(file, sep="\t")
