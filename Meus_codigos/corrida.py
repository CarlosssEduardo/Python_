def onibus (b1, b2):
    print(115*"-")
    print( (b1*" ") + "__________________________"           + ((100-b1) *" " ) + "|" )
    print( (b1*" ") + "|____|____|____|____|____|____"       + ((97-b1) *" ") + "|" )
    print( (b1*" ") + "|    CURUÇAMBA VER O PESO     |"      + ((96-b1) *" ") + "|" )
    print( (b1*" ") + "|-----o-----------------o-----|"      + ((96-b1) *" ") + "|" )
    print(115*"_")
    print( (b2*" ") + "__________________________"           + ((100-b1) *" " ) + "|" )
    print( (b2*" ") + "|____|____|____|____|____|____"       + ((97-b1) *" ") + "|" )
    print( (b2*" ") + "|    C.NOVA 6 P-VARGAS        |"      + ((96-b1) *" ") + "|" )
    print( (b2*" ") + "|-----o-----------------o-----|"      + ((96-b1) *" ") + "|" )
    print(115*"_")
    return "CORRIDA DE ÔNIBUS"

import time
import os
from random import randint

a = 0
b = 0 
print("CORRIDA DE ÔNIBUS!!")
print("CURUÇAMBA VER O PESO VS C.NOVA 6 P-VARGAS")
time.sleep(3)
os.system("cls")

while (a < 97) and (b < 97):
     c = randint(1,2)
     if c ==  1:
          a += 1
     if c == 2:
          b += 1
     os.system("cls")
     print(onibus(a,b))
     time.sleep(0.05)

if a == 97:
     vencedor = "CURUÇAMBA VER O PESO"
if b == 97:
     vencedor = "C.NOVA 6 P-VARGAS" 
print(f"VENCEDOR DA CORRIDA E---> {vencedor}")