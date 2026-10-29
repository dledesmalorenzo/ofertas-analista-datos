# Qué buscan las empresas en un analista de datos en España

Un análisis de 25.100 ofertas de trabajo de datos publicadas en España, para quien quiere entrar en el sector y saber qué aprender primero.

## La pregunta

¿Qué herramientas y condiciones piden las empresas en España a los perfiles de datos, y qué cambia cuando el puesto es de marketing?

Le interesa a quien quiere entrar en el sector (estudiantes de bootcamps, gente que cambia de profesión) para decidir qué aprender primero, y a los centros de formación para ajustar su temario a lo que pide el mercado.

## Los datos

- De dónde salen: [data_jobs](https://huggingface.co/datasets/lukebarousse/data_jobs), ofertas de trabajo recogidas de Google por Luke Barousse (licencia Apache 2.0).
- Cuántos son: el conjunto completo tiene 785.741 filas y 17 columnas. Me quedo con las ofertas de España: 25.100 filas y 17 columnas.
- Qué es cada fila: una oferta de trabajo de datos publicada en 2023, con el puesto, la ciudad, la empresa, si es en remoto, el tipo de jornada, el salario (cuando lo indica) y las herramientas que pide.

El archivo original pesa 231 MB y no se sube a GitHub. Para reproducir el análisis, descárgalo desde el enlace y guárdalo en `datos/data_jobs.csv`.

## Qué he limpiado y por qué

- (Pendiente: se completa al terminar el EDA.)

## Lo que he encontrado

1. (Pendiente: se completa al terminar el EDA.)
2.
3.

## La app

![La app](capturas/app.png)

(Pendiente: se completa al terminar la app.)

Enlace: (pendiente de publicar en Streamlit Community Cloud)

## Cómo ejecutarlo

1. Crear un entorno e instalar las librerías: `pip install -r requirements.txt`
2. Descargar los datos originales en `datos/data_jobs.csv` (ver el apartado "Los datos").
3. El EDA está en `eda.ipynb`.
4. La app se abre con `streamlit run app.py`.

## Autor

Daniel · [GitHub](https://github.com/dledesmalorenzo)
