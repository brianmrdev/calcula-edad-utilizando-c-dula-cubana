
#  Calcular edad utilizando una cédula cubana

Este código calcula la edad de una persona cubana utilizando su cédula de identidad. La función strptime() se usa para convertir la cadena de caracteres de la cédula de identidad en un objeto datetime. La función datetime.now() obtiene la fecha actual y se usa con la función relativedelta() para calcular la edad de la persona. Luego la edad se imprime en un mensaje. El código también tiene una línea adicional para ajustar la edad si la persona tiene más de 100 años.
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


