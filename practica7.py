from math import *
from random import *
def pertenece(s:list[int], e:int)->bool:
    for element in s:
        if element==e:
            return True
    else: return False
    
def divide_a_todos(s:list[int], e:int)->bool:
    for element in s:
        if element%e!=0:
            return False
    else: return True 

def suma_a_total(s:list[int])->int:
    x=0
    for element in s:
        x=x+element
    else:return x

def ordenados(s:list[int])->bool:
    x=None
    for element in s:
        if x!=None and element<=x:
                return False
        x=element
    else:return True

def palabra_larga(s:list[str])->bool:
    for element in s:
        if len(element)>7:
            return True
    else: return False 

def palindromo(s:str)->bool:
    x=''
    for element in s:
        x=element+x
    if x==s:
        return True
    else: return False

def fortaleza(s:str)->str:
    if len(s)>8:
        for element in s:
            if element in "abcdefghijklmnopqrstuvwxyz":
                break
        else: return False
        for element in s:
            if element in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                break
        else: return False
        for element in s:
            if element in "0123456789":
                break
        else:return False
        return "VERDE"
    elif len(s)<5:
        return "ROJO"
    else: return "AMARILLA"

def calcular_saldo(s:list[('str', float)])->float:
    x=0
    for element in s:
        if "I" in element:
            for elemento in element:
                if type(elemento)==int:
                    x=x+elemento
        if "R" in element:
            for elemento in element:
                if type(elemento)==int:
                    x=x-elemento
    else: return x

def vocales(s:str)->bool:
    x="aeiou"
    y=0
    for element in x:
        if element in s:
            y=y+1
        if y==3:
            return True
    else: return False

def lista_pares(s:list[float])->list[float]:
    x=1
    y=[]
    for element in s:
        if x%2==0:
            x=1
            y.append(0)
        else: 
            x=x+1
            y.append(element)
    else: 
        return y
    
def sin_vocales(s:str)->str:
    x="aeiou"
    z=''
    for element in x:
        for elemento in s:
            if element==elemento:
                z=z+''
            else: z=z+elemento
        else: 
            s=z
            z=''
    else: return s

def reemplazar_vocales(s:str)->str:
    x="aeiou"
    z=''
    for element in x:
        for elemento in s:
            if element==elemento:
                z=z+'-'
            else: z=z+elemento
        else: 
            s=z
            z=''
    else: return s

def dar_vuelta_str(s:str)->bool:
    x=''
    for element in s:
        x=element+x
    else: return x

def eliminar_repetidos(s:list[str])->list[str]:
    x=0
    y=[]
    for element in s:
        if element not in y:
         y.append(element)
    else: return y

def aprobado(notas:list[int])->int:
    x=0
    y=0
    for element in notas:
        if element>=4:
            x=x+element
            y=y+1
        else: return 3
    else:
        promedio= x/y 
        if promedio>=7:
            return 1
        elif 4<=promedio<7:
            return 2
            
def lista_alumnos():
    y=[]
    alumnos=''
    while alumnos!="listo":
        alumnos= input("Ingrese el nombre del alumnos ")
        y.append(alumnos)
    else: return y

def cargar_sube():
    operacion=""
    cantidad=''
    lista=[]
    while operacion!="X":
        operacion=input("Ingrese operacion: ")
        if operacion=="C":
            cantidad=input("Ingrese cantidad a cargar: ")
            lista.append((operacion,cantidad))
        elif operacion=="D":
            cantidad=input("Ingrese cantidad a cargar: ")
            lista.append((operacion,cantidad))
    else: return lista

def suma_especial(s:list[int])->int:
    x=0
    for element in s:
        if element in [10,11,12]:
            x=x+0.5
        else: x=x+element
    else:return x

def siete_y_medio():
    carta=choice([1,2,3,4,5,6,7,10,11,12])
    historial=[]
    eleccion=""
    while eleccion!="plantarse":
        historial.append(carta)
        if suma_especial(historial)==7.5:
            return ("ganaste", historial)
        elif suma_especial(historial)>7.5:
            return ("perdiste", historial, suma_especial(historial))
        else: eleccion=input(f'Su carta es {carta}, decida que hacer: ')
        carta=choice([1,2,3,4,5,6,7,10,11,12])
    else: return (suma_especial(historial), historial)

def pertenece_a_cada_uno_version_1(s:list[int], e:int)->list[bool]:
    res=[]
    expandir= randint(1,5)
    verdad=bool(randint(0,1))
    for element in s:
        res.append(pertenece(element,e))
    for element in range(expandir):
        res.append(verdad)
        verdad=bool(randint(0,1))
    else: return res

def pertenece_a_cada_uno_version_2(s:list[list[int]], e:int)->list[bool]:
    res=[]
    for element in s:
        res.append(pertenece(element,e))
    else: return res

def es_matriz(s:list[list[int]])->bool:
    x=0
    if len(s)>0:
        for element in s:
            while x== 0:
                x=len(element)
            if len(element)!=x:
                return False
        else: return True

def filas_ordenadas(m:list[list[int]])->list[bool]:
    lista=[]
    for element in m:
        lista.append(ordenados(element))
    else: return lista

import numpy as np

def matriz_potencia(d:int,p:int)->np.ndarray:
    m = np.random.randint(0,20,(d, d))    
    x=0
    y=0
    z=0
    matriz=[]
    a=[]
    n=m
    for element in m:           
            while p!=1:
                for hola in n:
                    while z<len(element):
                        for elemento in hola:
                            y=y+elemento*m[x][z]
                            x=x+1
                        else: 
                            matriz.append(y)
                            z=z+1
                            x=0
                            y=0
                    else: 
                        x=0
                        z=0
                        a=a+[matriz]
                        matriz=[]
                else:
                    n=a
                    p=p-1
                    a=[]
    return m,np.array(n) 

print(pertenece([1,2,3], 3), divide_a_todos([2,4,6], 2), suma_a_total([1,2,3,4]), ordenados([1,2,3]), 
      palabra_larga(["holamund"]), palindromo("neuque"), fortaleza("Matribur12"), calcular_saldo([("I",2000),
    ("R", 20),("R", 1000),("I", 300)] ), vocales("holae"), lista_pares([1,2,5,4]), sin_vocales("holamundo"),
      reemplazar_vocales("hola mundo"), dar_vuelta_str("hola mundo"), eliminar_repetidos(["hola", "mundo", "hola", "chau"]),
      aprobado([4,1,10]), pertenece_a_cada_uno_version_2([[1,2,3,2,3,2], [0]], 2), es_matriz([[0,1], [1,2]]),
      filas_ordenadas([[0,1], [1,0]]),matriz_potencia(3,2))
