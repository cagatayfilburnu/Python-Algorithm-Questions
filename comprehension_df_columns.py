import seaborn as sns
df = sns.load_dataset("car_crashes")

print(df.columns)

# First Question
# With List Comprehension, use upper() on column names and add "NUM_" to variables that are numeric ones.
df1 = ["NUM_" + col.upper() if df[col].dtype == float else col.upper() for col in df.columns]

# Second Question
# With List Comprehension, use upper() on column names and add "_FLAG" to variables that do not include "NO".
df2 = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]