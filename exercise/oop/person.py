class Person:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id

class Employee(Person):
    def __init__(self, name, id, salary, post):
        Person.__init__(self, name, id)
        self.__salary = salary
        self.__post = post
    
    def get_salary(self):
        return self.__salary
    
    def get_post(self):
        return self.__post
    
p = Person("Nafi", 120)
e = Employee("Audwit Nafi", 30180, 50000, "Trainee Software Engineer")

print(f"The name and id of the person is {p.get_name()} and {p.get_id()}")
print(f"He is a {e.get_post()}, id {e.get_id()}, of BJIT whose salary is {e.get_salary()}")