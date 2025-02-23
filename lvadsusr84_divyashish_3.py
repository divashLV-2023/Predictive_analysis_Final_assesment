# -*- coding: utf-8 -*-
"""LVADSUSR84_Divyashish 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q2Y2YpNLBXo3UttJMW5F5a2N_i0WFU3u
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch4-Assessment/main/seeds.csv")
data.tail()

data.info()

data.describe()

data.isnull().sum()

data.fillna(data.mean(), inplace=True)

data.isnull().sum()

data.shape

data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

sns.pairplot(data, diag_kind='kde')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='Pastel2', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

data['Cluster'] = clusters

inertia_values = []
silhouette_scores = []
k_values = range(2, 10)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, kmeans.labels_))

plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve for Optimal k')
plt.xticks(k_values)
plt.show()

plt.plot(k_values, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Optimal k')
plt.xticks(k_values)
plt.show()

optimal_k = 7
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(scaled_data)

cluster_labels = kmeans.predict(scaled_data)

silhouette_avg = silhouette_score(scaled_data, cluster_labels)
print("Average silhouette score: ",silhouette_avg)

data['Cluster'] = kmeans.labels_
cluster_profiles = data.groupby('Cluster').mean()
print(cluster_profiles)







