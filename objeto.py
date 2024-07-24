class Exemplo:
    pass

x = Exemplo()
print(type(x))

print(" ")
#----------------------------------------#
class Dog:
    def __init__(self):
        self.idade = 10

dog = Dog()

print("O dog tem {} anos.".format(dog.idade))
print(" ")
#----------------------------------------#
class Dog2:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 8

dog2 = Dog2("Bordie Collie")

print("O dog da raça {}, tem {} anos.".format(dog2.raca, dog2.idade))

print(" ")
#----------------------------------------#

class Dog3:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 8
        print("{} criado".format(raca))

dog3 = Dog3("Husk")

print(dog3)

print(" ")

#----------------------------------------#
class Dog4:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 8
        print("{}, criado".format(raca))
    
    def envelhecer(self):
        self.idade += 1
        return self.idade

dog4 = Dog4("Labr")
dog4.envelhecer()

print(dog4)
print(dog4)
print(dog4.idade)


print(" ")


#----------------------------------------#

#Circulo
class Circle:
    def __init__(self, raio=1):
        self.raio = raio
    
    def calcula_area(self):
        return self.raio * self.raio * 3.14
c1 = Circle()
print(c1.raio)
print(c1.calcula_area())
c2 = Circle(5)
print(c2.raio)
print(c2.calcula_area())