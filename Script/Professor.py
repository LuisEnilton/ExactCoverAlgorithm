class Professor:
    
    classes = [] # lista de aulas que o professor leciona, cada elemento é uma tupla (dia, horário)
    
    
    cost = 90 #Custo da aula por hora
    
    def __init__(self,name):
        self.name = name
    
    def __init__(self, name, classes):
        self.name = name
        self.salary = len(classes) * self.cost #salário do professor é o número de aulas que ele leciona vezes o custo da aula
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
    