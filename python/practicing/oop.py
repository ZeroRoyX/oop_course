def run():
    
    class Employee:
    
        num_of_emps = 0
        raise_amount = 1.04
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com'

            Employee.num_of_emps += 1            

        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)

    print(Employee.num_of_emps)


    emp_1 = Employee('Rodrigo', 'Arana', 50000)
    emp_2 = Employee('Test', 'User', 60000)

    print(Employee.num_of_emps)

    # emp_1.raise_amount = 1.05

    # print(emp_1.__dict__)
    # print(vars(emp_2))

    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)
    
    # emp_1.apply_raise()

    

if __name__ == '__main__':
    run()


