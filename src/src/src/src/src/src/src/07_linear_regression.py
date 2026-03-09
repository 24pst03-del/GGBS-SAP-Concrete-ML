from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

X = df.drop("Compressive_Strength_MPa", axis=1)
y = df["Compressive_Strength_MPa"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)

print("Model trained successfully")
