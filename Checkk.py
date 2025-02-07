import sqlite3

# Connect to the database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Query the Employees table
cursor.execute("SELECT * FROM Employees WHERE Department = ?", ("Sales",))
results = cursor.fetchall()

# Print the results
if results:
    print("Employees in Sales department:")
    for row in results:
        print(row)
else:
    print("No employees found in the Sales department.")

# Close the connection
conn.close()