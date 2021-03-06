# Calculating Principal Components
# You'll visually inspect a 4 feature sample of the ANSUR dataset before and after PCA using Seaborn's pairplot(). This will allow you to inspect the pairwise correlations between the features.

# The data has been pre-loaded for you as ansur_df.

# Instructions 1/4
# 25 XP
# Create a Seaborn pairplot to inspect ansur_df.

# Instructions 2/4
# 25 XP
# Create the scaler and standardize the data.

# Instructions 3/4
# 25 XP
# Create the PCA() instance and fit and transform the standardized data.

# Instructions 4/4
# 25 XP
# Create a pairplot of the principal component dataframe.

# Instruction 1
# Create a pairplot to inspect ansur_df
# sns.pairplot(ansur_df)

# plt.show()

# # Instruction 2
# from sklearn.preprocessing import StandardScaler

# # Create the scaler and standardize the data
# scaler = StandardScaler()
# ansur_std = scaler.fit_transform(ansur_df)

# # Instruction 3
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA

# # Create the scaler and standardize the data
# scaler = StandardScaler()
# ansur_std = scaler.fit_transform(ansur_df)

# # Create the PCA instance and fit and transform the data with pca
# pca = PCA()
# pc = pca.fit_transform(ansur_std)

# # This changes the numpy array output back to a dataframe
# pc_df = pd.DataFrame(pc, columns=['PC 1', 'PC 2', 'PC 3', 'PC 4'])

# Instruction 4
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Create the scaler
scaler = StandardScaler()
ansur_std = scaler.fit_transform(ansur_df)

# Create the PCA instance and fit and transform the data with pca
pca = PCA()
pc = pca.fit_transform(ansur_std)
pc_df = pd.DataFrame(pc, columns=['PC 1', 'PC 2', 'PC 3', 'PC 4'])

# Create a pairplot of the principal component dataframe
sns.pairplot(pc_df)
plt.show()
