from employee_reg import EmployeeRegistry

if __name__ == "__main__":
    registry = EmployeeRegistry()

    while True:
        print("\nChoose an option:")
        print("1. View all employees")
        print("2. Add employee")
        print("3. View employee by ID")
        print("4. Edit employee")
        print("5. Remove employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            registry.view_all_employees()
        elif choice == "2":
            first_name = input("Enter employee's first name: ")
            last_name = input("Enter employee's last name: ")
            id_number = int(input("Enter employee's ID number: "))
            registry.add_employee(first_name, last_name, id_number)
        elif choice == "3":
            id_number = int(input("Enter employee's ID number to view: "))
            registry.view_employee_by_id(id_number)
        elif choice == "4":
            employee_name = input("Enter employee's full name to edit: ")
            new_id_number = int(input("Enter employee's new ID number: "))
            registry.edit_employee(employee_name, new_id_number)
        elif choice == "5":
            employee_name = input("Enter employee's full name to remove: ")
            registry.remove_employee(employee_name)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")
