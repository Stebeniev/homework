from employee.customException import EmailAlreadyExitsException
from employee.employee import Employee
import traceback
from datetime import datetime


def main():
    emp = Employee('Alex', 'Administrator', 25, 'qwerty@gmail.com')
    print(emp)

if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExitsException:
        with open('logs.txt', 'a+') as fp:
            fp.write(f"{datetime.now()} \n {traceback.format_exc()}")
    # emp1 = Employee('Nick', 'Tester', 5)
    # emp2 = Employee('Alexey', 'Administrator', 8)
    # class_d1 = Developer('Petro', 'Administrator', 5, ['Python', 'JS', 'Java'])
    # class_d2 = Developer('Nicolas', 'Programmer', 8, ['C++', 'Java'])
    # class_d = class_d1 + class_d2
    # employee = Employee("Alex", "Programmer", 25)
    # print(employee.work())
    # print(str(employee))
    # recruiter = Recruiter("Helen", "Recruiter", 15)
    # print(recruiter.work())
    # print(str(recruiter))
    # developer = Developer("Ivan", "Developer", 50, 'Python')
    # print(developer.work())
    # print(str(developer))
    # print(emp1 < emp2)
    # print(class_d1 > class_d2)
    # print(class_d1.check_salary(20))
    # print(class_d.name, " ", class_d.tech_stack, " ", class_d.salary)
    # print(f'august salary - {class_d1.check_data_salary(8)}_$')
    #emp = Employee('Alex', 'Administrator', 25, 'qwerty@gmail.com')
