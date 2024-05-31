from queue import LifoQueue, Queue
from random import *

def contar_lineas(nombre_archivo:str)->int:
    archivo=open(nombre_archivo,"r")
    contenido=archivo.readlines()
    archivo.close()
    return len(contenido)

def existe_palabra(palabra:str, nombre_archivo:str)->bool:
    lista=""
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    for element in contenido:
        if element not in [" ", ".", "\n", "(", ")", ","]:
            lista=lista+element
        elif lista==palabra:
            return True
        else: 
            lista=""
    if palabra ==lista:  
        return True
    else:
        print(lista, len(lista))
        return False
            
def cantidad_de_apariciones(palabra:str, nombre_archivo:str)->int:
    contador=0
    lista=""
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    for element in contenido:
        if element not in [" ", ".", "\n", "(", ")",","]:
            lista=lista+element
        elif lista==palabra:
            contador+=1
        else: 
            lista=""
    if palabra ==lista:  
        return contador+1
    else:
        return contador

def clonar_sin_comentarios(nombre_del_archivo:str)->None:
    archivo=open(nombre_del_archivo,"r")
    contenido=archivo.readlines()
    archivo.close()
    texto=""
    nuevo=open("clonado.txt", "w")
    contador=0
    for element in contenido:
        if element[0]!="#" and element[0]!=" ":
            texto=texto+element
        while element[contador]==" ":
            if element[contador+1]==" ":
                contador+=1
            elif element[contador+1]=="#":
                contador=0
                break
            else: 
                texto=texto+element
                contador+=1
        else:
            contador=0 
    else:
        nuevo.writelines(texto)
        nuevo.close()
        
def invertir_lineas(nombre_del_archivo)->None:
    archivo=open(nombre_del_archivo, "r")
    contenido=archivo.readlines()
    archivo.close()
    contador=len(contenido)-1
    texto=""
    while contador!=0:
        if contador==len(contenido)-1:
            texto=texto+contenido[contador]+"\n"
        else:texto=texto+contenido[contador]
        contador-=1
    else: texto=texto+contenido[0]
    nuevo=open("reverso.txt", "w")
    nuevo.writelines(texto)
    nuevo.close()

def agregar_frase_al_final(nombre_archivo:str, frase:str)->None:
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    archivo=open(nombre_archivo,"w")
    archivo.writelines(contenido+"\n"+frase)
    archivo.close()
    
def agregar_frase_al_inicio(nombre_archivo:str, frase:str)->None:
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    archivo=open(nombre_archivo,"w")
    archivo.writelines(frase+"\n"+contenido)
    archivo.close()

def listar_palabras_de_un_archivo(nombre_del_archivo:str)->list[str]:
    archivo=open(nombre_del_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    palabra=''
    lista_palabras=[]
    for element in contenido:
        if element not in [" ", ".", "\n", "(", ")", ","]:
            palabra=palabra+element
        elif len(palabra)>=5:
            lista_palabras.append(palabra)
            palabra=""
        else: palabra=''
    if len(palabra)>=5:
        lista_palabras.append(palabra)
        return lista_palabras
    else: return lista_palabras
    
def listar_todas_palabras_de_un_archivo(nombre_del_archivo:str)->list[str]:
    archivo=open(nombre_del_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    palabra=''
    lista_palabras=[]
    for element in contenido:
        if element not in [" ", ".", "\n", "(", ")", ","]:
            palabra=palabra+element
        elif palabra!="":
            lista_palabras.append(palabra)
            palabra=""
    else:
        lista_palabras.append(palabra)
        return lista_palabras

def promedio_estudiante(nombre_archivo:str, lu : str)->float:
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivo.close
    lista_palabras=listar_todas_palabras_de_un_archivo(nombre_archivo)
    notas=[]
    while lu in lista_palabras:
        posicion=lista_palabras.index("nota", lista_palabras.index(lu))
        lista_palabras.remove(lu)
        notas.append(int(lista_palabras[posicion]))
    else: return sum(notas)/len(notas)
    
def promedio_por_estudiante(nombre_archivo_notas:str,nombre_archivo_promedio:str):
    archivo=open(nombre_archivo_notas, "r")
    lista_palabras=listar_todas_palabras_de_un_archivo(nombre_archivo_notas)
    archivo.close()
    texto=''
    alumnos=[]
    print(lista_palabras)
    while "LU" in lista_palabras:
        estudiante=lista_palabras.index("LU")+1
        LU=lista_palabras[estudiante]
        if LU not in alumnos:
            texto=texto+f'{lista_palabras[estudiante]}, promedio({promedio_estudiante(nombre_archivo_notas, LU)}) \n'
            alumnos.append(LU)
        while LU in lista_palabras:
            indice=lista_palabras.index(LU)-1
            lista_palabras.pop(indice)
            lista_palabras.remove(LU)
    else:
        archivo=open(nombre_archivo_promedio,"w")
        archivo.writelines(texto)
        archivo.close()
        
def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->LifoQueue[int]:
    pila=LifoQueue(maxsize=cantidad)
    while not pila.full():
        pila.put(randint(desde,hasta))
    else: return pila

def cantidad_de_elementos(p:LifoQueue)->int:
    lista=[]
    contador=0
    while not p.empty():
        lista.append(p.get())
        contador+=1
    while lista!=[]:
        p.put(lista[0])
        lista.pop(0)
    else:return contador
    
def buscar_maximo(p:LifoQueue)->int:
    copia=p
    lista=[]
    while not copia.empty():
        lista.append(copia.get())
    while len(lista)!=1:
        if lista[0]>=lista[1]:
            lista.remove(lista[1])
        else: lista.remove(lista[0])
    else:return lista[0]

# def esta_bien_balanceda(s:str)->bool:
#     while "(" in s:
#         indice=s.index("(")
#         ind=s.index(")")
#         if s.count("(")!=s.count(")"):
#             return False
#         elif indice>ind:
#             return False
#         else: 
#             s=s.replace("(","",1)
#             s=s.replace(")","",1)
#     else:return True (esta mas fachera y mas facil.PD: las pilas son una mierda)

def esta_bien_balanceada(s:str)->bool:
    pila=LifoQueue()
    contador=0
    guardar=""
    indice=0
    while indice!=len(s):
        pila.put(s[indice])
        indice+=1
    while not pila.empty():
        guardar=pila.get()
        if guardar==')':
            while guardar!="(":
                guardar=pila.get()
                if pila.empty():
                    return False
                elif guardar==")":
                    contador+=1
            else:
                for element in range(contador):
                    pila.put(")")
                else:
                    contador=0
        elif guardar=="(":
            return False
    else: return True
            
print(esta_bien_balanceada("1 + ( 2 * 3 - ( 2 0 / 5 ) )"))
print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( -1)))"))
print(esta_bien_balanceada("1 + ) 2 * 3 ( ( )"))