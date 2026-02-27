# Project 6: Automation Script (Real Power 🔥)
"""
Option A: File Organizer
Folder bhitra ko files
type anusar move:
.jpg → Images
.pdf → Docs
.txt → Texts
"""


def main():
    import os                   # for file and directory operations  
    import shutil               # for moving files

    folderPath = input("Enter the folder path to organize: ")
    if not os.path.isdir(folderPath):                                               # Check if the provided path is a valid directory where os.path is a module in the os library that provides functions for interacting with the operating system, and isdir is a function that checks if a given path is a directory. 
        print("Invalid folder path. Please enter a valid directory.")
        return
    
    for filename in os.listdir(folderPath):
        filePath = os.path.join(folderPath, filename)                               # os.path.join is used to create a full file path by combining the folder path and the filename. This ensures that the correct path is constructed regardless of the operating system being used.
        if os.path.isfile(filePath):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                destFolder = os.path.join(folderPath, 'Images')                     # os.path.join is used again to create the destination folder path by combining the original folder path with the new folder name ('Images' in this case). This ensures that the new folder is created in the same location as the original folder.
                os.makedirs(destFolder, exist_ok=True)                              # Create the destination folder if it doesn't exist  ani exit_ok=True is used to prevent an error if the folder already exists. If the folder already exists, it will simply continue without raising an exception.
                shutil.move(filePath, os.path.join(destFolder, filename))           # shutil.move is used to move the file from its original location (filePath) to the new location (os.path.join(destFolder, filename)). This effectively organizes the files based on their types.
            elif filename.endswith('.pdf'):
                destFolder = os.path.join(folderPath, 'Docs')
                os.makedirs(destFolder, exist_ok=True)
                shutil.move(filePath, os.path.join(destFolder, filename))
            elif filename.endswith('.txt'):
                destFolder = os.path.join(folderPath, 'Texts')
                os.makedirs(destFolder, exist_ok=True)
                shutil.move(filePath, os.path.join(destFolder, filename))
    print("Files organized successfully.")

if __name__ == "__main__":                  # This line checks if the script is being run directly (as the main program) rather than imported as a module in another script. If this condition is true, it will execute the code block that follows, which in this case is the call to the main() function. This is a common practice in Python to allow for modular code and to prevent certain code from running when the script is imported as a module.
    main()


