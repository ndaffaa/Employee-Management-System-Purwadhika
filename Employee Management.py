from tabulate import tabulate

# Sample employee data with years employed
employees = [
    ["Budi", "Santoso", "Software Engineer", "Engineering", 1],
    ["Siti", "Rahayu", "Human Resources Manager", "HR", 5],
    ["Agus", "Setiawan", "Marketing Executive", "Marketing", 7],
    ["Rini", "Susanti", "Accountant", "Finance", 2],
    ["Ani", "Wijaya", "Sales Representative", "Sales", 1],
    ['Naufal', 'Daffa', 'Data Scientist', 'Data', 10],
    ['Ayu', 'Widya', 'Software Engineer', 'Engineering', 3],
    ['Serenande', '', 'Human Resources Staff', 'HR', 2],
    ['Tegar', 'Silalahi', 'Marketing Manager', 'Marketing', 8],
    ['Jasper', 'Corpus', 'Head of Sales', 'Sales', 9],
    ['Juan', 'Dharmaji', "Head of Finance", 'Finance', 5]
]

header = ["First Name", "Last Name", "Role", "Division", "Years Employed"]

# Function to generate a summary of user input
def generate_input_summary(**kwargs):
    print("\nSummary of Input:")
    print("\n====================")
    for key, value in kwargs.items():
        print(f"{key.ljust(15)}: {value}")
    print("\n====================")

# Function to sort employees based on different criteria
def sort_employees(criteria, employee_data):
    if criteria == "first name":
        return sorted(employee_data, key=lambda x: x[0].lower())
    elif criteria == "last name":
        return sorted(employee_data, key=lambda x: x[1].lower())
    elif criteria == "role":
        return sorted(employee_data, key=lambda x: x[2].lower())
    elif criteria == "division":
        return sorted(employee_data, key=lambda x: x[3].lower())
    elif criteria == "years employed":
        return sorted(employee_data, key=lambda x: x[4])


# Function to display the employee table
def display_employee_table(employee_data):
    headers = header
    print(tabulate(employee_data, headers=headers, tablefmt="grid", showindex='always'))
    
    while True:
        action = input('''\nChoose an action:\n1. Sort the list\n2. View employee details\n3. Return to main menu\nEnter your choice: ''').strip()
        
        if action == "1":
            print("\nSorting Options:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Role")
            print("4. Division")
            print("5. Years Employed")
            choice = input("Enter your choice (type 'back' to back): ").strip()
            if choice == "1":
                criteria = "first name"
            elif choice == "2":
                criteria = "last name"
            elif choice == "3":
                criteria = "role"
            elif choice == "4":
                criteria = "division"
            elif choice == "5":
                criteria = "years employed"
            elif choice == 'back':
                continue
            else:
                print("Invalid choice, please input correct answer.")
                continue
            sorted_employees = sort_employees(criteria, employee_data)
            if sorted_employees:
                print("Sorted Employees:")
                display_employee_table(sorted_employees)
            else:
                print("No employees in the list.")
            break
        elif action == "2":
            try:
                index = int(input("Enter the employee number to view details: "))
                if 0 <= index < len(employee_data):  # Changed condition from <= to <
                    employee = employee_data[index]
                    generate_input_summary(First_name=employee[0], Last_name=employee[1], Role=employee[2], Division=employee[3], Years_employed=employee[4])
                else:
                    print("Invalid employee number. Please enter a number between 0 and", len(employee_data) - 1)  # Added instruction for valid input range
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif action == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Function to display the list of employees
def display_employees():
    if employees:
        print("List of Employees:\n")
        display_employee_table(employees)
    else:
        print("No employees in the list.")


# Function to add a new employee
def add_employee():
    while True:
        try:
            first_name = input("Enter employee first name (type 'exit' to cancel): ").strip().title()
            if first_name.lower() == 'exit':
                print("Employee addition cancelled.")
                return  # Exit the function
            if not first_name.replace(' ','').isalpha():
                raise ValueError("First name must contain only alphabetic characters or cannot be empty.")
            
            last_name = input("Enter employee last name (type 'exit' to cancel): ").strip().title()
            if last_name.lower() == 'exit':
                
                return  # Exit the function
            if not last_name.replace(' ','').isalpha():
                raise ValueError("Last name must contain only alphabetic characters or cannot be empty.")
            
            full_name = f"{first_name} {last_name}"
            for employee in employees:
                if f"{employee[0]} {employee[1]}" == full_name:
                    raise ValueError(f"Employee named {first_name} {last_name}  already exists. Please use the 'update' menu to change particular data.")
            
            role = input("Enter employee role (type 'exit' to cancel): ").strip().title()
            if role.lower() == 'exit':
                print("Employee addition cancelled.")
                return  # Exit the function
            if not role.replace(' ','').isalpha():
                raise ValueError("Role must contain only alphabetic characters or cannot be empty.")
            
            division = input("Enter employee division (type 'exit' to cancel): ").strip().title()
            if division.lower() == 'exit':
                print("Employee addition cancelled.")
                return  # Exit the function
            if not division.replace(' ','').isalpha():
                raise ValueError("Division must contain only alphabetic characters or cannot be empty.")
            
            years_employed = input("Enter years employed (type 'exit' to cancel): ").strip()
            if years_employed.lower() == 'exit':
                print("Employee addition cancelled.")
                return  # Exit the function
            years_employed = int(years_employed)
            if years_employed < 0:
                raise ValueError("Years employed cannot be negative.")
            
            # Generate summary of user input
            generate_input_summary(First_name=first_name, Last_name=last_name, Role=role, Division=division, Years_employed=years_employed)
            
            confirm = input(f"\nAre you sure you want to add {full_name} to the employee list? (yes/no): ").strip().lower()
            if confirm == 'yes':
                employees.append([first_name, last_name, role, division, years_employed])
                print("Employee added successfully.")
                break  # Exit the loop if all data is valid
            elif confirm == 'no':
                print("Employee addition cancelled.")
                return
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        except ValueError as e:
            print("Error:", e)


