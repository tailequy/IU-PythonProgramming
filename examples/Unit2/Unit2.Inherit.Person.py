class PersonClass(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self, person_type):
        print("The " + person_type + " name is: " + self.first_name +" "+ self.last_name)

    def get_name_email(self, email):
        name_email = "The email of " + self.first_name + " " + self.last_name \
                     + " is: " + email
        return name_email

    def is_employee(self):
        return True

class EmployeeClass(PersonClass):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def print_employee_id(self, id):
        print("Employee " + self.first_name + " " + self.last_name + " id is: " + str(id))

    def is_employee(self):
        return True

class CustomerClass(PersonClass):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def print_customer_phone(self, customer_phone):
        print("Customer " + self.first_name + " " + self.last_name +
              " phone is: " + customer_phone)

    def is_employee(self):
        return False

def main():
    # print employee name
    first_name = "John"
    last_name = "Smith"
    employee_class = EmployeeClass(first_name, last_name)
    person_type = "employee"
    employee_class.print_name(person_type)
    # print employee id
    employee_id = 100
    employee_class.print_employee_id(employee_id)
    # check if an employee is employee
    result = employee_class.is_employee()
    print(result)
    # print customer name
    first_name = "David"
    last_name = "Johnson"
    customer_class = CustomerClass(first_name, last_name)
    person_type = "customer"
    customer_class.print_name(person_type)
    # print customer phone number
    customer_phone = "+1.800.503.987.6543"
    customer_class.print_customer_phone(customer_phone)
    # check if a customer is employee
    result = customer_class.is_employee()
    print(result)
if __name__ == '__main__':
    main()