#Eloyse Marques 3° Ano
class Veículo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def frear(self):
        return(f"{self.marca} {self.modelo} O veículo está freando.")
    def acelerar(self):
        return(f"{self.marca} {self.modelo} O veículo está acelerando.")

class Carro(Veículo):
    def __init__(self,marca,modelo,cor):
        super().__init__(marca,modelo)
        self.cor = cor
    def abrir_porta(self):
        return(f"As portas do{self.marca} {self.modelo} {self.cor} estão abertas.")

class Moto(Veículo):
    def __init__(self,marca,modelo,cilindrada):
        super().__init__(marca,modelo)
        self.cilindarda = cilindrada
    def verticalizar(self):
        return(f"{self.marca} {self.modelo} {self.cilindarda} está verticalizando.")
if __name__ == "__main__":
    carro = Carro("Chevrolet","Opala","Preto")
    print(carro.frear())
    print(carro.acelerar())
    print(carro.abrir_porta())

    moto = Moto("Harley","Harley-Dividson","1200")
    print(moto.frear())
    print(moto.acelerar())
    print(moto.verticalizar())