import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv("ign.csv")

pc_reviews = reviews[reviews["platform"] == "PC"]["score"]
pc_reviews.plot(kind="hist")
plt.show()
