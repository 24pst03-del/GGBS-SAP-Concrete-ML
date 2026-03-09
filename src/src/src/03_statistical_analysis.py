import pandas as pd

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

print(df.describe())
print(df.mean())
print(df.std())
