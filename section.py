
def areaPoly(x):
    y=list()
    for i in range(len(x[0])-1):
        y.append(x[0][i]*x[1][i+1]-x[0][i+1]*x[1][i])
    return y
def momentPoly(x):
    y=list()
    for i in range(len(x)-1):
        y.append(x[i]+x[i+1])
    return y
def statPoly(x,y):
    z=0
    for i in range(len(x)):
        z+=x[i]*y[i]
    return z
def inertPoly(x,y,z):
    u=0
    for i in range(len(x)-1):
        u+=(x[i]-x[i+1])*(y[i]**2+y[i+1]**2)*z[i]
    return u
class General:
    def __init__(self,x):
            self.x=x
            self.Area=sum(areaPoly(self.x))/2
    def Qx(self):
        return statPoly(areaPoly(self.x),momentPoly(self.x[1]))/6
    def Qy(self):
        return statPoly(areaPoly(self.x),momentPoly(self.x[0]))/6
    def Ixx(self):
        return inertPoly(self.x[0],self.x[1],momentPoly(self.x[1]))/12
    def Iyy(self):
        return -inertPoly(self.x[1],self.x[0],momentPoly(self.x[0]))/12
    def xg(self):
        return self.Qy()/self.Area
    def yg(self):
        return self.Qx()/self.Area
    def Ixg(self):
        return self.Ixx()-self.Area*self.yg()**2
    def Iyg(self):
        return self.Iyy()-self.Area*self.xg()**2
    def srx(self):
        return self.Ixg()/self.Area
    def sry(self):
        return self.Iyg()/self.Area
    def rx(self):
        return self.srx()**0.5
    def ry(self):
        return self.sry()**0.5
    def x1(self):
        return self.xg()-min(self.x[0])
    def x2(self):
        return max(self.x[0])-self.xg()
    def y1(self):
        return self.yg()-min(self.x[1])
    def y2(self):
        return max(self.x[1])-self.yg()
    def S1x(self):
        return self.Ixg()/self.y1()
    def S2x(self):
        return self.Ixg()/self.y2()
    def S1y(self):
        return self.Iyg()/self.x1()
    def S2y(self):
        return self.Iyg()/self.x2()
    def k1x(self):
        return self.srx()/self.y2()
    def k1y(self):
        return self.sry()/self.x2()
    def k2x(self):
        return self.srx()/self.y1()
    def k2y(self):
        return self.sry()/self.x1()
class BeamTBridg(General):
    def __init__(self,bt,bb,bw,h,ht,hb,tt,tb):
        self.bt=bt
        self.bb=bb
        self.bw=bw
        self.h=h
        self.ht=ht
        self.hb=hb
        self.tt=tt
        self.tb=tb
        self.x=[
[bb/2,bb/2,bw/2,bw/2,bt/2,bt/2,-bt/2,-bt/2,-bw/2,-bw/2,-bb/2,-bb/2,bb/2],
[0,hb,hb+tb,h-ht-tt,h-ht,h,h,h-ht,h-ht-tt,hb+tb,hb,0,0]]
        self.Area=sum(areaPoly(self.x))/2

'''
#Ejemplo de la clase
bt=56;  bb=51;  bw=20                                h=152;  ht=13;  hb=16.5
tt=4;   tb=16.5
section1=section.BeamTBridg(bt,bb,bw,h,ht,hb,tt,tb)  print(f"Ag={section1.Ag}")                           print(f"Qx={section1.Qx()}\tQy={section1.Qy()}")     print(f"xg={section1.xg()}\tyg={section1.yg()}")     print(f"x1={section1.x1()}\ty1={section1.y1()}")
print(f"x2={section1.x2()}\ty2={section1.y2()}")     print(f"Ixx={section1.Ixx()}\tIyy={section1.Iyy()}") print(f"Ixo={section1.Ixo()}\tIyo={section1.Iyo()}") print(f"rx={section1.rx()}\try={section1.ry()}")     print(f"S1x={section1.S1x()}\tS1y={section1.S1y()}")
print(f"S2x={section1.S2x()}\tS2y={section1.S2y()}") print(f"k1x={section1.k1x()}\tk1y={section1.k1y()}") print(f"k2x={section1.k2x()}\tk2y={section1.k2y()}")
'''
