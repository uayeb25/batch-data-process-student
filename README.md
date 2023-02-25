# Examen OOP I

En este proyectos cargamos mediante un proceso BATCH hecho en python los datos que se encuentran en ``` classes.data.DATA ``` en diferentes collections de una MongoDB

Note que en el archivo ```app.py``` ya se encuentra cargada en una variable ```data``` los datos crudos que se desean procesar. 

la variable DATA que ya se cargo en el ```main``` es una arreglo donde cada objeto tiene la siguiente estructura:

```python

{
    'numero_cuenta': 4069666
    , 'nombre_completo': 'Lucía 1390 Sánchez 1390'
    , 'cursos_aprobados': ['Ciencias políticas', 'Derecho', 'Geografía', 'Cine']
    , 'cursos_reprobados': ['Veterinaria', 'Ciencias políticas', 'Biología']
    , 'edad': 24
    , 'carrera': 'Psicología'
}

```