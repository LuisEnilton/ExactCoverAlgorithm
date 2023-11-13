#Essa classe busca representar uma estrutura de horários, onde cada elemento é uma tupla (dia, horário)
# Ela é criada dando os dias da semana e os horários requeridos, e gera as tuplas automaticamente
class EstruturaDeHorarios:
    # dias é uma lista que pode ter 7 valores [1,2,3,4,5,6,7], segunda,terça,quarta,quinta,sexta,sabado,domingo
    #horários é uma tupla que define o inicio e o final , cada aula tem por padrão uma hora de duração, intervalos não são considerados 
     
    horarios = []
    dias = []
    horas = []
    def gera_horarios(self):
        ret = []
        for dia in self.dias:
            for i in range(self.horas[0],self.horas[1]+1):
                ret.append((dia,i))
        return ret
    
    def __init__(self, dias, horas):
        self.dias = dias
        self.horas = horas
        self.horarios = self.gera_horarios()
    