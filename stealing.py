import os
import tkinter as tk
from tkinter import filedialog

def delete_files_in_folder(folder_path, search_term):
    deleted_count = 0  
    seen_files = set() 

    for filename in os.listdir(folder_path):
        
        if search_term in filename:
            
            file_path = os.path.join(folder_path, filename)

            if filename in seen_files:
                print(f"{filename} Has already been deleted.")
                continue  

            seen_files.add(filename) 
            try:
                os.remove(file_path)
                print(f"{filename} deleted.")
                deleted_count += 1  
            except Exception as e:
                print(f"{filename} Could not be deleted: {e}")
    
    return deleted_count

def main():
    print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠛⠛⠛⠛⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣼⣧⣤⣤⣤⣤⣼⣧⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⠛⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⢹⣿⣿⡏⢹⣿⣿⡏⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠘⣿⣿⡇⢸⣿⣿⠃⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀⣿⣿⡇⢸⣿⣿⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣿⣿⡇⢸⣿⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⢿⣿⡇⢸⣿⡿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆⢸⣿⡇⢸⣿⡇⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⡇⢸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣾⣿⣷⣾⣿⣷⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠉⠉authour⠉⠉⠀
         0_rhpositive

""")

    root = tk.Tk()
    root.withdraw()  

    folder_path = filedialog.askdirectory(title="Select the folder containing the files to be deleted")
    
    if not folder_path:
        folder_path = input("Enter the folder path containing the files to be deleted: ")

    while True:
        search_term = input("Enter a word to search in the file name to be deleted: ")

        deleted_count = delete_files_in_folder(folder_path, search_term)

        print(f"Total number of deleted files: {deleted_count}")

        if deleted_count == 0:
            print("The file to be deleted was not found. Please enter another word.")
        else:
            break  

    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
