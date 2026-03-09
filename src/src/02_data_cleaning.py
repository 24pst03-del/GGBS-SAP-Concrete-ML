import pandas as pd

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

print(df.isnull().sum())

df = df.drop_duplicates()

print("Cleaned Dataset Shape:", df.shape)
