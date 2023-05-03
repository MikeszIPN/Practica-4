class Person:
    def __init__ (self, name, age, weight, height):
        self.age = age
        self.weight = weight

        self.name = name
        self. height = height

    def setPeso (self, peso):
        self.weight = peso

    def setEdad(self, edad):
        self.age = edad
    
    def getPeso(self):
        return self.weight

    def getEdad(self):
        return self.age

    def indMasaCorp(self):
        return 100*self.height/self.weight

p1 = Person ('Bob', 41, 74, 1.74)

""""
p1 = Person()
p1.name = 'Bob'
p1.setEdad(41)
p1.heigth = 74
p1.setPeso(1.74)
"""

print('Nombre: ' + p1.name)
print('Edad: ' + str(p1.getEdad()))
print('Peso: ' + str(p1.getPeso()))
print('Estatura: ' + str(p1.height))
print('ind Masa Corporal: ' + str(p1.indMasaCorp()))