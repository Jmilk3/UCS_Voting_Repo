import pandas as pd
from pathlib import Path

# Open one of the voting files

with open(Path(__file__ + "/../../Election_Data_Sheets/csv/filename").resolve()) as file:
    data = pd.read_csv(file)
