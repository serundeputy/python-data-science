import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# Dist plot
# sns.displot(tips['total_bill'], kde = True, bins = 30)

# Joint plot
# sns.jointplot(x = 'total_bill',y = 'tip', data = tips, kind = 'scatter')

# Pair plot
# sns.pairplot(tips, hue='sex', palette='coolwarm')

# Rug plot
# sns.rugplot(tips['total_bill'])

# kde plots; Kernel Density Estimation
## notebooks/06-Data-Visualization-with-Seaborn/01-Distribution Plots.ipynb

# Categorical plots
# sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std)

# Count plot
# sns.countplot(x = 'sex', data = tips)

# Box plot
# sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')

# Violin plot
# sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex', split = True)

# Strip plot
# sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True, hue = 'sex', split = True)

# Swarm plot
#sns.violinplot(x = 'day', y = 'total_bill', data = tips)
#sns.swarmplot(x = 'day', y = 'total_bill', data = tips, color = 'black')

# Factor plot
# sns.factorplot(x = 'day', y = 'total_bill', data = tips, kind = 'violin')

# Matrix plots
# tc = tips.corr()
# sns.heatmap(tc, annot = True, cmap = 'coolwarm')
# fp = flights.pivot_table(index = 'month', columns = 'year', values = 'passengers')
# sns.heatmap(fp, cmap = 'magma', linecolor = 'white', linewidths = '1')
# sns.clustermap(fp, cmap = 'coolwarm', standard_scale = 1)

# Grids
# iris = sns.load_dataset('iris')
# g = sns.PairGrid(iris)
# g.map_diag(sns.histplot, kde = True)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot)

# Facet grid
# g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')
# g.map(plt.scatter, 'total_bill', 'tip')

# Regression plot
# sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', markers = ['o', 'v'], scatter_kws = {'s': 100})
# sns.lmplot(x = 'total_bill', y = 'tip', data = tips, col = 'day', hue = 'sex',
#         aspect = 0.6, size = 8)

# Styles
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', palette = 'seismic')
plt.show()
