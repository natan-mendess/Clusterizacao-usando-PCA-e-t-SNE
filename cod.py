# Imports
import numpy as np # Algebra linear
import pandas as pd # Processar dataset
import matplotlib.pyplot as plt # Plotar gráfico
import seaborn as sns # Plotar heatmap
from sklearn.preprocessing import StandardScaler # Reescalar valores do dataset
from sklearn.decomposition import PCA
# Ler/tratar database
df = pd.read_csv("dataset.csv")
df['Target']=df['Target'].apply(lambda x: 1 if x=='Graduate' else 0)
scaler=StandardScaler()
scaled_data = scaler.fit_transform(df)
# PCA
pca=PCA(n_components=2, whiten=True)
pca.fit(scaled_data)

x_pca=pca.transform(scaled_data)
#Plotar gráfico
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0], x_pca[:,1], c=df['Target'],cmap='plasma')
plt.xlabel('Primeiro componente principal')
plt.ylabel('Segundo componente principal')
