from stack import Stack

def convertisseur(op):
pile=Stack()
operateur={'+':+,'-':-,'*':*}
    for l in op:
        resultat=0
        pile.push(l)
        if l in operateur:
            for i in range (2):
                pile.pop()
            
            