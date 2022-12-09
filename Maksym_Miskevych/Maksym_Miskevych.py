
from math import *
from xml.etree.ElementTree import PI # * - koik funktsionid moodulist
#import math      math.funnktsion
#print("tere tulemast!") #ввод информации на экран
#nimi=input("Mis on sinu nimi on?") #ввод пользователем input()--str
#print() #пустая строка
##print(f"{nimi}, sul on vaga ilus nimi!")
##print(nimi,", sul on vaga ilus nimi!) #, -> tuhik
##print(nimi+", suk on vaga ilus nimi!") #str+str
#vanus=int(input("kui vana sa oled")) #int(str)
#print(nimi,"sa oled",vanus,"aastat vana")
#vanus+=10
#print(nimi+",1 10 aasta parast sa oled"+str(vanus)+"aastat vana")
print()
print("Vordse pindalaga ristkulik ja ring")
a=float(input("anna laius: "))
b=float(input("anna koigus: "))
S=a*b #-,+,**,/,sqrt,//,%
P=2*a+2*b
d=sqrt(a**2+b**2)
print(f"Pindala = {S}\nLabimoot ={P}\nDiagonaal = {d}")
d=round(sqrt(a**2+b**2),2) #umardamine 
print(f"Pindala = {S}\nLabimoot = {P}\nDiagonaal = {d}")
print("Ringi raadius ")
Pi=3.14
r=sqrt(S/Pi)
print(r)