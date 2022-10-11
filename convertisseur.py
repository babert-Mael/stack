from stack import Stack

def calcul(operation):
    """
    une fonction qui permet de faire de calcul en ecriture polonaise inverse
    operation étant une chaine de caractère
    """
    
    pile=Stack()
    operateur=('+', '-', '*', '^')
    for c in operation:
      resultat=0
      if c not in operateur: # si c n'est pas un operateur
          pile.push(c) # met la valeur dans la pile
      else:
        op1=int(pile.pop()) # op1 est égale à la valeur en haut de la pile
        op2=int(pile.pop()) # op2 est égale à la valeur en bas de la pile
        if c=='*': # si le caracter est égale à * fait une multiplication des opérateur
          resultat=op2 * op1
        elif c=='+': # si le caractere est égale à + fait un addition des deux multiplicateur
          resultat= op2 + op1
        elif c=='-': #si le caractere est égale à - fait une soustraction des deux opérateurs
          resultat=op2-op1
        elif c=='^': #si le caractere est égale à ^ fait une puissance des deux opérateurs
            resultat=op2**op1  
        pile.push(resultat)
    return pile.pop()
