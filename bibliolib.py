###############################
##                           ##
##   Made by Ilyas Casters   ##
##                           ##
###############################

from math import pi,log
from random import randint

hexAlphabet = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
hexAlphabetIndex = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
units = {"m":0,"dm":-1,"cm":-2,"mm":-3,"dam":1,"hm":2,"km":3}
sign = [1,-1]

#base64Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]


#Unit convertion
def celsius2Kelvin(t :float, reverse=False) :
    return t+(273,15*sign[float(reverse)])

def degre2Radian(a : float, reverse=False) :
    return a * (pi/180**sign[float(reverse)])

def lengthConvert(u1 :str, u2 :str, v :float) :
    ex1 = -units[u1]
    ex2 = -units[u2]
    return v*(10**ex1+ex2)

#Base convertion
def bin2Dec(n2:str, reverse=False):
    if reverse:
        r = n10%2
        q = n10//2
        n2 = str(r)
        while q != 0 :
            r = q%2
            q = q//2
            n2 = str(r) + n2
        return int(n2)
    else:
        n10 = 0
        for i in range(len(n2)):
            n10 += int(n2[i]) * 2 ** (len(n2)-i-1)
        return n10

def hex2Dec(n, reverse=False) -> int:
    if reverse:
        return bin2Hex(bin2Dec(n,True))
    else:
        ex = len(n)
        packs = [hexAlphabetIndex[e] for e in n]
        packs.reverse()
        n10 = 0
        for i in range(ex):
            n10 += packs[i]*(16**i)
        return n10

def bin2Hex(n:str, reverse=False) -> str :
    if reverse:
        return bin2Dec(hex2Dec(n),True)
    else:
        n = ("0"*((4-len(n2))%4))+ n
        ex = len(n)//4
        n16 = ""
        for i in range(ex):
            pack = n[i*4:i*4+4]
            packSum = int(pack[0])*8 + int(pack[1])*4 + int(pack[2])*2 + int(pack[3])
            n16 = n16 + hexAlphabet[packSum]
        return n16

#Swap
def swap( ls, i ,  j ):
    ls[i],ls[j]=ls[j],ls[i]
    return ls

def dSwap (ls , i , j):
  ls2 = ls[:]
  ls2[i],ls2[j]=ls2[j],ls2[i]

#Sorting
def selectSort(ls) :
    for i in range(0,len(ls)-1):
        swap( ls, i ,  i+searchMinimum(ls[i:]))

def dSelectSort(ls) :
    ls2 = ls[:]
    for i in range(0,len(ls2)-1):
        swap( ls2, i ,  i+searchMinimum(ls2[i:]))
    return ls2

def insertSort(ls) :
    for i in range(1,len(ls)):
        j = i
        while j > 0 and ls[j] < ls[j-1]:
        swap( ls, j ,  j-1 )
        j -= 1
def dInsertSort(ls) :
    ls2 = ls[:]
    for i in range(1,len(ls2)):
        j = i
        while j > 0 and ls2[j] < ls2[j-1]:
            swap( ls2, j ,  j-1 )
            j -= 1
    return ls2

#Statistics
def mean(ls:iter) -> float:
    return sum(ls)/len(ls)

def median(ls:iter) -> float:
    if len(ls) % 2:
        return (ls[len(ls)//2]+ls[(len(ls)//2)-1])/2
    else:
        return ls[len(ls)//2]

def randList(n:int,a:int,b:int) -> list:
   return [random.randint(a,b) for i in range(n)]

def searchMinimum(ls):
    index_mini=0
    for i in range (1,len(ls)):
        if ls[i]<ls[index_mini]:
            index_mini=i
    return index_mini

def searchMinimum(ls):
    index_maxi=0
    for i in range (1,len(ls)):
        if ls[i]>ls[index_maxi]:
            index_mini=i
    return index_maxi

def searchExtremum(ls):
    return searchMinimum(ls), searchMinimum(ls)



