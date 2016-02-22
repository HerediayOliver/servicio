def main ():
    funcion = raw_input("Dame la función: ")
    h = double(raw_input("Dame el periodo h: "))
    y0 = double(raw_input("Dame el valor de y0: "))    
    x0 = double(raw_input("Dame el valor de x0: ")) 
    valoresX = [0]*5
    valoresY = [0]*5
    valoresX[0]=x0
    valoresY[0]=y0

def unaFuncion(x,y):
    funcion
    return (funcion)

def metodo(x0,y0,h):
     k1 = h*funcion(x0, y0)
     k2 = h*funcion(x0 + (h/2), y0 + (k1/2))
     k3 = h*funcion(x0 + (h/2), y0 + (k2/2))
     k4 = h*funcion(x0 + h, y0 + k3)

     y = y0 + 1/6*(k1 + 2k2 2k3 + k4)

     return [x,y,k1,k2,k3,k4]
 
     cont = 0
     while(cont<5):
     
     resultado= metodo(valoresX[cont],valoresX[cont],h)
     valoresX[cont+1] = resultado[0]
     valoresY[cont+1] = resultado[1]
     cont = cont + 1

     
     print "Resultado %f" %(cont+1) 
     print "x   y   k1   k2   k3   k4"
     print  resultado
     print "  "