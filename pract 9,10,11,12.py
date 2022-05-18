import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/demo1.csv')
df

col=["math score","reading score","writing score","placement score"]
df.boxplot(col)

fig,ax=plt.subplots(figsize = (18,10))
ax.scatter(df['placement score'], df['placement offer count'])
plt.show()

from scipy import stats

z = np.abs(stats.zscore(df['math score']))
print(z)

threshold = 1.09
sample_outliers = np.where(z<threshold)
sample_outliers

sorted_rscore = sorted(df['reading score'])
sorted_rscore

q1 = np.percentile(sorted_rscore, 25)
q3 = np.percentile(sorted_rscore, 75)
print(q1,q3)

IQR = q3-q1

lwr_bound = q1-(1.5*IQR)
upr_bound = q3+(1.5*IQR)

print(lwr_bound, upr_bound)

r_outlier = []
for i in sorted_rscore:
  if(i<lwr_bound or i>upr_bound):
    r_outlier.append(i)
print(r_outlier)

