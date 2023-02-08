import datetime
from dateutil.relativedelta import relativedelta

def calcular_edad(ci):
    if ci.isdigit():
        if len(ci) == 11:
            fecha_nac = ci[:6]
            fecha = fecha_nac[:2] + fecha_nac[2:4] + fecha_nac[-2:]
            ordenar_fecha= datetime.datetime.strptime(fecha, '%y%m%d')
            
            fecha_actual = datetime.datetime.now().date()
            
            if ordenar_fecha.year > fecha_actual.year:
                ordenar_fecha = ordenar_fecha.replace(year=ordenar_fecha.year-100)
            
            edad = relativedelta(datetime.datetime.now(), ordenar_fecha.date())
            
            print(f"{edad.years} años")
        
        else:
            print("El número de cedula debe tener 11 dígitos")
    else:
        print("El número de cedula debe contener solo dígitos")
    

calcular_edad(ci = input("Introduce Numero de Identidad: "))