# Function to delete an employee by index
def delete_employee():
    while True:
        try:
            if not employees:
                print("No employees in the list.")
                return
            
            print("\nList of Employees:")
            headers = header
            print(tabulate(employees, headers=headers, tablefmt="grid", showindex='always'))

            index = input("Enter the index of the employee to delete (type 'exit' to cancel): ").strip()
            if index.lower() == 'exit':
                print("Employee deletion cancelled.")
                return
            index = int(index)

            if index < 0 or index >= len(employees):
                raise ValueError("Invalid index.")

            employee = employees[index]

            # Generate summary of user input
            generate_input_summary(First_name=employee[0], Last_name=employee[1], Role=employee[2], Division=employee[3], Years_employed=employee[4])
    
            confirm = input(f"\nAre you sure you want to delete {employee[0]} {employee[1]} from the employee list? (yes/no): ").strip().lower()
            if confirm == 'yes':
                employee = employees.pop(index)
                print(f"Employee '{employee[0]} {employee[1]}' deleted successfully.")
                break
            elif confirm == 'no':
                print("Employee deletion cancelled.")
                return
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and", len(employees) - 1, " or 'exit' to cancel.")


# Function to update employee information
def update_employee():
    try:
        if not employees:
            print("No employees in the list.")
            return
        print("\nList of Employees:")
        headers = header
        print(tabulate(employees, headers=headers, tablefmt="grid", showindex='always'))
        
        index = int(input("Enter the index of the employee to update: "))
        if index < 0 or index >= len(employees):
            raise ValueError("Invalid index.")
        
        employee = employees[index]
        print(f"\nUpdating information for employee: {employee[0]} {employee[1]}")

        new_first_name = input("Enter new first name (leave empty to keep current or type 'exit' to cancel): ").strip().title()
        if new_first_name.lower() == 'exit':
                print("Employee update cancelled.")
                return
        
        new_last_name = input("Enter new last name (leave empty to keep current or type 'exit' to cancel): ").strip().title()
        if new_last_name.lower() == 'exit':
                print("Employee update cancelled.")
                return
        
        new_role = input("Enter new role (leave empty to keep current or type 'exit' to cancel): ").strip().title()
        if new_role.lower() == 'exit':
                print("Employee update cancelled.")
                return
        
        new_division = input("Enter new division (leave empty to keep current or type 'exit' to cancel): ").strip().title()
        if new_division.lower() == 'exit':
                print("Employee update cancelled.")
                return
        
        new_years_employed = input("Enter new years employed (leave empty to keep current or type 'exit' to cancel): ").strip()
        if new_years_employed.lower() == 'exit':
                print("Employee update cancelled.")
                return
        
        # Generate summary of user input
        generate_input_summary(First_name=new_first_name or employee[0], 
                                Last_name=new_last_name or employee[1], 
                                Role=new_role or employee[2], 
                                Division=new_division or employee[3], 
                                Years_employed=new_years_employed or employee[4])
        
        confirm = input(f"Are you sure you want to update this information? (yes/no): ").strip().lower()
        if confirm == 'yes':
            if new_first_name:
                employee[0] = new_first_name
            if new_last_name:
                employee[1] = new_last_name
            if new_role:
                employee[2] = new_role
            if new_division:
                employee[3] = new_division
            if new_years_employed:
                employee[4] = int(new_years_employed)
            
            print("Employee information updated successfully.")
        elif confirm == 'no':
            print("Employee information update cancelled.")
            return
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    except ValueError as e:
        print("Error:", e)
 

# Main function
def main():
    while True:
        print("\nWelcome to Employee Management System of Purwadhika")
        print("1. Show list of employees")
        print("2. Add employee")
        print("3. Delete employee")
        print("4. Update employee information")
        print("5. Exit")
        choice = input("Enter your choice by index: ")

        if choice == "1":
            display_employees()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
