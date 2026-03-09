import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

X = df.drop("Compressive_Strength_MPa", axis=1)
y = df["Compressive_Strength_MPa"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = Sequential()

model.add(Dense(16,input_dim=X.shape[1],activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1))

model.compile(loss='mse',optimizer='adam')

model.fit(X_train,y_train,epochs=50,batch_size=10)

print("ANN Model Trained")
