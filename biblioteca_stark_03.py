import os
from datos_stark_03 import lista_personajes
#from functools import reduce

evaluar_lista = lambda lista_heroes : True if not lista_heroes else False
lista_vacia =[]

def limpiar_consola() -> None:
    _ = input("\n Presione una tecla para continuar")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

def stark_normalizar_datos(lista_heroes: list[dict]):
    #La función recibe una lista de diccionarios, si los valores de las keys peso, altura, edad o fuerza no estan en el tipo de dato adecuado los convierte. Imprime un mensaje si la lista que recibe está vacia y otro si normalizó al menos un dato.
    flag = False
    mensaje = "Datos normalizados"
    if not evaluar_lista:
        print("Error lista de héroes vacía")
    else:
        for heroe in lista_heroes:
            for key, value in heroe.items():
                if key == "edad" or key == "fuerza" and type(value) != int:
                    value = int(value)  
                    heroe.update({key: value})
                    flag = True
                elif key == "peso" or key == "altura" and type(value) != float:
                    value = float(value)
                    heroe.update({key: value})
                    flag = True
    
    if flag:
        print(mensaje)

def obtener_nombre(heroe: dict) -> str:
    # Recibe:  un heroe de tipo dict, 
    # retorna: un string con el nombre del heroe
    nombre = heroe.get("nombre")
    return f"Nombre: {nombre}"

def imprimir_dato(dato:str):
    #recibe: un string
    #Imprime el dato recibido
    #Retorno: no tiene
    print(dato)

def stark_imprimir_nombres_heroes(lista_heroes:list[dict]):
    #Recibe: lista de diccionarios (heroes)
    #Retorna: -1 si la lista esta vacia
    #Llama a las funciones imprimir dato y obtener nombre para poder listar los nombres de los héroes
    if len(lista_heroes) == 0:
        return -1
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))

def obtener_nombre_y_dato(heroe:dict, key:str):
    #Recibe: un dict(heroe) y un string
    #Llama a la funcion obtener nombre
    #Retorna: nombre del heroe junto con la key seleccionada con su valor
    return f"{obtener_nombre(heroe)} | {key}: {heroe.get(key)}"

def stark_imprimir_nombres_alturas(lista_heroes:list[dict]):
    #Recibe una list de dict
    #Si la list esta vacia retorna -1. Sino recorre la lista y llama a la funcion obtener_nombre_y_dato para imprimir nombre, y el dato de caa heroe 
    if len(lista_heroes) == 0:
        return -1
    else: 
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe,"altura"))

def calcular_max(lista_heroes:list[dict], key:str)->dict:
    #Recibe: list de dict y un string que representa el dato a calcular
    #calcula el maximo valor del string ingresado
    #Retorna: nombre del heroe con el maximo valor del dato ingresado como parametro
    heroe_max = None
    valor_max = 0
    for heroe in lista_heroes:
        parametro = heroe.get(key)
        if parametro > valor_max:
            valor_max = parametro
            heroe_max = heroe

    return heroe_max
 
def calcular_min(lista_heroes: list[dict], key:str)->dict:
    #Recibe: list de dict y un string que representa el dato a calcular
    #calcula el minimo valor del string ingresado
    #Retorna: nombre del heroe con el minimo valor del dato ingresado como parametro
    heroe_min = None
    valor_min = 0
    for heroe in lista_heroes:
        parametro = heroe.get(key)
        if valor_min == 0 or parametro < valor_min:
            valor_min = parametro
            heroe_min = heroe
    
    return heroe_min

def calcular_max_min_dato(lista_heroes:list[dict],calculo:str,key:str)->dict:
    #Recibe: list de dict, string calculo que debe ser minimo o maximo, y una key que es el dato a calcular
    #Calcula lo indicado por los parametros calculo y key
    #Retorna el nombre del heroe 
    if calculo == "maximo":
        return calcular_max(lista_heroes,key)
    elif calculo == "minimo":
        return calcular_min(lista_heroes, key)

def stark_calcular_imprimir_heroe(lista_heroes:list[dict],max_o_min:str,key:str):
    #Recibe: lista tipo dict de heroes, un string:debe ser maximo o minimo, y una key que es el parametro a evaluar(ej:peso)
    #Llama a la funcion calcular_max_min_dato para que calcule lo solicitado
    #Hace un print del dato obtenido

    calcular_max_min_dato(lista_heroes,max_o_min,key)
    match max_o_min:
        case "maximo":
            valor = "Mayor"
        case "minimo": 
           valor = "Menor"
        
    print(f"{valor} {key}: {obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,max_o_min,key), key)}")

