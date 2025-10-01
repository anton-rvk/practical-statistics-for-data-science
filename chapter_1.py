import pandas as pd 
from scipy.stats import trim_mean
import numpy as np
import wquantiles
from statsmodels import robust

state = pd.read_csv("data/state.csv")

print(state.head())
print("\n")

print(f"Mean population: {state['Population'].mean()}")
print(f"Trim mean population: {trim_mean(state['Population'], 0.1)}")
print(f"Median of the populaton: {state['Population'].median()}")

print(f"Weighted average of the murder rate by population: {np.average(state['Murder.Rate'], weights=state['Population'])}")
print(f"Weighted median: {wquantiles.median(state['Murder.Rate'], weights=state['Population'])}")

print(f"STD: {state['Population'].std()}")
print(f"IQR: {state['Population'].quantile(0.75) - state['Population'].quantile(0.25)}")
print(f"MAD: {robust.scale.mad(state['Population'])}") #MAD is almost twice as small as STD since it's robust and not sensetive to outliers

### Exploring the distributions 

print(f"Percentiles of murder rate: {state['Murder.Rate'].quantile([0.05, 0.25, 0.5, 0.75, 0.95])}")

ax = (state['Population'] / 1_000_000).plot.box()
ax.set_ylabel('Population (millions)')