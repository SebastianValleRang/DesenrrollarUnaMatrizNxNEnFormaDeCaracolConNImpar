#matriz = [[1,2,3],[4,5,6],[7,8,9]]

matriz = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

""" ponemos el numero de fila o columna ya que esta es una matriz cuadrada """
w = 5

caracol = "";

a = w - 1

""" superior """

acot_sup_ini_fil = 0
acot_sup_ini_col = 0

acot_sup_fin_fil = 0
acot_sup_fin_col = a


""" derecha """

acot_der_ini_fil = 0
acot_der_ini_col = a

acot_der_fin_fil = a
acot_der_fin_col = a

""" abajo """

acot_aba_ini_fil = a
acot_aba_ini_col = a

acot_aba_fin_fil = a
acot_aba_fin_col = 0

""" izquierda """

acot_izq_ini_fil = a
acot_izq_ini_col = 0

acot_izq_fin_fil = 1
acot_izq_fin_col = a

#----------------------------- DIMENSION IMPAR --------------------------------------------------


centro = (w/2) + 0.5 - 1
reduccion = w
print (centro)
ncentro = matriz[int(centro)][int(centro)]

print(ncentro) 

#reducir cascaron

while reduccion != 1:

    for i in range(acot_sup_ini_col,acot_sup_fin_col):
    
        caracol = caracol + str(matriz[acot_sup_ini_fil][i])+","
        

    for i in range(acot_der_ini_fil,acot_der_fin_fil):

        caracol = caracol + str(matriz[i][acot_der_ini_col])+","
    

    for i in range (acot_aba_ini_col, acot_aba_fin_col , -1):

        caracol = caracol + str(matriz[acot_aba_ini_fil][i])+","

    
    for i in range(acot_izq_ini_fil,acot_izq_fin_fil,-1):
    
        caracol = caracol + str(matriz[i][acot_izq_ini_col])+","

    reduccion = reduccion - 2

    print(acot_izq_fin_fil)
    print(acot_izq_fin_col)
    
    caracol = caracol+str(matriz[acot_izq_fin_fil][acot_izq_ini_col])+","

    if(reduccion != 1):

        #caracol = caracol + str(matriz[i][acot_izq_ini_col])

        acot_sup_ini_fil = acot_sup_ini_fil + 1
        acot_sup_ini_col = acot_sup_ini_col + 1

        acot_sup_fin_fil = acot_sup_fin_fil + 1
        acot_sup_fin_col = acot_sup_fin_col - 1


        """ derecha """

        acot_der_ini_fil = acot_der_ini_fil + 1
        acot_der_ini_col = acot_der_ini_col - 1

        acot_der_fin_fil = acot_der_fin_fil - 1
        acot_der_fin_col = acot_der_fin_col - 1

        """ abajo """

        acot_aba_ini_fil = acot_aba_ini_fil - 1
        acot_aba_ini_col = acot_aba_ini_col - 1

        acot_aba_fin_fil = acot_aba_fin_fil - 1
        acot_aba_fin_col = acot_aba_fin_col + 1

        """ izquierda """

        acot_izq_ini_fil = acot_izq_ini_fil - 1
        acot_izq_ini_col = acot_izq_ini_col + 1

        acot_izq_fin_fil = acot_izq_fin_fil + 1
        acot_izq_fin_col = acot_izq_fin_col + 1






#reduccion a vector


caracol = caracol+str(matriz[int(centro)][int(centro)])

print(caracol)








