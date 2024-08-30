import datetime
from dateutil.relativedelta import relativedelta

def calcular_edad(ci):
    if not ci.isdigit():
        print("El número de cédula debe contener solo dígitos.")
        return
    
    if len(ci) != 11:
        print("El número de cédula debe tener 11 dígitos.")
        return
    
    try:
        fecha_nac = ci[:6]
        ordenar_fecha = datetime.datetime.strptime(fecha_nac, '%y%m%d')
        
        fecha_actual = datetime.datetime.now().date()
        if ordenar_fecha.year > fecha_actual.year:
            ordenar_fecha = ordenar_fecha.replace(year=ordenar_fecha.year - 100)
        
        edad = relativedelta(datetime.datetime.now(), ordenar_fecha)
        print(f"Tienes {edad.years} años.")
    
    except ValueError:
        print("Error en la conversión de la fecha. Verifique la cédula.")

# Ejecución de la función
calcular_edad(input("Introduce Número de Identidad: "))
