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

def cantidad_elementos(p:LifoQueue)->int:
    lista=[]
    contador=0
    while not p.empty():
        lista.append(p.get())
        contador+=1
    while lista!=[]:
        p.put(lista[0])
        lista.pop(0)
    else:return contador
    
def buscar_maximo(pila:LifoQueue[int])->int:
    maximo=None
    while not pila.empty():
        numero=pila.get()
        if maximo==None or maximo<numero:
            maximo=numero
    else:return maximo

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
                if pila.empty() and  guardar!="(":
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
            
def evaluar_expresion(s:str)->float:
    pila=LifoQueue()
    indice=len(s)-1
    guardar=""
    numeros=LifoQueue()
    resultado=0
    numero=""
    while indice!=-1:
        pila.put(s[indice])
        indice-=1
    while not pila.empty():
        guardar=pila.get()
        if "0"<=guardar<="9":
            while "0"<=guardar<="9":
                numero=numero+guardar
                guardar=pila.get()
            else: 
                numeros.put(numero)
                numero=""
        elif  guardar in ["+", "-", "*", "/"]:
            resultado=cuentas(float(numeros.get()), guardar, float(numeros.get()))
            numeros.put(resultado)
            resultado=0
    else: return numeros.get()

def cuentas(numero:float,operador:str,numero2:float)->float:
    if operador=="/":
        return numero2/numero
    elif operador=="+":
        return numero + numero2
    elif operador=="-":
        return numero2-numero
    else:
        return numero*numero2

def armar_cola(cantidad:int,desde:int,hasta:int)->Queue[int]:
    pila:LifoQueue[int]=generar_nros_al_azar(cantidad,desde,hasta)
    cola:Queue[int]=Queue()
    while not pila.empty():
        cola.put(pila.get())
    else: return cola

def cantidad_de_elementos(cola:Queue)->int:
    contador=0
    while not cola.empty():
        cola.get()
        contador+=1
    return contador

def buscar_el_maximo(cola:Queue[int])->int:
    maximo=None
    while not cola.empty():
        numero=cola.get()
        if maximo==None or maximo<numero:
            maximo=numero
    else:return maximo
    
def armar_carton_de_bingo()->Queue[int]:
    cola=Queue(maxsize=12)
    lista=[]
    for element in range(100):
        lista.append(element)
    while not cola.full():
        numero=choice(lista)
        lista.remove(numero)
        cola.put(numero)
    else: return cola
    
def jugar_carton_de_bingo(carton:list[int], bolillero:Queue[int])->int:
    contador=0
    while carton!=[]:
        numero=bolillero.get()
        if numero in carton:
            contador+=1
            carton.remove(numero)
        else: contador+=1
    else: return contador
  
def hospital(c:Queue[(int,str,str)])->int:
    contador=0
    while not c.empty():
        guardar=c.get()
        if guardar[0]<=3:
            contador+=1
    else:return contador

def atencion_banco(c:Queue[(str,int,bool,bool)])->Queue[(str,int,bool,bool)]:
    prioridad=Queue()
    preferencial=Queue()
    resto=Queue()
    final=Queue()
    while not c.empty():
        guardar=c.get()
        if guardar[3]:
            prioridad.put(guardar)
        elif guardar[2]:
            preferencial.put(guardar)
        else: resto.put(guardar)
    while not prioridad.empty():
        guardar=prioridad.get()
        final.put(guardar)
    while not preferencial.empty():
        guardar=preferencial.get()
        final.put(guardar)
    while not resto.empty:
        guardar=resto.get()
        final.put(guardar)