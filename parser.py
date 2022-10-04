from stack import Stack

p=Stack()


        

def pars_checker(string):
    pile=Stack()
    for l in string:
        if l=='(':
            pile.push(l)
        elif l==")":
            try:
                pile.pop()
            except IndexError:
                return False
    return pile.size()==0
    
        


expressions =['2x(x+1)','2x((x+1)','2x+1)', '2x(x+1)(x+2)(x+3)','2x(x+1)(x+2)((x+3)','2x(x+1)(x+2))(x+3)','','(','()',')(']