def sumar_dato_heroe(lista_heroes:list[dict], key:str):
    acumulador = 0
    for heroe in lista_heroes:
        if type(heroe) == dict and len(heroe) > 0 and (type(heroe.get(key)) == float or type(heroe.get(key)) == int):
            acumulador += heroe.get(key)
    
    
    return acumulador

def dividir(dividendo,divisor):
    resultado =  dividendo/divisor if divisor != 0 else 0
    return resultado

def calcular_promedio(lista_heroes:list[dict], key:str):
    promedio = dividir(sumar_dato_heroe(lista_heroes,key), len(lista_heroes)) 
    return promedio

def stark_calcular_imprimir_promedio_altura(lista_heroes:list[dict]):
    promedio_altura = dividir(sumar_dato_heroe(lista_heroes,"altura"),len(lista_heroes)) if lista_heroes else -1
    imprimir_dato(f"El promedio de altura es: {promedio_altura}")

def stark_imprimir_identidades_bajo_alto(lista_heroes:list[dict]):
    alto = obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,"maximo","altura"),"identidad")
    bajo = obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,"minimo","altura"),"identidad")
    print(f"El héroe más alto es: {alto} \nEl héroe mas bajo es: {bajo}")
    
def imprimir_menu_2():
    #No recibe parámetros
    #No retorna nada
    #Tiene una variable con el menu, el cual es mostrado al llamar a la funcion imprimir_dato
    menu_2 = """
    1  - Imprimir el nombre de cada superhéroe de género M
    2  - Imprimir el nombre de cada superhéroe de género F
    3  - Mostrar cuál es el superhéroe más alto de género M 
    4  - Mostrar cuál es el superhéroe más alto de género F 
    5  - Determinar cuál es el superhéroe más bajo  de género M 
    6  - Determinar cuál es el superhéroe más bajo  de género F 
    7  - Determinar la altura promedio de los  superhéroes de género M
    8  - Determinar la altura promedio de los  superhéroes de género F
    9  - Informar el nombre de los superhéroes mas alto y bajo de género F y M 
    10 - Informar cuántos superhéroes tienen cada tipo de color de ojos.
    11 - Informar cuántos superhéroes tienen cada tipo de color de pelo.
    12 - Informar cuántos superhéroes tienen cada tipo de inteligencia. 
    13 - Mostrar superhéroes agrupados por color de ojos.
    14 - Mostrar superhéroes agrupados por color de pelo.
    15 - Mostrar superhéroes agrupados por tipo de inteligencia
    """
    imprimir_dato(menu_2)

def validar_entero(numero:str):
    return numero.isdigit()

def pedir_opcion():
    opcion = input("Por favor elija una opción: ")
    if validar_entero(opcion):
        opcion = int(opcion)
    else:
        opcion = -1
    #opcion = int(opcion) if validar_entero(opcion) else -1
    return opcion

def stark_menu_principal_2():
    imprimir_menu_2()
    return pedir_opcion()
     
def es_genero(heroe:dict, string:str):
    return True if (string.upper()== heroe["genero"].upper()) else False
    
def stark_imprimir_heroe_genero(lista_heroes:list[dict], genero:str):
    #recibe como parámetros una list de dict(heroes) y un string para el género a filtrar
    #Llama a las funciones es_esgenero, imprimir_dato y obtener_nombre para mostrar los nombres según genero deseado
    genero = genero.upper()
    for heroe in lista_heroes:
        if es_genero(heroe,genero) and genero == heroe["genero"]:
            imprimir_dato(obtener_nombre(heroe))

def calcular_min_genero(lista_heroes:list[dict], genero:str, variable:str)->dict:
    #La funcion recibe una lista de dict, un genero(string) y una variable(string)
    #filtra la lista segun genero
    #ordena la lista de mayor a menor segun la variable
    #retorna el heroe
    lista_filtrada_por_genero = list(filter(lambda x : x["genero"] == genero.upper(),lista_heroes))
    lista_filtrada_por_genero.sort(key= lambda x : x[variable.lower()])
    return lista_filtrada_por_genero[0]
    #codigo entre lineas 210 y 219 son la primera solucion al problema
    # genero = genero.upper()
    # variable = variable.lower()
    # minimo = 0
    # min_heroe = None
    # for heroe in lista_heroes:
    #     if es_genero(heroe,genero) and heroe["genero"] == genero:
    #         if min_heroe == None or heroe[variable] < minimo:
    #             minimo = heroe[variable]
    #             min_heroe = heroe
    # return min_heroe
            
