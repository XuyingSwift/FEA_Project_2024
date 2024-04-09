
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Data
# functions = ["Ackley", "Brown", "Dixon & Price", "Griewank", "PowellSingular", "PowellSingular2", 
#              "PowellSum", "QingFunction", "QuarticFunction", "Rastrigin", "Rosenbrock", 
#              "Salomon", "Schwefel", "Schwefel.1.2", "Schwefel.2.20", "Sphere", "Stepint", "SumSquares", "Zakharov"]

# dim10 = [2.18e-14, 4.83e-39, 1.13e-4, 0.022, 0.0024, 7.54e-27, 8.04e-44, 0.0006, 0.945, 0.0, 3.76, 0.40, 2.79e-38, 0.0, -1000.0, 1.47e-41, -25, 5.94e-39, 99.27]
# dim30 = [3.24e-14, 6.59e-41, 2.38e-4, 0.0, 0.0259, 4.19e-33, 2.57e-22, 0.152, 0.043, 2.27e-13, 25.34, 2.60, 1.55e-38, 0.0, -3000.0, 1.44e-40, -125, 6.01e-39, 723.27]
# dim50 = [8.57e-14, 2.53e-42, 3.18e-5, 0.0, 0.0128, 5.93e-33, 3.82e-23, 0.371, 0.324, 5.68e-13, 141.09, 3.30, 3.66e-41, 0.0, -5000.0, 4.76e-43, 225, 3.52e-42, 944.73]

df = pd.read_csv("/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Analysis/Autoencoder_Experiment_Results.csv")

functions = df.iloc[:, 0]  # First column for function names
dim10 = df.iloc[:, 1]      # Second column for dim10
dim30 = df.iloc[:, 2]      # Third column for dim30
dim50 = df.iloc[:, 3]      # Fourth column for dim50

# Calculate the maximum positive variation across dimensions for each function
max_positive_variations = [max(dim10[i], dim30[i], dim50[i]) for i in range(len(functions))]

# Calculate the maximum negative variation across dimensions for each function
max_negative_variations = [min(dim10[i], dim30[i], dim50[i]) for i in range(len(functions))]

# Find the function with the maximum positive variation
max_positive_variating_function = functions[np.argmax(max_positive_variations)]

# Find the function with the maximum negative variation
max_negative_variating_function = functions[np.argmin(max_negative_variations)]

# Find the dimension where the maximum positive variation occurs
max_positive_variation_dim = np.argmax(max_positive_variations)

# Find the dimension where the maximum negative variation occurs
max_negative_variation_dim = np.argmin(max_negative_variations)

# Plotting
plt.figure(figsize=(12, 6))

for i in range(len(functions)):
    plt.plot([10, 30, 50], [dim10[i], dim30[i], dim50[i]], label=functions[i])

# Annotate the line with the function that varies the most positively
plt.annotate(f'Max Positive Variation: {max_positive_variating_function}', (50, dim50[max_positive_variation_dim]), xytext=(30, dim50[max_positive_variation_dim] * 1.1),
             arrowprops=dict(arrowstyle='->'))

# Annotate the line with the function that varies the most negatively
plt.annotate(f'Max Negative Variation: {max_negative_variating_function}', (50, dim50[max_negative_variation_dim]), xytext=(30, dim50[max_negative_variation_dim] * 0.9),
             arrowprops=dict(arrowstyle='->'))

plt.xlabel('Dimension')
plt.ylabel('Function Value')
plt.title('Function Performance vs. Dimension')
plt.legend(loc='best')
plt.grid(True)

# Set the DPI (e.g., 300 for high resolution)
plt.savefig('function_performance.png', dpi=300)

plt.show()
