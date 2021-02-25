import os
try:
    os.remove("my_first_file.txt")
    print("Deleted")
except:
    print("File already deleted!")