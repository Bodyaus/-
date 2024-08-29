import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sss.csv")
df.index = [1,2,3,4,5,6,7]
df["price"].plot(kind = "hist")


plt.show()