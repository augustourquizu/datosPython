import math

def imprimir_hola_mundo() -> str:
	return("Hola Mundo")

def raiz_de_2  ()-> float:
	return round(math.sqrt(2), 4)

def factorial_de_2() ->int:
	return math.factorial(2)

def perimetro ()-> float:
	return round(2*math.pi,4)

def imprimir_saludo (nombre:str) -> str:
	return (f"Hola {nombre}")

def raiz_de_un_numero (numero:float) -> float :
	return round(math.sqrt(numero), 4)

def fahrenheit_a_celcius (temp_far:float)-> float:
	return round((temp_far-32) *5 /9, 4)

def imprimir_dos_veces(estribillo:str) -> str:
	print ((estribillo+"\n")*2)

def es_multiplo_de (n:int, m:int) -> bool:
	return n%m==0

def es_par(numero:int) -> bool:
	return es_multiplo_de(numero,2)

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int)->int:
	return math.ceil(comensales*min_cant_de_porciones/8)

def alguno_es_0(numero1:float, numero2:int) -> bool:
	return numero1==0 or numero2==0

def ambos_son_0(numero1:float, numero2:int) -> bool:
	return numero1==0 and numero2==0

def nombre_largo(nombre:str) -> bool:
	return 3<= len(nombre) <= 8

def es_bisiesto(año:int)-> bool:
	return (año%4==0 and año%100!=0) or año%400==0

def peso_pino(altura:float) -> float:
	return min(300, altura*100)*3+ 2*max(altura*100-300, 0)

def es_peso_util(peso:float) -> float:
	return 400<=peso<=1000

def sirve_pino(altura:float) -> bool:
	return es_peso_util(peso_pino(altura))

def devolver_el_doble_si_es_par(numero:int) ->int:
	if numero%2==0:
		return numero*2
	else: return numero

def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
	if numero%2==0:
		return numero
	else: return numero+1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int):
	if numero%3==0:
		if numero%9==0:
			return numero*3
		return numero*2
	else: return numero

def lindo_nombre(nombre:str) -> str:
	if len(nombre)>=5:
		return "Tu nombre tiene muchas letras!"
	else: return "Tu nombre tiene menos de 5 caracteres"
def elRango(numero:int) ->str:
	if numero<5:
		return "Menor a 5"
	elif 10<=numero <=20:
		return  "Entre 10 y 20"
	else: return "Mayor a 20"

def trabajo_o_descanso(genero:str,edad:int):
	if genero =="F" and (edad>=60 or edad <18):
		return "A descansar"
	if genero =="M" and (edad>=65 or edad <18):
		return "A descansar"
	else: return "A trabajar"

def rango_10():
	x=1
	y=""
	while x!=10:
		y=y+ str(x) + ", "
		x=x+1
	else: return y+str(x)

print(imprimir_hola_mundo(),raiz_de_2(), factorial_de_2(), perimetro(), imprimir_saludo("Augusto"), raiz_de_un_numero(3), fahrenheit_a_celcius(212), es_multiplo_de(4,2),
  	es_par(2), cantidad_de_pizzas (3,3), alguno_es_0(0,1), ambos_son_0 (0,0), "\n",nombre_largo ("Augusto"), es_bisiesto(2000), peso_pino(5),es_peso_util(400), sirve_pino(3),
  	devolver_el_doble_si_es_par(3), devolver_valor_si_es_par_sino_el_que_sigue(4), devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(9), lindo_nombre("Augusto"), "\n",
  	trabajo_o_descanso("F",10), rango_10())
#imprimir_dos_veces ("No grites por favor \ny no apagues la luz")
