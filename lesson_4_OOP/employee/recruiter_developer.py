from employee.employee import Employee


class Recruiter(Employee):
    """Class Recruiter"""

    def work(self):
        """Method returns a string"""
        return 'I come to the office and start to hiring.'

    def __str__(self):
        return f"{self.job_title}:{self.name}"


class Developer(Employee):
    """Class Developer"""

    def __init__(self, name, job, salary, tech_stack):
        """Constructor accepts arguments: name, job, salary, tech_stack"""

        self.tech_stack = tech_stack
        super().__init__(name, job, salary)

    def work(self):
        """Method returns a string"""
        return 'I come to the office and start to coding.'

    def __str__(self):
        return f"{self.job_title}:{self.name}"

    def __lt__(self, other):
        return self.tech_stack < other.tech_stack

    def __le__(self, other):
        return self.tech_stack <= other.tech_stack

    def __gt__(self, other):
        if self.tech_stack > other.tech_stack:
            return True
        else:
            return False

    def __ge__(self, other):
        return self.tech_stack >= other.tech_stack

    def __eq__(self, other):
        return self.tech_stack == other.tech_stack

    def __ne__(self, other):
        return self.tech_stack != other.tech_stack

    def __add__(self, other):
        return Developer(self.name + " " + other.name, None, max(self.salary, other.salary),
                         list(set(self.tech_stack + other.tech_stack)))
