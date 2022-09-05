"""Module contains classes: Employee, Recruiter, Developer"""

from datetime import date, datetime

import numpy


class Employee:
    """Class Employee"""

    def __init__(self, name, job_title, salary):
        """Constructor accepts arguments: name, job_title, salary"""

        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        """Method returns a string"""
        return 'I come to the office.'

    def __str__(self):
        return f"employee:{self.name}"

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def check_salary(self, days):
        """Payment calculation method"""
        return self.salary * days

    def check_data_salary(self, month):
        """Method for calculating payment for a certain period"""
        date1 = date(2022, month, 1)
        date2 = datetime.now()
        work_day = numpy.busday_count(date1.strftime("%y-%m-%d"), date2.strftime("%y-%m-%d"))
        work_day = work_day + 1
        salary_working_day = self.salary * work_day
        return salary_working_day
