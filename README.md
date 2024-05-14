# Calculadora de Subredes

## Descripción

Estos scripts de Python permiten calcular la cantidad de subredes y hosts con el
rango de la IP, broadcast y la máscara de subred, todo eso en base a la
dirección IP y la máscara de red que se le proporcione.

## Archivos

### Jupyter Notebook

Puedes usar la calculadora a través de un cuaderno Jupyter, la ventaja de usar
este método es que la salida será renderizada a Markdown, lo que permitirá la
mejor apreciación de los resultados. Este archivo lo puedes encontrar
[aquí](calculadora.ipynb), también puedes usar un cuaderno Jupyter en la web con
Google Colab
[aquí](https://colab.research.google.com/drive/1yQ11I-7GkI7zvz2QGcDnzY4rTOrFQ0Ln#scrollTo=aBuh9ZEsYgip).

### Script de Python

Si tienes algún interprete de Python instalado puedes usar el
[script de Python](calculadora.py) para obtener los resultados. Ten en cuenta
que tendrás que instalar las dependencias necesarias con el siguiente comando:

Si estás en Windows:

```bash
pip install numpy tabulate -q
```

Si estás en un sistema basado en Unix:

```bash
pip3 install numpy tabulate -q
```
