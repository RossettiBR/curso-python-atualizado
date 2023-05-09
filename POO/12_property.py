class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('azul')
print(caneta.cor)
print(caneta.cor_tampa)
