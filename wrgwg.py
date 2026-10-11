class kitap:
    def __init__(self,ad,yazar):
       self.ad=ad
       self.yazar=yazar
    def bilgi_ver(self):
        print (f"{self.ad} kitabı , {self.yazar} yazarı tarafından yazılmıştır.")
kitap1=kitap("Nutuk","Mustafa kemal atatürk")
kitap1.bilgi_ver()