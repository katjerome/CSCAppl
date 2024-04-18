"""Kayatha Jerome April 17,2024"""

from abc import ABC, abstractmethod

"""This class employee was created to set the initial state for an employee.
 The constructor will define the type of information that is needed for the employee to enter.  """
class Employee(ABC):
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    @abstractmethod
    # abstract method to get information about the employee
    def get_employee_info(self):
        pass # Placeholder left intentionally blank

class EmployeeManager:
    ## Initialize the EmployeeManager with a dictionary of employees
    def __init__(self):
        self.employees = {
            "Sarah Marshall": 7786,
            "Jacob Masterson": 5672,
            "Benjamin Edwards": 8569
        }

    def add_employee(self):
        ## Method to add a new employee to the dictionary
        ## Input first name
        ## Input last name
        ## Input ID number
        ## will need an if and else
    pass


    def edit_employee(self):
        # method to edit employee information
        ## input employee name
        ## int input for new id num
        ## if /else needed
        ## print memos "Employee information updated successfully" "Employee not found"
    pass

    def remove_employee(self):
    # method to remove existing employee from the dictionary
    # input employee name
    # print memos "Employee removed successfully" "Employee not found"
     pass


    def view_employees(self):
    # method to display the current list of employees in the dictionary
    # print memo "(current employees)'
    pass

class NewEmployee(Employee):
    # Subclass of employee representing a new employee
    # Implementation of the abstract method to get information about the employee
    # return function
    pass


if __name__ == "__main__":
    manager = EmployeeManager()
# Main menu for the user when the application starts
    while True:
        print("\nChoose an option:")
        print("1. Add new employee")
        print("2. Edit employee")
        print("3. Remove employee")
        print("4. View employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

# if statements for the options that are available
        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.edit_employee()
        elif choice == "3":
            manager.remove_employee()
        elif choice == "4":
            manager.view_employees()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")