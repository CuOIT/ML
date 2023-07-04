import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4,6],
    'B': [2, 4, 6, 8,9],
    'C': [3, 6, 9, 12, 15]
}

df = pd.DataFrame(data)

# Compute the correlation matrix
corr_matrix = df.corr()

print(corr_matrix)