class Professor:
    
    classes = [] # lista de aulas que o professor leciona, cada elemento é uma tupla (dia, horário)
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __init__(self, name, age, salary, classes):
        self.name = name
        self.age = age
        self.salary = salary
        self.classes = classes
    
    def get_name(self):
        return self.name

    def __eq__(self,other):
        return self.classes == other.classes
    
    def __hash__(self):
        return hash(tuple(self.classes))
    
    def get_age(self):
        return self.age
    
    def get_salary(self):
        return self.salary
    
    def add_class(self, day, time):
        self.classes.append((day, time))
    