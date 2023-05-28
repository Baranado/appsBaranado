
#Materiales
import math
import section
import struct
#Condiciones de diseño
l=2500
print(f"Luz simple de diseño: {l} cm")
w=800
print(f"Ancho de calzada: {w} cm")
nbeam=4
print(f"Numero de vigas: {nbeam}")
s=220
print(f"Separacion entre ejes de vigas: {s} cm")
nl=int(round(w/360))
print(f"Numero de vias: {nl}")
rmf=[1.2,1,.85]
mf=.65 if nl>3 else rmf[nl-1]
print(f"Factor de presencia multiple: {mf}")
de=(w-(nbeam-1)*s)/2
print(f"Distancia eje de viga exterior al borde de la calzada: {de} cm")
#Materiales
gammac=.0000024
print(f"Peso especifico del hormigon: {gammac} tonf/cm3")
fcbeam=.4
print(f"Resistencia caracteristica del hormigon en la viga: {fcbeam} tonf/cm2")
fcdeck=.28
print(f"Resistencia caracteristica del hormigon en la losa: {fcdeck} tonf/cm2")
ne=(fcbeam/fcdeck)**.5
print(f"Relacion modular: {ne}")
#Seccion viga T
bt=56;  bb=51;  bw=20
h=152;  ht=13;  hb=16.5
tt=4;   tb=16.5
section1=section.BeamTBridg(bt,bb,bw,h,ht,hb,tt,tb)
Abeam=section1.Area
print(f"Area de la viga: {Abeam} cm2")
Ixg=section1.Ixg()
print(f"Momento de Inercia de la viga: {Ixg} cm4")
yt=section1.y2()
print(f"Distancia del centro a la parte superior de la viga: {yt} cm")
#Seccion losa
ts=math.ceil(max(s,195)/15)/2+10
print(f"Espesor de la losa: {ts} cm")
be=s/2+min(l/8,6*ts+bt/4,70)
print(f"Ancho efectivo de losa en viga exterior: {be} cm")
Adeck=be*ts
print(f"Area efectiva de losa en viga exterior: {Adeck} cm2")
#Seccion compuesta
Acomp=Abeam+Adeck
print(f"Area de la seccion compuesta: {Acomp} cm2")
eg=yt+ts/2
print(f"Distancia entre centroides de losa y viga: {eg} cm")
kg=ne*(Ixg+Abeam*eg**2)
print(f"Rigidez de la seccion compuesta: {kg} cm4")
#Seccion carpeta de rodadura                         
hw=2
print(f"Espesor de la capa de rodadura: {hw} cm")
Adw=be*hw
print(f"Area de la carpeta de rodadura: {Adw} cm2")
#Seccion de diafragma
ndiaph=2
print(f"Numero de diafragmas: {ndiaph}")
bdiaph=20
print(f"Espesor del diafragma: {bdiaph} cm")
hdiaph=119
print(f"Alto del diafragma: {hdiaph} cm")
Adiaph=bdiaph*hdiaph
print(f"Area de la seccion del diafragma: {Adiaph} cm2")
Vdiaph=Adiaph*(s-bw)/2
print(f"Volumen del diafragma: {Vdiaph} cm3")
#Seccion bordillo
Ad1=350+15*(ts+hw)
print(f"Area de la seccion de bordillo: {Ad1} cm2")
#Seccion acera
Ad2=705
print(f"Area de la seccion de acera: {Ad2} cm2")
#Seccion baranda
Ad3=375
print(f"Area de la seccion de baranda: {Ad3} cm2")
#Seccion poste
spost=200
print(f"Separacion entre postes: {spost} cm")
Ad4=26800/spost
print(f"Area equivalente distrobuida de la seccion de poste: {Ad4} cm2")
Ad=Ad1+Ad2+Ad3+Ad4+Adw
print(f"Area total de las secciones no estructurales: {Ad} cm2")
#Analisis de cargas
#Peso propio
wo=Acomp*gammac
print(f"Carga distribuida por peso propio: {wo} tonf/cm")
Po=Vdiaph*gammac
print(f"Carga puntual por diafragma: {Po} tonf")
#Carga muerta
wd=Ad*gammac
print(f"Sobrecarga muerta distribuida: {wd} tonf/cm")
#Camion de diseño
ptruck=14.5;    atruck=430;     btruck=180
ptandem=11;     atandem=120;    btandem=60
wlane=.0095
#Carga peatonal
wpl=.000036
print(f"Carga viva peatonal distribuida: {wpl} tonf/cm")
#Analisis estructural
struct1=struct.simpBeam(l)
Mo=struct1.Mdistmax(wo)+struct1.Mpuntmax(Po,nl)
Md=struct1.Mdistmax(wd)
mgmsi=0.06+(s/430)**.4*(s/l)**.3*(kg/l/ts**3)**.1
mgmse=1.2*(1+(de-btandem-btruck/2)/s)
mgmmi=.075+(s/290)**.6*(s/l)**.2*(kg/l/ts**3)**.1
mgmme=(.77+de/280)*mgmmi
mgme=max(mgmse,mgmme)
mgmi=max(mgmsi,mgmmi)
Mtruck=struct1.Mtruck(ptruck,atruck)
Mtandem=struct1.Mtandem(ptandem,atandem)
Mlane=struct1.Mlane(wlane)
Mpl=+struct1.Mdistmax(wpl)
Mlli=1.33*max(Mtruck,Mtandem)+Mlane
Ml=mgme*(Mlli)+Mpl
print(f"mgmsi={mgmsi}\nmgmse={mgmse}\nmgmmi={mgmmi}\nmgmme={mgmme}")
print(f"Mtruck={Mtruck}")
print(f"Mtandem={Mtandem}")
print(f"Mlane={Mlane}")
print(f"Mpl={Mpl}")
print(f"Ml={Ml}")
print(f"wo={wo}\tPo={Po}\twd={wd}")
print(f"Mo={Mo}\tMd={Md}\tMl={Ml}")

