def contar_rutas_mas_cortas(C):

    lim = len(C)-1
    if  C[lim][lim] == 1:
        return 0
    else:
        if vefPosiailidad(C, lim) == -1:
            return 0
        C[lim][lim] = 't'
        x = verColumna(C, lim, 1,0,0)+1
        if x == 3:
            return x+1
        else:
            return x


def verColumna(C, lim, i, posRutas, contador):

    if lim != -1:

        if lim == len(C)-1:

            if i> len(C)-1:
                if C[i-1][lim] == 't':
                    return verColumna(C, lim-1, 1 , posRutas+1, contador+1 )
            
                elif C[i-1][lim] == 0:
                    C[i-1][lim] = 'a'
                    return verColumna(C, lim, i+1, posRutas, contador )
                else:
                    return verColumna(C, lim-1, 1 , posRutas, contador+1)

            elif C[i][lim] == 't':
                return verColumna(C, lim-1, 1 , posRutas+1, contador+1 )
            
            elif C[i][lim] == 0:
                C[i][lim] = 'a'
                return verColumna(C, lim, i+1, posRutas, contador )
            else:
                return verColumna(C, lim-1, posRutas, contador+1)
        elif i <= len(C)-1:

            if C[i][lim] == 0:
                if C[i][lim+1] == 'a':
                    C[i][lim] = 'a'
                    return verColumna(C, lim, i+1, posRutas+1*contador, contador)

                elif C[i][lim+1] == 't':
                    C[i][lim] = 'a'
                    return verColumna(C, lim-1, 1, posRutas+1*contador, contador+1)
                else:
                    return verColumna(C, lim-1, 1, posRutas, contador+1)
            else:
                return verColumna(C, lim-1, 1, posRutas, contador+1)
        else:
            return verColumna(C, lim-1, 1, posRutas, contador+1)

    else:
        return posRutas

def vefPosiailidad(C,lim):
    i = lim
    x = False
    t = False
    while (i != -1):
        if C[i][lim] == 1:
            x = True
        i -= 1
    i = lim
    while(i != -1):
        if C[lim][i] == 1:
            t = True
        i -= 1
    if x == True and t == True:
        return -1
    else:
        return 1
