class simpBeam():
    def __init__(self,l):
        self.l=l
    def Mdistmax(self,w):
        return w*self.l**2/8
    def Mpuntmax(self,p,n):
        return p*self.l/8*(n*(n+2)/(n+1)) if n % 2 == 0 else n+1
    def Mtruck(self,p,a):
        return p/4*(self.l if self.l<=2*a else (9*self.l-10*a)/4)
    def Mtandem(self,p,a):
        return p*(self.l-a)/2
    def Mlane(self,w):
        return w*self.l**2/8


