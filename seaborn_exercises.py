import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic['fare'].max())
print(titanic[titanic['fare'] == 512.3292])
# sns.jointplot(x = 'fare', y = 'age', data = titanic)
# sns.displot(titanic['fare'], bins = 30)
# plt.xlim(0, 600)
# plt.ylim(0, 500)
# sns.boxplot(x = 'class', y = 'age', data = titanic)
# sns.swarmplot(x = 'class', y = 'age', data = titanic)
# sns.displot(titanic['sex'])
# tc = titanic.corr()
# sns.heatmap(tc, cmap = 'coolwarm')
# plt.title('titanci.corr()')
g = sns.FacetGrid(data = titanic, col = 'sex')
g.map(plt.hist, 'age')
plt.show()