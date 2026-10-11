class araba :
    def __init__ (self,marka,model) :
        self.marka=marka
        self.model=model
    def bilgileri_goster(self):
        return f"Marka: {self.marka}, model: {self.model}"
araba1=araba("Toyota","corolla")
print(araba1.bilgileri_goster())