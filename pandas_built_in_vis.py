import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv(
    'Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df1',
    index_col = 0)
df2 = pd.read_csv(
    'Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df2')
print(df1.head())
print(df1.index)
# df1['A'].hist(bins = 30)
# df1['A'].plot(kind = 'hist', bins = 30)
# df2.plot.area(alpha= 0.4)
# df2.plot.bar(stacked = True)
# df1['A'].plot.hist(bins = 50)
# df1.plot.line(y = 'B', figsize = (12, 3), lw = 0.5)
# df1.plot.scatter(x = 'A', y = 'B', s=df1['C']*100, cmap = 'coolwarm', edgecolors='#000')
# df2.plot.box()
df = pd.DataFrame(np.random.randn(1000, 2), columns = ['a', 'b'])
# df.plot.hexbin(x = 'a', y = 'b', gridsize = 25, cmap = 'coolwarm')
# df.plot.kde()
df2.plot.density()
plt.show()
