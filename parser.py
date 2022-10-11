from stack import Stack     

def pars_checker(string):
    pile=Stack()
    codes={')':'(', ']':'[', '}':'{'}
    for l in string:
        if l in codes.values():
            pile.push(l)
        
        elif l in codes.keys():
            try: #si le dernier (en haut) element de la pile est "(" enleve le
                if pile.summit()==codes[l]:
                    pile.pop()
                else:
                    return False
            except IndexError: #sauf si il y a pas d'element
                return False
                
    return pile.size()==0
    
        


expressions =['2x(x+1)','2x((x+1)','2x+1)', '2x(x+1)(x+2)(x+3)','2x(x+1)(x+2)((x+3)','2x(x+1)(x+2))(x+3)','','(','()',')(']

