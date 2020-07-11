import os

# read a file
# use with to close the file resource after use
if os.path.exists("fruits.txt"):
    with open("fruits.txt") as file:
        file_data = file.read()
        print(file_data)


# write to a file, "w" mode remove everything from file and write new content
with open("vegetables.txt", "w") as vegetables_file:
    vegetables_file.write("Spinach\n")
    vegetables_file.write("Lettuce")

# mode "a" opens the file in append mode to append data to existing file
with open("vegetables.txt", "a") as vegetables_file:
    vegetables_file.write("\nCauliflower")

# mode a+ opens the file in append and read more
with open("vegetables.txt", "a+") as vegetables_file:
    vegetables_file.write("\nOkra")
    # Seek move the cursor to location
    vegetables_file.seek(0)
    print(vegetables_file.read())

