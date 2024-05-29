from queue import LifoQueue, Queue
def contar_lineas(nombre_archivo:str)->int:
    archivo=open(nombre_archivo,"r")
    contenido=archivo.readlines()
    return len(contenido)

def existe_palabra(palabra:str, nombre_archivo:str)->bool:
    lista=""
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivo.close()
    for element in contenido:
        if element!=" " and element!="."and element!="\n":
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
        if element!=" " and element!="." and element!="\n":
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
    nuevo=open("texto2.txt", "w")
    contador=0
    bandera=True
    for element in contenido:
        if element[0]!="#" and element[0]!=" ":
            texto=texto+element+"\t"
        while element[contador]==" " and element[contador]!="#" and bandera:
            if element[contador+1]==" ":
                contador+=1
            elif element[contador+1]=="#":
                bandera=False
            else: 
                texto=texto+element
                bandera=False
        else: 
            bandera=True
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
        texto=texto+contenido[contador]
        contador-=1
    else: texto=texto+contenido[0]
    nuevo=open("reverso.txt", "w")
    nuevo.writelines(texto)
    nuevo.close()
