def importTable(fileName:str):
    try:
        file = open(fileName+".csv","r")
    except OSError:
       return []
    
    ls =[]
    key = file.readline().strip("\n").split(",")

    for ln in file.readlines():
        dict= {}
        ln_split = ln.strip("\n").split(",")

        for i in range(len(key)):
            dict[key[i]] = ln_split[i]
        ls.append(dict)
        
    file.close()
    return ls

def printTable(tab:list,name:str):
    print(name)
    ks = tab[0].keys()
    print("   |   ".join(ks))
    for e in tab:
        print("   |   ".join(e.values()))

    maVar="exemple"
    maVar2="texte"
    print(f"sur 15 caractères :{maVar:15} et {maVar2:15}. ")

achats = importTable('achats')
clients = importTable('clients')
produits = importTable('produits')

printTable(achats,"Achats")

