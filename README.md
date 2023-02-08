
#  Calcular edad utilizando una cédula cubana

Este código es una función que calcula la edad de una persona cubana a partir de un número de cedula. Primero, comprueba si el número de cedula es un número válido de 11 dígitos. Luego, extrae la fecha de nacimiento del número de cedula y la almacena en una variable. Después, convierte la fecha de nacimiento en un objeto de datetime. Finalmente, calcula la edad de la persona utilizando la función relativedelta y la muestra en pantalla.

## Configurar y ejecutar



1. Clonamos el repo
```bash
  git clone https://github.com/brianmrdev/calcula-edad-utilizando-cedula-cubana.git
  cd calcula-edad-utilizando-cedula-cubana
```
2. Creamos el entorno virtual y lo activamos
```bash
  python3 -m venv env
  source env/bin/activate
```
3. Instalamos las dependencias
```bash
  pip install -r equirements.txt
```
4. Ejecutamos el proyecto
```bash
  python main.py
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)


