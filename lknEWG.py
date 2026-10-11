from abc import ABC abstracmethod
import math
class ucgen:(ABC)
    abstractemethod
    def delta(self):pass
class deltahesaplama (ucgen)
    def__init__(self,b,a,c)
self.b,self.a,self.c=b,c,a
def delta  (self):
    return self.b*self.b-4*self.a*self.c
class hesaplama (deltahesaplama)
    def kokhesaplama (self)
        d=self.delta()
        if d>0
