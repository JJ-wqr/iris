import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix
from mpl_toolkits.mplot3d import Axes3D
read_iris = pd.read_csv('iris.csv')
print(read_iris.head(5))
print(read_iris.isnull())
print(read_iris.head())
print("Number of Rows:", read_iris.shape[0])
print("Number of Columns:", read_iris.shape[1])
print("Missing Data Count:")
print(read_iris.isnull().sum())
numerical_features = read_iris.columns.drop('species')
fig, axs = plt.subplots(len(numerical_features), figsize=(10, 18))
for i, num_feature in enumerate(numerical_features):
    axs[i].hist(read_iris[num_feature], bins=20)
    axs[i].set_title(f'Histogram of Basic Visualization')
    axs[i].set_xlabel(num_feature)
    axs[i].set_ylabel('Frequency')
for i, num_feature in enumerate(numerical_features):
    axs[i].boxplot(read_iris[num_feature], vert=False)
    axs[i].set_title(f'Boxplot of {num_feature}')
fig2, axs2 = plt.subplots(1, len(numerical_features), figsize=(30, 10))
for i, num_feature in enumerate(numerical_features):
    axs2[i].boxplot([read_iris.loc[read_iris['species'] == s, num_feature] for s in read_iris['species'].unique()], 
                    labels=read_iris['species'].unique(), vert=False)
    axs2[i].set_title(f'Boxplot of {num_feature} by Species')
sns.pairplot(read_iris, hue='species', diag_kind='kde')
correlation = read_iris.drop('species', axis=1).corr()
mask = np.triu(np.ones_like(correlation, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(correlation, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".2f")
plt.figure(figsize=(8, 6))
sns.violinplot(x='species', y='sepal_length', data=read_iris, split=True)
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.title('Sepal Length Distribution by Species')
species_colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(read_iris['sepal_length'], read_iris['sepal_width'], read_iris['petal_length'], c=read_iris['species'].map(species_colors), cmap='viridis')
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
ax.set_title('3D Scatter Plot of Iris Features')
sns.set_style("whitegrid")
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
corr = read_iris.drop(columns=['species']).corr()
sns.heatmap(corr, annot=True, cmap="Greens", ax=axs[0])
axs[0].set_title("Correlation Heatmap")
most_correlated_pair = corr.unstack().sort_values(ascending=False).index[0]
feature1, feature2 = most_correlated_pair
sns.scatterplot(data=read_iris, x=feature1, y=feature2, hue="species", ax=axs[1])
axs[1].set_title(f"Scatterplot of {feature1} vs {feature2}")
sns.violinplot(data=read_iris, x="species", y="petal_length", ax=axs[2])
axs[2].set_title("Violin Plot of Petal Length by Species")
fig.tight_layout()
plt.show()


