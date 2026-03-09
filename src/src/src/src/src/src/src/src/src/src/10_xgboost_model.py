import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

X = df.drop("Compressive_Strength_MPa", axis=1)
y = df["Compressive_Strength_MPa"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = xgb.XGBRegressor()

model.fit(X_train,y_train)

print("XGBoost Model Trained")
