import pandas as pd 
from scipy.stats import trim_mean
import numpy as np
import wquantiles

state = pd.read_csv("data/state.csv")

print(state.head())
print("\n")

print(f"Mean population: {state['Population'].mean()}")
print(f"Trim mean population: {trim_mean(state['Population'], 0.1)}")
print(f"Median of the populaton: {state['Population'].median()}")

print(f"Weighted average of the murder rate by population: {np.average(state['Murder.Rate'], weights=state['Population'])}")
print(f"Weighted median: {wquantiles.median(state['Murder.Rate'], weights=state['Population'])}")
