try:
    with open("test_file.txt", "r") as file:
        print(file.readlines())
except:
    print("File not found or path is incorrect")
