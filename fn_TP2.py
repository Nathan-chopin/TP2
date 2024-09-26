# fonction du TP2
# Nathan Chopin
# 26/09/24
# l'implémentation de la lecture du fichier.txt (creation_dictionnaire()) ne fonctionne pas


import os


dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}
# article:0 , adjectif:1 , nom:2 , verbe:3 , nom propre:4 , ".":5

                # art,adj,nom,vb,nprop,"."
transition_etat = [[1,8,8,8,4,8], #0
                   [8,1,2,8,8,8], #1
                   [8,2,8,3,8,8], #2 
                   [5,8,8,8,7,9], #3
                   [8,8,8,3,8,8], #4
                   [8,5,6,8,8,8], #5
                   [8,6,8,8,8,9], #6
                   [8,8,8,8,8,9], #7
                   [8,8,8,8,8,8], #8
                   [9,9,9,9,9,9]] #9

###################################################################################################################################################################

def separation(list,caractere):
    '''sépare dans un élément d'une liste un mot et un caractère'''
    if len(list) == 0:          # cas liste vide
        return []
    
    
    elif len(list) == 1:        # cas liste de 1 élément
        if list == ['']:           # cas liste à 1 élément dont le str est vide
            return ['']
        elif list[0][0] == caractere:             # caractère au début
            return [list[0][1:]]                  # assenblage de la liste sans le caractère
        elif list[0][len(list[0]) - 1] == caractere :   # caractère à la fin
            return list[0][:len(list[0])]     # assenblage de la liste sans le caractère
    
    
    for i in range(len(list) - 1):                           # idem mais pour une liste de taille n >= 2
        if list[i][0] == caractere :
            list = list[:i] +  [list[i][1:]] + list[i + 1:]  # assenblage de la liste sans le caractère
        elif list[i][len(list[i]) - 1] == caractere :        
            list = list[:i]  + [list[i][:len(list[i]) - 1]] + list[i:]  # assenblage de la liste sans le caractère
            list.remove(list[i - 1])
    return list

############################################################################################################################################################################

def creation_dictionnaire():
    fichier = open("dico.txt","r")
    dic = {}
    for ligne in fichier.readlines():
        for i in range(len(ligne)):
            if ligne[i] == ' ':
                dic[ligne[:i]] = int(ligne[i + 1:].rstrip())
    fichier.close()
    return dic

print(creation_dictionnaire())
#################################################################################################################################################################

def correcteur(phrase):
    '''dit si une phrase est correcte ou pas'''
    etat = 0                # état et valeur associé au mot initiallement
    val_mot = 0
    dictionnaire = creation_dictionnaire()

    def etat_final(etat = 0):
        '''renvois l'état final de cet automate'''
        if etat == 9 or etat != 8:     
            print('phrase incorrecte') 
            return False                
        else :
            print("phrase correcte")
            return True
    

    list_mot = phrase.split(" ")
    list_mot = separation(list_mot,',')
    list_mot = separation(list_mot,'.')  

    if phrase == "":        # cas où il n'y a pas de phrase
        return etat_final()
    else:
        for mot in list_mot:
            if mot not in dictionnaire.keys() and mot != ';' and mot != ',':        # cas où le mot n'est pas dans le dic
                return etat_final()
            elif mot != ';' and mot != ',':
                val_mot = dictionnaire[mot]
                etat = transition_etat[etat][val_mot]     # réalise un changement d'état
    return etat_final(etat)

