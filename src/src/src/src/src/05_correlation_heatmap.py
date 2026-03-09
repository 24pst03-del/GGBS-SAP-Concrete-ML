import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/ggbs_sap_concrete_dataset_500_github_ready.csv")

sns.heatmap(df.corr(), annot=True)
plt.show()
