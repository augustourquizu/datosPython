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

print(pertenece([1,2,3], 3), divide_a_todos([2,4,6], 2), suma_a_total([1,2,3,4]), ordenados([1,2,3]), 
      palabra_larga(["holamund"]), palindromo("neuque"), fortaleza("Matribur12"), calcular_saldo([("I",2000),
    ("R", 20),("R", 1000),("I", 300)] ), vocales("holae"), lista_pares([1,2,5,4]), sin_vocales("holamundo"),
      reemplazar_vocales("hola mundo"), dar_vuelta_str("hola mundo"), eliminar_repetidos(["hola", "mundo", "hola", "chau"]))