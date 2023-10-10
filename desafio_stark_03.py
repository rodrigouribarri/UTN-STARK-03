from biblioteca_stark_03 import(stark_normalizar_datos, stark_menu_principal_2, stark_imprimir_heroe_genero, stark_calcular_imprimir_heroe_genero, stark_calcular_imprimir_promedio_altura_genero, stark_calcular_cantidad_por_tipo, stark_listar_heroes_por_dato, limpiar_consola)

def stark_marvel_app_2(lista_heroes:list[dict]):
    stark_normalizar_datos(lista_heroes)
    while True:
        opcion_elegida = stark_menu_principal_2()
        match opcion_elegida:
            case 0:
                break
            case 1:
                stark_imprimir_heroe_genero(lista_heroes,"m")
            case 2:
                stark_imprimir_heroe_genero(lista_heroes,"f")
            case 3:
                stark_calcular_imprimir_heroe_genero(lista_heroes,"maximo","altura","m")
            case 4:
               stark_calcular_imprimir_heroe_genero(lista_heroes,"maximo","altura","f")
            case 5:
                stark_calcular_imprimir_heroe_genero(lista_heroes,"minimo","altura","m")
            case 6:
                stark_calcular_imprimir_heroe_genero(lista_heroes,"minimo","altura","f")
            case 7:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes,"altura","m")
            case 8:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes,"altura","f")
            case 9:
                stark_calcular_cantidad_por_tipo(lista_heroes,"color_ojos")
            case 10:
                stark_calcular_cantidad_por_tipo(lista_heroes,"color_pelo")
            case 11:
                stark_calcular_cantidad_por_tipo(lista_heroes,"inteligencia")
            case 12:
                stark_listar_heroes_por_dato(lista_heroes,"color_ojos")
            case 13:
                stark_listar_heroes_por_dato(lista_heroes,"color_pelo")
            case 14:
                stark_listar_heroes_por_dato(lista_heroes,"inteligencia")
            case _: 
                print("Opción incorrecta.\nElija otra por favor")
        limpiar_consola()
                

