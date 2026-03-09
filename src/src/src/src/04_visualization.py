import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

df.hist(figsize=(10,8))
plt.show()
