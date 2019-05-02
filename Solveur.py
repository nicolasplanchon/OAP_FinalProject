import os

# Change le répertoire de base pour trouver le fichier
os.chdir("C:/Users/Alexandre Le Texier/Desktop/OAP/Projet final/Programmes/Python")

# Création du fichier instance à remplir
instance=[[-1,-1,-1,-1,-1,-1,-1],[],[-1],[-1,-1,-1],[],[],[]]

# Index récurrents
IdxInfoG = 0 #Informations générales
IdxProd = 1 # Produits
IdxCmd = 2 # Commandes
IdxInfGra = 3 # Information générale du graphe
IdxArc = 4 # Arcs du graphe
IdxChemin = 5 # Plus court chemin du graphe
IdxLocNom = 6 # Coordonnées et noms de localisation

# Ouverture du fichier en mode lecture
fichier = open("Instances/instance_0116_131940_Z2.txt", "r")

## Parcours du fichier

#Informations générales
fichier.readline()
instance[IdxInfoG][0]=int(fichier.readline()) #Nblocations
fichier.readline()
fichier.readline()
instance[IdxInfoG][1]=int(fichier.readline()) #NbProducts
fichier.readline()

fichier.readline()
instance[IdxInfoG][2]=int(fichier.readline()) #NbBoxesTrolley
fichier.readline()

fichier.readline()
instance[IdxInfoG][3]=int(fichier.readline()) #NbD
fichier.readline()

fichier.readline()
temp=fichier.readline()
temp=temp.split()
instance[IdxInfoG][4]=int(temp[0]) #NbCapaboxWei
instance[IdxInfoG][5]=int(temp[1]) #NbCapaboxVol
fichier.readline()

fichier.readline()
instance[IdxInfoG][6]=int(fichier.readline()) #BoxMixedOrder
fichier.readline()


fichier.readline()
fichier.readline()

while 0==0:
    temp=fichier.readline().split()

    if temp==[]:
        break
    else:
        for i in range(len(temp)):
            temp[i]=int(temp[i])
        instance[IdxProd].append(temp)
fichier.readline()

# Commandes
fichier.readline()
instance[IdxCmd][0] = int(fichier.readline())
fichier.readline()


while 0==0:
    temp=fichier.readline().split()
    if temp==[]:
        break
    else:
        order=[]
        order.append(int(temp[0]))
        order.append(int(temp[1]))
        order.append(int(temp[2]))
        for i in range(3,len(temp),2):
            product=[]
            product.append(int(temp[i]))
            product.append(int(temp[i+1]))
            order.append(product)
        instance[IdxCmd].append(order)
fichier.readline()

# Information générale du graphe
fichier.readline()
instance[IdxInfGra][0] = int(fichier.readline())
fichier.readline()

fichier.readline()
instance[IdxInfGra][1] = int(fichier.readline())
fichier.readline()

fichier.readline()
instance[IdxInfGra][2] = int(fichier.readline())
fichier.readline()

# Arcs du graphe

fichier.readline()
fichier.readline()

while 0==0:
    temp=fichier.readline().split()

    if temp==[]:
        break
    else:
        for i in range(len(temp)):
            temp[i]=int(temp[i])
        instance[IdxArc].append(temp)
fichier.readline()

# Plus court chemin du graphe, [i][j] donne la longueur du chemin le plus court pour aller de i à j. Il donne infini si cela n'est pas possible.

infini = 99999999999999999999
roads=[[] for i in range(instance[IdxInfoG][0]+1)]

for i in range(instance[IdxInfoG][0]+1):
    roads[i]=[infini for i in range(instance[IdxInfoG][0]+2)]
for i in range(len(roads)):
    roads[i][i]=0

while 0==0:
    temp=fichier.readline().split()

    if temp==[]:
        break
    else:
        roads[int(temp[0])][int(temp[1])]=int(temp[2])

instance[IdxChemin]=roads
fichier.readline()


# Coordonnées et noms de localisation, [i] donne les informations du point i
fichier.readline()

while 0==0:
    temp=fichier.readline().split()

    if temp==[]:
        break
    else:
        del temp[0]
        temp[0]=int(temp[0])
        temp[1]=int(temp[1])
    instance[IdxLocNom].append(temp)


# Fermeture du fichier

fichier.close()

print("Importation du fichier avec succès !")