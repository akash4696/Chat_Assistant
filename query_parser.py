import re

def parse_query(user_query):
    """
    Parse a natural language query into an SQL query.
    Returns: (sql_query, params)
    """
    user_query = user_query.lower()
    print("Received Query:", user_query)  # Debugging print
    
    # Match "Show me all employees in the X department"
    match = re.match(r"show me all employees in the (.+) department", user_query)
    if match:
        department = match.group(1).strip()
        print("Parsed Department:", department)  # Debugging print
        return "SELECT * FROM Employees WHERE LOWER(Department) = LOWER(?)", (department,)

    # Match "Who is the manager of the X department"
    match = re.match(r"who is the manager of the (.+) department", user_query)
    if match:
        department = match.group(1).strip()
        print("Parsed Department:", department)  # Debugging print
        return "SELECT Manager FROM Departments WHERE LOWER(Name) = LOWER(?)", (department,)

    # Match "List all employees hired after YYYY-MM-DD"
    match = re.match(r"list all employees hired after (\d{4}-\d{2}-\d{2})", user_query)
    if match:
        date = match.group(1).strip()
        print("Parsed Hire Date:", date)  # Debugging print
        return "SELECT * FROM Employees WHERE Hire_Date > ?", (date,)

    # Match "What is the total salary expense for the X department"
    match = re.match(r"what is the total salary expense for the (.+) department", user_query)
    if match:
        department = match.group(1).strip()
        print("Parsed Department:", department)  # Debugging print
        return "SELECT SUM(Salary) AS Total_Salary FROM Employees WHERE LOWER(Department) = LOWER(?)", (department,)

    print("No matching query found")  # Debugging print
    return None, None
