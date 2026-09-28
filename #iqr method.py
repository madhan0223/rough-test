#iqr method
import pandas as pd
import numpy as np
import seaborn as sns
print(pd.__version__)

import matplotlib.pyplot as plt
print(sns.get_dataset_names())

# %% [markdown]
# percentile

# %%
df=np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])
q1=np.percentile(df,25)
q3=np.percentile(df,75)
print("q1:",q1)
print("q3:",q3)


# %% [markdown]
# calculate IQR

# %%
iqr=q3 - q1
print("iqr:",iqr)

# %% [markdown]
# find the lower and upper limit

# %%
lower=q1-1.5*iqr
upper=q3+1.5*iqr
print("lower:",lower)
print("upper:",upper)

# %% [markdown]
# find the ouliers

# %%
outliers=df[(df < lower) | (df > upper)]
count=len(outliers)
print(count)

# %% [markdown]
# OUTLIERS IN TIPS DATASET

# %%
import seaborn as sns

df = sns.load_dataset("tips")

# Q1 and Q3
Q1 = df["total_bill"].quantile(0.25)
Q3 = df["total_bill"].quantile(0.75)

# IQR
IQR = Q3 - Q1

# Lower and upper limits
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Find outliers
outliers = df[
    (df["total_bill"] < lower) |
    (df["total_bill"] > upper)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower limit:", lower)
print("Upper limit:", upper)

print("\nOutliers:")
print(outliers.head(10))


# %%
data=np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])
q1=np.percentile(data,25)
q2=np.percentile(data,75)
print("q1:",q1)
print("q2:",q2)
IQR=q2-q1
print("IQR:",IQR)
lower=q1-1.5*IQR
upper=q2+1.5*IQR
print("lower:",lower)
print("upper:",upper)
#outliers outside limit
outliers1=data[(data<lower )| (data > upper)]
print("Outliers:", outliers1)
print("Number of outliers:", np.size(outliers1))
# outliers with in this normal
outliers2=data[(data>=lower )& (data <= upper)]
print("normal value ",outliers2)
print("number of normal",np.size(outliers2))

# %%



