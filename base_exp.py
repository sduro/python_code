import sys
#Calculate the exponential 

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    index=0
    resultado=base
    if base==1 or exp==0:
        return 1
    if base ==0:
        return 0
    for index in (range(exp-1)):
        resultado=resultado*base
    return resultado

def main():
    try:
        print(iterPower(int(sys.argv[1]),int(sys.argv[2])))
    except:
        print ("Faltan argumentos\nUsar como base_exp.py [base] [exponente] ")
    
if __name__ == '__main__':
    main()



