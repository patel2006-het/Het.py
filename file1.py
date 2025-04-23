# Write a program to create a csv file that we can directly open in MS-Excel.
# Define the name of the CSV file
filename = "example.csv"

with open(filename, "w") as add:
    # Write the header row. Each value is separated by a comma.
    add.write("Name,Age,Occupation\n")
    
    # Write a few data rows.
    # The newline character (\n) indicates the end of each row.
    add.write("alpha,30,Engineer\n")
    add.write("Beta,25,Data Scientist\n")
    add.write("gamma,35,Teacher\n")

# Inform the user that the file was created successfully.
print(f"CSV file '{filename}' has been created and can be opened in MS-Excel.")
