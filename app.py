# La app de mi proyecto
# Para verla, en la terminal: streamlit run app.py
# Son los mismos pasos que en app_pisos.py y app_titanic.py. Si te atascas, busca el mismo paso allí.



# Paso 1. La página
# 1.1 Importa streamlit y pandas.
# 1.2 Pon el nombre de la pestaña del navegador, la página a todo lo ancho y un título que diga de qué va tu proyecto.
# 1.3 Debajo, una o dos frases con st.write: qué pregunta responde la app y de dónde salen los datos.

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analistas de datos en España",
    page_icon= "📊",
    layout="wide"
)

st.title("Analistas de datos en España")

st.write("¿Qué buscan las empresas en un analista de datos en España?")
st.write("¿Qué puestos piden menos habilidades y son más fáciles para empezar?")

# Paso 2. Los datos
# 2.1 La función cargar_datos, con @st.cache_data encima, que lea "datos/datos_limpios.csv" y lo devuelva.
#     La limpieza ya está hecha en el cuaderno, así que la función solo lee y devuelve, como en la carta del bar.
# 2.2 Llama a la función y guarda la tabla en una variable con el nombre de tus datos.

@st.cache_data                                             # lee el CSV una sola vez, no en cada clic
def cargar_datos():
    ofertas = pd.read_csv("datos/datos_limpios.csv")       # los datos ya limpios del EDA
    ofertas["habilidades"] = ofertas["habilidades"].str.split(", ")   # el texto "sql, python" vuelve a ser lista (.str.split me lo dio el profesor, no lo hemos visto en clase)
    return ofertas

ofertas = cargar_datos()                                   # llamamos a la función y guardamos la tabla
st.write("Tenemos", len(ofertas), "ofertas de trabajo de datos en España.")   # para comprobar que se ha cargado


# Paso 3. Los filtros
# 3.1 En la barra de la izquierda (with st.sidebar:), al menos dos filtros:
#     un desplegable o unos botones para una columna de texto, con "Todos" al principio,
#     y una barra para una columna de números.

with st.sidebar:

    st.header("Filtros")
    puestos = sorted(ofertas["puesto"].unique())
    puestos.insert(0, "Todos")
    puesto = st.selectbox("Puestos", puestos)

    modalidad = st.radio("Modalidad", ["Todas", "Remoto", "Presencial"])

    titulo_uni = st.radio("Título universitario", ["Todas", "Menciona título universitario", "No menciona título universitario"])

    habilidades_min, habilidades_max = st.slider("Nº de habilidades requeridas", 1, 34, (1, 34))


# Paso 4. Filtrar
# 4.1 Empieza con filtrados = tu tabla, y después aplica un filtro por cada widget, como en los pisos.

filtrados = ofertas

if puesto != "Todos":
    filtrados = filtrados[filtrados["puesto"] == puesto]
if modalidad == "Remoto":
    filtrados = filtrados[filtrados["remoto"] == True]
if modalidad == "Presencial":
    filtrados = filtrados[filtrados["remoto"] == False]
if titulo_uni == "Menciona título universitario":
    filtrados = filtrados[filtrados["sin_titulo"] == False]
if titulo_uni == "No menciona título universitario":
    filtrados = filtrados[filtrados["sin_titulo"] == True]

if habilidades_min > 1 or habilidades_max < 34:
    filtrados = filtrados[filtrados["num_habilidades"] >= habilidades_min]
    filtrados = filtrados[filtrados["num_habilidades"] <= habilidades_max]

# Paso 5. Si no queda nada
# 5.1 Si filtrados está vacía, saca un aviso con st.warning y para el programa con st.stop().

if len(filtrados) == 0:
    st.warning("No hay ofertas con estos filtros")
    st.stop()

# Paso 6. Las métricas
# 6.1 Tres métricas en columnas, con los números más importantes para tu pregunta.

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Nº de ofertas", len(filtrados))
with col2:
    st.metric("Media de habilidades requeridas", filtrados["num_habilidades"].mean().round(1))
with col3:
    st.metric("Porcentaje sin mención de título", (filtrados["sin_titulo"].mean()*100).round(1))

# Paso 7. Las pestañas
# 7.1 Al menos dos pestañas: una con la tabla filtrada y otra con dos gráficos.
# 7.2 Si tus datos tienen latitud y longitud, otra pestaña con el mapa.



# Paso 8. Una pregunta para el usuario
# 8.1 Una última pestaña con una pregunta, como "¿Cuánto cobrarías por tu piso?" o "¿Te habrías salvado?":
#     el usuario elige algo y la app le contesta con lo que dicen los datos.
