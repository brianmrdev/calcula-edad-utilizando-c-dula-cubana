import datetime
from dateutil.relativedelta import relativedelta

def calcular_edad(ci):
    
    fecha_nac = ci[:6]
    fecha = fecha_nac[:2] + fecha_nac[2:4] + fecha_nac[-2:]
    ordenar_fecha= datetime.datetime.strptime(fecha, '%y%m%d')
    
    fecha_actual = datetime.datetime.now().date()
    
    if ordenar_fecha.year > fecha_actual.year:
        ordenar_fecha = ordenar_fecha.replace(year=ordenar_fecha.year-100)
    
    edad = relativedelta(datetime.datetime.now(), ordenar_fecha.date())
    
    print(f"{edad.years} años")
    

calcular_edad(ci = "88081128104")