def calcular_max_genero(lista_heroes:list[dict], genero:str, variable:str)-> dict:
    #La funcion recibe una lista de dict, un genero(string) y una variable(string)
    #filtra la lista segun genero
    #ordena la lista de mayor a menor segun la variable
    #retorna el heroe
    lista_filtrada_por_genero = list(filter(lambda x : x["genero"] == genero.upper(),lista_heroes))
    lista_filtrada_por_genero.sort(key= lambda x : x[variable.lower()],reverse= True)
    return lista_filtrada_por_genero[0]
    #codigo entre lineas 226 y 236 son la primera solucion al problema
    # genero = genero.upper()
    # variable = variable.lower()
    # maximo = 0
    # max_heroe = None
    # for heroe in lista_heroes:
    #     if es_genero(heroe,genero) and heroe["genero"] == genero:
    #         if heroe[variable] > maximo:
    #             maximo = heroe[variable]
    #             max_heroe = heroe
    # return max_heroe

def calcular_max_min_dato_genero(lista_heroes:list[dict],maximo_o_minimo:str, variable:str,genero:str)->dict:
    #Recibe como parametros una lista de heroes(dict), string maximo o minimo, string variable(a evaluar) y string para genero
    #Evalua si es minimo o maximo y llama a la funcion correspondiente para retornar el hereo deseado
    if maximo_o_minimo.lower() == "minimo":
        return calcular_min_genero(lista_heroes,genero,variable)
    elif maximo_o_minimo.lower() == "maximo":
        return calcular_max_genero(lista_heroes,genero,variable)
    
def stark_calcular_imprimir_heroe_genero(lista_heroes:list[dict],maximo_o_minimo:str, variable:str,genero:str):
    #Recibe como parámetros una list de dict(heroe), string maximo o minimo, string variable y string m, f o nb para genero
    #Evalua si la lista no está vacia, si esto es true imprime el dato deseado, de lo contrario no hace nada y retorna -1
    if not lista_heroes:
        return -1
    else:
        heroe = calcular_max_min_dato_genero(lista_heroes,maximo_o_minimo,variable,genero)
        imprimir_dato(obtener_nombre_y_dato(heroe,variable))

def sumar_dato_heroe_genero(lista_heroes:list[dict], variable:str,genero:str):
    #Recibe como parametros una list de dict(heroe), string variable y string genero (M,F o NB)
    #Evalua que cada heroe no esté vacío, que la variable sea una key del dict y el valor de la key genero del dict sea igual al del parámetro género. Si todo se cumple acumula los valores
    #Retorna el acumulador
    acumulador = 0
    variable = variable.lower()
    for heroe in lista_heroes:
        if variable in heroe and heroe and heroe["genero"] == genero.upper():
            acumulador += heroe.get(variable)
    return acumulador

def cantidad_heroes_genero(lista_heroes:list[dict], genero:str):
    #Recibe una lista de heroe y un string para el género. Filtra la lista según genero y retorna la cantidad de heroes de ese género
    acumulador_heroes = len(list(filter(lambda heroe : heroe["genero"] == genero.upper(),lista_heroes)))
    return acumulador_heroes

def calcular_promedio_genero(lista_heroes:list[dict],variable:str, genero:str):
    #Recibe una lista de dict(heroes), un string variable y un string genero (M, F o NB)
    #Calcula el promedio llamando a las funciones sumar_dato_heroe_genero y cantidad_heroes_genero y lo retorna
    promedio = round(sumar_dato_heroe_genero(lista_heroes,variable,genero) / 
                     cantidad_heroes_genero(lista_heroes,genero),2)
    return promedio

def stark_calcular_imprimir_promedio_altura_genero(lista_heroes:list[dict],variable:str, genero:str):
    #Recibe una list de dict(heroes), un string variable(altura, peso, etc) y un string genero (M, F, NB)
    #Evalua que la lista no esté vacia, de ser así imprime un mensaje indicandolo
    #Si no esta vacia invoca a la funcion calcular promedio e imprimir dato para mostrar el dato deseado
    variable = variable.lower()
    if not evaluar_lista:
        print("Error: Lista de héroes vacía")
    else:
        imprimir_dato(f"{variable.capitalize()} promedio genero {genero.upper()}: {calcular_promedio_genero(lista_heroes,variable,genero)}") 

