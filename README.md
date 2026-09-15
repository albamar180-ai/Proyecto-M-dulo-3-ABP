# Sistema de Gestion de Datos - Proyecto Modulo 3

Proyecto desarrollado como parte del modulo 3 del bootcamp.

## Descripcion
Aplicacion de consola en Python para gestionar productos internos de una empresa de tecnologia. Permite listar, agregar, actualizar, eliminar y resumir datos de inventario, segun lo solicitado en pauta entregada.

## Tecnologias
- Python 3
- CSV como archivo de datos
- Programacion modular con archivos .py separados

## Como ejecutar
1. Abrir terminal en la carpeta sistema_gestion_datos.
2. Ejecutar:

bash
python src/main.py


## Estructura
text
sistema_gestion_datos/
├── src/
│   ├── main.py
│   ├── operations.py
│   ├── validators.py
│   └── data_manager.py
├── data/
│   └── productos.csv
├── tests/
│   └── salida_prueba.txt
└── docs/


## Funcionalidades
- Entrada y salida con input(), print() y f-strings.
- Validacion de datos con manejo de excepciones.
- Uso de condicionales, bucles, break y continue.
- Funciones con parametros y retorno.
- Funcion recursiva para sumar el valor total del inventario.
- Uso de listas, diccionarios, tuplas y conjuntos.
- Separacion del codigo en modulos.

## Desafios y soluciones
El principal desafio fue ordenar el codigo para que no quedara todo en un solo archivo. Para solucionarlo, se separaron las responsabilidades en modulos: validaciones, operaciones y manejo de archivos.
