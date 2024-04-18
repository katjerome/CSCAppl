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
        first_name = input("Enter employee's first name: ")
        last_name = input("Enter employee's last name: ")
        id_number = int(input("Enter employee's ID number: "))
        employee_name = first_name + " " + last_name
        if employee_name in self.employees:
            print("Employee already exists.")
        else:
            self.employees[employee_name] = id_number
            print("Employee added successfully.")

    def edit_employee(self):
        employee_name = input("Enter employee's full name to edit: ")
        if employee_name in self.employees:
            new_id_number = int(input("Enter employee's new ID number: "))
            self.employees[employee_name] = new_id_number
            print("Employee information updated successfully.")
        else:
            print("Employee not found.")

    def remove_employee(self):
        employee_name = input("Enter employee's full name to remove: ")
        if employee_name in self.employees:
            del self.employees[employee_name]
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

    def view_employees(self):
        print("Current employees:")
        for employee, id_number in self.employees.items():
            print(f"{employee} ID: {id_number}")

class NewEmployee(Employee):
    def get_employee_info(self):
        return f"{self.first_name} {self.last_name} ID: {self.id_number}"


if __name__ == "__main__":
    manager = EmployeeManager()

    while True:
        print("\nChoose an option:")
        print("1. Add new employee")
        print("2. Edit employee")
        print("3. Remove employee")
        print("4. View employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

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
