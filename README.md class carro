class Carro:
    def __init__(self , marca, modelo, cor, ano, valor):
        self.marca=marca
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        self.valor=valor
class Estoque:
    def __init__(self):
        self.carros=[]
    def Adicionar_Carro(self,carro):
        self.carros.append(carro)
    def Mostra_Estoque(self):
        for carro in self.carros:
            print(f'{carro.modelo}, {carro.marca} adicionado ao estoque ')
carro_1=Carro('porsche','911','branca','2024', 1000000)
carro_2=Carro('lamborghini','urus','preto','2024', 2000000)
carro_3=Carro('ferrari','puro sangue','vermelha','2024', 15000000)
carro_4=Carro('mercedes','g63','preto','2025', 2247900)
carro_5=Carro('nissan','gtr r5','prta e azul','2012', 1579000)

estoque=Estoque()
estoque.Adicionar_Carro(carro_1)
estoque.Adicionar_Carro(carro_2)
estoque.Adicionar_Carro(carro_3)
estoque.Adicionar_Carro(carro_4)
estoque.Adicionar_Carro(carro_5)

estoque.Mostra_Estoque()
