import os
from analyze_main import get_best_performance
from analyze_main import get_performance_list

def main():
    # Specify the directory path you want to loop through
    directory_path = '/Users/xuyingwangswift/Desktop/FEA_PCA_AUTOENCODER/src/Results/PCA_abs_dim50'
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    # Sort the files by the first letter of their filenames
    sorted_files = sorted(files, key=lambda x: x[0].lower())
    # Loop through each file in the directory
    # Now, sorted_files contains the filenames sorted by their first letter
    for filename in sorted_files:
        file_path = os.path.join(directory_path, filename)
    
            # Check if the item in the directory is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # Get the first letter of the filename (assuming filenames are not empty)
            first_letter = filename[0].lower()
            
            # Process the file if its first letter matches your criteria
            if 'a' <= first_letter <= 'z':

                list = get_performance_list(file_path)
                best = get_best_performance(list)
                print("file name", filename)
                print("best fit: ", best)
                print()
                    
            # You can perform any file-specific operations here

    # You can also add additional directory-specific operations here
#main()

def fac():
        # Defining the list of factors
    factors =  [[2, 13, 20, 23, 24, 30, 37], [11, 32], [0, 8, 21, 22, 36], [6, 24, 26, 27, 30, 41, 47], [7, 12, 20, 23, 27, 40, 48], [27], [3, 30, 47, 49], 
                [4, 8, 12, 15, 26, 33, 40], [2, 7, 11, 15, 26, 33, 35, 36, 38], [10, 14, 17, 20, 29], [9, 17, 20, 22, 25, 28, 30, 39, 44], 
                [1, 8, 26, 32, 38, 49], [4, 7, 30, 40, 43, 49], [0, 18, 24, 26, 27, 30, 37, 42, 46], [9, 29], [7, 8, 26, 33], [35], [
                    9, 10, 20, 21, 23, 28, 29, 32, 33, 34, 36, 44], [13, 19, 26, 27, 42], [18], [0, 4, 9, 10, 17, 23, 27], [2, 17, 22, 29, 34], 
                    [2, 10, 21, 25], [0, 4, 17, 20, 28, 32, 33, 36, 48], [0, 3, 13, 27, 30, 37, 41, 45], [10, 22, 30, 39, 44], [3, 7, 8, 11, 13, 15, 18, 27, 33, 38, 42, 47], 
                    [3, 4, 5, 13, 18, 20, 24, 26, 41, 42], [10, 17, 23, 34, 44], [9, 14, 17, 21, 34], [0, 3, 6, 10, 12, 13, 24, 25, 37, 39, 44], [32, 45, 47], 
                    [1, 11, 17, 23, 31, 33, 36], [7, 8, 15, 17, 23, 26, 32, 36], [17, 21, 28, 29, 44], [8, 16], [2, 8, 17, 23, 32, 33, 41], [0, 13, 24, 30, 43], [8, 11, 26], 
                    [10, 25, 30, 44], [4, 7, 12], [3, 24, 27, 36], [13, 18, 26, 27], [12, 37], [10, 17, 25, 28, 30, 34, 39], [24, 31, 47], [13], [3, 6, 26, 31, 45, 49], [4, 23], 
                    [6, 11, 12, 47]]


    # Calculating the average size of sublists
    average_size = sum(len(sublist) for sublist in factors) / len(factors)

    # Outputting the result
    print(average_size)

fac()