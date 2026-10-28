# Propuesta del proyecto

Rellenadla y enseñádmela antes de empezar el EDA. Son diez minutos que os pueden ahorrar días.

Nombre: 

## 1. La idea

Título del proyecto: ¿Qué buscan las empresas en un analista de datos en España?

¿Qué preguntas responde y a quién le interesa?
¿Qué herramientas y condiciones piden las empresas en España a los perfiles de datos, y qué cambia cuando el puesto es de marketing? Le interesa a quien quiere entrar en el sector (estudiantes de bootcamps, gente que cambia de profesión...) para saber qué aprender primero, y a los centros de formación para ajustar su temario a lo que pide el mercado.

## 2. Los datos

De dónde salen:
- [ ] Kaggle
- [x] Hugging Face (está en la lista de 03_DATOS.md: "Ofertas de trabajo de datos")
- [ ] Datos míos (dónde los he encontrado):

Enlace a los datos: https://huggingface.co/datasets/lukebarousse/data_jobs

Cuántas filas y columnas tienen:
785.741 filas y 17 columnas en total. Me quedo con las ofertas de España: 25.100 filas y 17 columnas.

Qué es cada fila (un vino, un partido, una venta...):
Una oferta de trabajo de datos publicada en 2023 (analista, científico, ingeniero de datos...), con el puesto, la ciudad, la empresa, si es en remoto, el tipo de jornada, el salario (cuando lo indica) y las herramientas que pide.

Comprobado (los requisitos están en 03_DATOS.md):
- [x] Son tabulares, en una sola tabla
- [x] No los hemos usado en clase
- [x] Tienen más de 1.000 filas
- [x] Tienen al menos 6 columnas, con números y con texto
- [x] Entiendo qué es cada columna
- [x] Hay algo que limpiar: al 12 % de las ofertas de España le faltan las herramientas, el 99 % no indica salario, las ciudades vienen con formatos distintos ("Madrid, Spain", "Spain", "Anywhere") y las herramientas vienen como una lista dentro de una celda
- [x] Sé de dónde salen y se pueden usar: ofertas recogidas de Google por Luke Barousse, con licencia Apache 2.0
- [x] El CSV limpio pesará menos de 100 MB (el original pesa 231 MB, pero solo con España se quedará muy por debajo)

## 3. Tres preguntas que quiero responder

1. ¿Qué herramientas piden más las ofertas de Data Analyst en España?
2. ¿Qué cambia entre una oferta de analista de marketing y una de analista general (herramientas, remoto, tipo de jornada)?
3. ¿Dónde están las ofertas (Madrid, Barcelona, otras ciudades, remoto) y cambia lo que piden según la ciudad?

## 4. La app

¿Qué filtros pondrías en la barra de la izquierda?
Tipo de puesto (Data Analyst, Data Scientist, Data Engineer...), ciudad, si es en remoto o no, y tipo de jornada (completa, media, prácticas, autónomo...).

¿Qué pregunta le harías al usuario al final? (como "¿Cuánto cobrarías por tu piso?")
"¿Qué te falta para ser analista de datos?": el usuario marca las herramientas que ya sabe usar y la app le dice a cuántas ofertas podría optar y cuál es la herramienta que más le conviene aprender a continuación.

¿Tienen coordenadas para hacer un mapa?
- [ ] Sí
- [x] No (hay ciudad, pero no latitud y longitud)

## 5. Plan B

Por si los datos principales no sirven, otros distintos:
Clientes de una telefónica (por qué se van los clientes y si influye el tipo de contrato), de la lista de 03_DATOS.md.

Enlace: https://huggingface.co/datasets/scikit-learn/churn-prediction (Me llamó la atención porque se analizaría la retención de clientes)
