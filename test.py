from matplotlib import pyplot as plt

import fastf1
from fastf1 import plotting

session_2024 = fastf1.get_session(2024, 24, "R")
session_2024.load()
laps_2024 = session_2024.laps[["Driver", "LapTime", "Sector1Time", "Sector2Time", "Sector3Time"]].copy()
laps_2024.dropna(inplace=True)

print(laps_2024.head())