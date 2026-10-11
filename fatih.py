class karakter :
    def __init__(self, isim , can ):
        self.isim = isim
        self.can = can

    def saldir(self):
            print(f"{self.isim} saldırıya geçti! ")

oyuncu1 = karakter("savaşçı", 100)

print(f"karakter: {oyuncu1.isim} , canı : {oyuncu1.can}")
oyuncu1.saldir()
#