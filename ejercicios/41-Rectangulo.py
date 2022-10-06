class Recatangulo:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def area(self):
        area=self.alto*self.ancho
        return area
    def perimetro(self):
        perimetro=(self.alto*2)+(self.ancho*2)
        return perimetro
r1=Recatangulo(4,2)
area=r1.area()
perimetro=r1.perimetro()
print("El área es:", area)
print("El perímetro es:", perimetro)