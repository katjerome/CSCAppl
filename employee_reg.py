# Import abc to define the abstractmethod in the code
from abc import ABC, abstractmethod

# Employee class to manage employee information
class EmployeeRegistry:
    def __init__(self):
# Empty dictionary to store employees
        self.employees = {}

# Method to add a new employee
    def add_employee(self, first_name, last_name, id_number):
        employee_name = first_name + " " + last_name
        if employee_name in self.employees:
            print("Employee already exists.")
        else:
            self.employees[employee_name] = id_number
            print("Employee added successfully.")

# Method to view all employees in the dictionary

    def view_all_employees(self):
        print("Current employees:")
        for employee_name, id_number in self.employees.items():
            print(f"Name: {employee_name}, ID: {id_number}")

# Method to view emplyess by their ID number

    def view_employee_by_id(self, id_number):
        for employee_name, employee_id in self.employees.items():
            if employee_id == id_number:
                print(f"Employee details: Name: {employee_name}, ID: {id_number}")
                return
        print("Employee not found.")
# Method to edit employee information in the registry

    def edit_employee(self, employee_name, new_id_number):
        if employee_name in self.employees:
            self.employees[employee_name] = new_id_number
            print("Employee information updated successfully.")
        else:
            print("Employee not found.")

# Method to remove employee from the registry permanently

    def remove_employee(self, employee_name):
        if employee_name in self.employees:
            del self.employees[employee_name]
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

# Abstract base class for employee

class Employee(ABC):
    @abstractmethod
    def get_employee_info(self):
        pass

# Class NewEmployee definition
class NewEmployee(Employee):
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

# Implementing the abstract method to get employee information
    def get_employee_info(self):
        return f"{self.first_name} {self.last_name} ID: {self.id_number}"
