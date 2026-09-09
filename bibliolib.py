###############################
##                           ##
##   Made by Ilyas Casters   ##
##                           ##
###############################

#/!\ Note: L'ensemble du code est rester sur mon espace de travail personnel /!\

import math,random

hexAlphabet = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
hexAlphabetIndex = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
#base64Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]

def bin2Hex(n2:str) -> str :
   n2 = ("0"*((4-len(n2))%4))+ n2
   ex = len(n2)//4
   n16 = ""
   for i in range(ex):
      pack = n2[i*4:i*4+4]
      packSum = int(pack[0])*8 + int(pack[1])*4 + int(pack[2])*2 + int(pack[3])
      n16 = n16 + hexAlphabet[packSum]
   return n16

def hex2Dec(n16:str) -> int:
   ex = len(n16)
   packs = [hexAlphabetIndex[e] for e in n16]
   packs.reverse()
   n10 = 0
   for i in range(ex):
      n10 += packs[i]*(16**i)
   return n10
    
def dec2Bin(n10:str) -> str:
  r = n10%2
  q = n10//2
  n2 = str(r)
  while q != 0 :
    r = q%2
    q = q//2
    n2 = str(r) + n2
  return n2

def mean(liste:iter) -> float:
    return sum(liste)/len(liste)

def randList(n:int,a:int,b:int) -> list:
   return [random.randint(a,b) for i in range(n)]


