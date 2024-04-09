import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ackley_factors = [
                  [8, 17, 23, 29, 30, 34, 43], 
                  [9, 17, 19, 25, 26, 28, 30, 31, 32, 33, 47], 
                  [4, 7, 8, 15, 18, 26, 32, 36, 40, 43, 48], 
                  [4, 14, 36, 40, 41], 
                  [2, 3, 5, 12, 14, 15, 20, 23, 25, 32, 36, 40, 41, 46, 48, 49], 
                  [4, 49], 
                  [11, 25, 38, 39, 40, 48, 49], 
                  [2, 8, 12, 13, 14, 16, 26, 33, 35, 37, 38], 
                  [0, 2, 7, 17, 26, 29, 34, 38], 
                  [1, 19, 25, 30], 
                  [16, 22, 25, 28, 31, 33, 37, 39, 40, 41, 47], 
                  [6, 28, 38, 40, 49], 
                  [4, 7, 15, 16, 18, 25, 30, 35, 38, 43, 46], 
                  [7, 15, 18, 19, 21, 26, 42, 45, 46], 
                  [3, 4, 7, 20, 26, 33, 35, 36, 37, 40, 41, 43, 46], 
                  [2, 4, 12, 13, 18, 21, 32, 45, 46, 48], 
                  [7, 10, 12, 18, 19, 31, 33, 35, 38, 39, 47], 
                  [0, 1, 8, 27, 28, 29, 32, 33, 34, 47], 
                  [2, 12, 13, 15, 16, 19, 26, 33, 36, 39, 40, 42, 43, 45, 47], 
                  [1, 9, 13, 16, 18, 21, 24, 25, 26, 27, 30, 33, 39, 41, 42, 43], 
                  [4, 14, 46], 
                  [13, 15, 19, 22, 24, 26, 27, 32, 35, 38, 41, 43, 45, 46], 
                  [10, 21, 26, 37, 38, 41], 
                  [0, 4, 49], 
                  [19, 21, 27, 41, 43], 
                  [1, 4, 6, 9, 10, 12, 19, 30, 39], 
                  [1, 2, 7, 8, 13, 14, 18, 19, 21, 22, 30, 31, 38, 42, 43, 47], 
                  [17, 19, 21, 24, 28, 41, 43, 47], 
                  [1, 10, 11, 17, 27, 34, 38, 41, 42, 44, 47, 49], 
                  [0, 8, 17, 30, 34, 43], 
                  [0, 1, 9, 12, 19, 25, 26, 29, 31, 38, 43, 47], 
                  [1, 10, 16, 26, 30, 47], 
                  [1, 2, 4, 15, 17, 21, 33, 35, 48], 
                  [1, 7, 10, 14, 16, 17, 18, 19, 32, 37, 39, 40], 
                  [0, 8, 17, 28, 29, 42, 44], 
                  [7, 12, 14, 16, 21, 32, 38, 43], 
                  [2, 3, 4, 14, 18, 40, 41, 43], 
                  [7, 10, 14, 22, 33, 41, 46, 48], 
                  [6, 7, 8, 11, 12, 16, 21, 22, 26, 28, 30, 35, 40, 49], 
                  [6, 10, 16, 18, 19, 25, 33, 40, 48, 49], 
                  [2, 3, 4, 6, 10, 11, 14, 18, 33, 36, 38, 39, 41, 43, 44, 48, 49], 
                  [3, 4, 10, 14, 19, 21, 22, 24, 27, 28, 36, 37, 40, 43], 
                  [13, 18, 19, 26, 28, 34, 44], 
                  [0, 2, 12, 14, 18, 19, 21, 24, 26, 27, 29, 30, 35, 36, 40, 41, 45, 46], 
                  [28, 34, 40, 42], 
                  [13, 15, 18, 21, 43, 46, 47], 
                  [4, 12, 13, 14, 15, 20, 21, 37, 43, 45, 48], 
                  [1, 10, 16, 17, 18, 26, 27, 28, 30, 31, 45], 
                  [2, 4, 6, 15, 32, 37, 39, 40, 46, 49], 
                  [4, 5, 6, 11, 23, 28, 38, 39, 40, 48]
                ]

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

ackley_factors = [
    [8, 17, 23, 29, 30, 34, 43], 
    # ... (other factors)
    [4, 5, 6, 11, 23, 28, 38, 39, 40, 48]
]

# Create an empty similarity matrix
num_factors = len(ackley_factors)
similarity_matrix = np.zeros((num_factors, num_factors))

# Calculate Jaccard similarity between each pair of factors
for i in range(num_factors):
    for j in range(num_factors):
        if i != j:
            set1 = set(ackley_factors[i])
            set2 = set(ackley_factors[j])
            similarity_matrix[i][j] = jaccard_similarity(set1, set2)

# Display the similarity matrix
print("Jaccard Similarity Matrix:")
print(similarity_matrix)

# Your similarity_matrix should be defined here
# similarity_matrix = ...

# Set up the figure and axis
plt.figure(figsize=(10, 8))
sns.set(font_scale=1.2)  # Adjust the font size for better readability

# Create a heatmap using seaborn
ax = sns.heatmap(
    similarity_matrix,
    cmap="YlGnBu",  # Choose a color map
    annot=True,     # Show values in each cell
    fmt=".2f",      # Format of the cell values (two decimal places)
    linewidths=0.5, # Line width between cells
    square=True,    # Ensure a square aspect ratio
    xticklabels=False, # Disable x-axis labels
    yticklabels=False  # Disable y-axis labels
)

# Add a title
plt.title("Factor Overlap Heatmap")

# Show the heatmap
plt.show()
