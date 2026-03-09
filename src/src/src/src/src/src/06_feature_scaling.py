from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

X = df.drop("Compressive_Strength_MPa", axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Scaled Features Shape:", X_scaled.shape)
