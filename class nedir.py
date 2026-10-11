class araba:
    def __init__(self,marka,renk):
        self.marka=marka
        self.renk=renk
    def tanit(self):
        print(f"bu araba bir {self.marka} ve rengi {self.renk}.")

benim_arabam = araba("toyota","kırmızı")
benim_arabam.tanit()