def calcular_cantidad_tipo(lista_heroes:list[dict],variable:str):
    #Recibe una list de dict(heroes) y un string variable (color_ojos, color_pelo, etc)
    #Crea un dict donde guarda como key value el tipo y cantidad del dato ingresado como parametro
    diccionario = {}
    if not evaluar_lista:
        print("Error: Lista de héroes vacía")
    else:
        for heroe in lista_heroes:
            dato = heroe.get(variable,"No tiene").capitalize()
            if dato == "":
                dato = "No tiene"
            elif dato in diccionario:
                diccionario[dato] += 1
            else:
                diccionario[dato] = 1
    return diccionario

def imprimir_cantidad_heroes_tipo(diccionario:dict, variable:str):
    #Recibe una diccionario con key y value que representan valores de los heroes, y un string que representa el dato a mostrar.
    #Llamando a la funcion imprimir dato, imprime cada key(caracteristica) con su valor(cantidad)
    variable = variable.replace("_", " de ").capitalize()
    print(f"Característica: {variable}")
    for key, value in diccionario.items():
        imprimir_dato(f"Color: {key} - Cantidad de héroes: {value}")

def stark_calcular_cantidad_por_tipo(lista_heroes:list[dict], variable:str):
    #Recibe como parámetros una list de dict(heroes) y un string variable (color_pelo, color_ojos, etc)
    #Invoca a las funciones imprimir_cantidad_heroes_tipo y calcular_cantidad_tipo para mostrar por pantalla los datos
    imprimir_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes,variable),variable) 

def obtener_lista_de_tipos(lista_heroes:list[dict], variable:str)->list:
    #Recibe una list[dict] de heroes, un string variable a buscar
    #Crea una lista de dict, itera la lista recibida y guarda en la nueva lista como key el valor obtenido de la variable pasada por paámetro, si la key ya se encontraba no la agrega 2 veces
    #Retorna la lista con las key
    lista = []
    for heroe in lista_heroes:
        if not heroe[variable].capitalize() in lista:
            if heroe[variable] == "" or not heroe[variable]:
                lista.append("N/A")
            else:
                lista.append(heroe[variable].capitalize())
    return lista

def normalizar_dato(valor:str,valor_por_defecto:str)-> str:
    #Recibe un valor y valor por defecto ambos de tipo string.
    #Si el valor que llega no está vacio lo retorna, si l está lo reemplaza por el valor por defecto y lo retorna
    if valor != "":
        return valor
    else:
        return valor_por_defecto

def obtener_heroes_por_tipo(lista_heroes:list[dict],lista_variedades:list[dict],variable:str)->dict[list]:
    #Recibe list[dict] de heroes, list[dict] y un string variable. 
    #Crea un diccionario que tendrá como keys, los value de una key del heroe, mientras que los value del nuevo dict serán listas con los nombres de los heroes.
    #Retorna un dict[list]
    diccionario = {}
    for item in lista_variedades:
        if not item in diccionario.keys():
            diccionario[item] = []
        for heroe in lista_heroes:
            valor = normalizar_dato(heroe[variable],"N/A").capitalize()
            if valor == "N/a":
                valor = valor.upper()
            if valor in diccionario and not heroe["nombre"] in diccionario[valor]:
                diccionario[valor].append(heroe["nombre"])
    return diccionario

def imprimir_heroes_por_tipo(diccionario_tipo:dict, variable:str):
    #Recibe un dict que representa los ditintos tipos como clave y una lista de nombres como su valor, y una variable que representa el tipo a evaluar
    #recorre el diccionario e imprime por cada tipo los nombres de heroes asociados
    for key, value in diccionario_tipo.items():
        lista_ordenada =" | " 
        lista_ordenada = lista_ordenada.join(value)
        dato = f"{variable.capitalize().replace('_',' de ')} {key.capitalize()}: {lista_ordenada}"
        imprimir_dato(dato)
        
def stark_listar_heroes_por_dato(lista_heroes:list[dict], variable:str):
    #Recibe una list[dict] de heroes, y una variable
    #Llama a las funciones para imprimir los héroes segun el parámetro valiable pasado
    imprimir_heroes_por_tipo(obtener_heroes_por_tipo(lista_heroes,obtener_lista_de_tipos(lista_heroes,variable),variable),variable)


