# La app de mi proyecto
# Para verla, en la terminal: streamlit run app.py
# Son los mismos pasos que en app_pisos.py y app_titanic.py. Si te atascas, busca el mismo paso allí.



# Paso 1. La página
# 1.1 Importa streamlit y pandas.
# 1.2 Pon el nombre de la pestaña del navegador, la página a todo lo ancho y un título que diga de qué va tu proyecto.
# 1.3 Debajo, una o dos frases con st.write: qué pregunta responde la app y de dónde salen los datos.

import streamlit as st                                                                    # para hacer la app
import pandas as pd                                                                       # para trabajar con las tablas

st.set_page_config(                                                                       # configuración de la página: nombre e icono de la pestaña y página a todo lo ancho
    page_title="Analistas de datos en España",
    page_icon= "📊",
    layout="wide"
)

st.title("Analistas de datos en España")                                                  # el título grande de la app

st.write("¿Qué buscan las empresas en un analista de datos en España?")                   # la pregunta principal que responde la app
st.write("¿Qué puestos piden menos habilidades y son más fáciles para empezar?")          # otra pregunta que responde la app

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

with st.sidebar:                                                                          # todo lo que va aquí sale en la barra de la izquierda

    st.header("Filtros")                                                                  # título de la barra
    puestos = sorted(ofertas["puesto"].unique())                                          # la lista de puestos, sin repetir y ordenada
    puestos.insert(0, "Todos")                                                            # añadimos "Todos" al principio de la lista
    puesto = st.selectbox("Puestos", puestos)                                             # el desplegable de puestos; guarda el que elige el usuario

    modalidad = st.radio("Modalidad", ["Todas", "Remoto", "Presencial"])                  # botones para elegir remoto o presencial

    titulo_uni = st.radio("Título universitario", ["Todas", "Menciona título universitario", "No menciona título universitario"])  # botones para elegir si la oferta menciona título universitario

    habilidades_min, habilidades_max = st.slider("Nº de habilidades requeridas", 1, 34, (1, 34))  # barra de dos puntas: mínimo y máximo de habilidades


# Paso 4. Filtrar
# 4.1 Empieza con filtrados = tu tabla, y después aplica un filtro por cada widget, como en los pisos.

filtrados = ofertas                                                                       # empezamos con todas las ofertas y vamos filtrando

if puesto != "Todos":                                                                     # si se ha elegido un puesto concreto
    filtrados = filtrados[filtrados["puesto"] == puesto]                                  # nos quedamos con las ofertas de ese puesto
if modalidad == "Remoto":                                                                 # si se ha elegido remoto
    filtrados = filtrados[filtrados["remoto"] == True]                                    # nos quedamos con las ofertas en remoto
if modalidad == "Presencial":                                                             # si se ha elegido presencial
    filtrados = filtrados[filtrados["remoto"] == False]                                   # nos quedamos con las ofertas que no son en remoto
if titulo_uni == "Menciona título universitario":                                         # si se ha elegido que mencione título
    filtrados = filtrados[filtrados["sin_titulo"] == False]                               # sin_titulo es False cuando la oferta sí menciona título
if titulo_uni == "No menciona título universitario":                                      # si se ha elegido que no mencione título
    filtrados = filtrados[filtrados["sin_titulo"] == True]                                # sin_titulo es True cuando la oferta no menciona título

if habilidades_min > 1 or habilidades_max < 34:                                           # solo si se ha movido la barra (si no, se perderían las ofertas sin habilidades)
    filtrados = filtrados[filtrados["num_habilidades"] >= habilidades_min]                # nos quedamos con las que piden al menos el mínimo
    filtrados = filtrados[filtrados["num_habilidades"] <= habilidades_max]                # y como mucho el máximo

# Paso 5. Si no queda nada
# 5.1 Si filtrados está vacía, saca un aviso con st.warning y para el programa con st.stop().

if len(filtrados) == 0:                                                                   # si no queda ninguna oferta
    st.warning("No hay ofertas con estos filtros")                                        # aviso
    st.stop()                                                                             # paramos la app para que no dé error al calcular las métricas

# Paso 6. Las métricas
# 6.1 Tres métricas en columnas, con los números más importantes para tu pregunta.

col1, col2, col3 = st.columns(3)                                                          # tres columnas para las métricas

with col1:
    st.metric("Nº de ofertas", len(filtrados))                                            # cuántas ofertas cumplen los filtros
with col2:
    st.metric("Media de habilidades requeridas", filtrados["num_habilidades"].mean().round(1))  # cuántas habilidades piden de media, con un decimal
with col3:
    st.metric("Porcentaje sin mención de título", (filtrados["sin_titulo"].mean()*100).round(1))  # porcentaje de ofertas que no mencionan título universitario

# Paso 7. Las pestañas
# 7.1 Al menos dos pestañas: una con la tabla filtrada y otra con dos gráficos.
# 7.2 Si tus datos tienen latitud y longitud, otra pestaña con el mapa.

tab1, tab2, tab3 = st.tabs(["Ofertas", "¿Qué se pide?", "¿Qué te falta?"])                # tres pestañas

with tab1:                                                                                # primera pestaña
    st.header("Las ofertas filtradas")                                                    # título de la pestaña
    st.dataframe(filtrados)                                                               # la tabla de las ofertas filtradas

with tab2:                                                                                # segunda pestaña
    col_a, col_b = st.columns(2)                                                          # dos columnas, una para cada gráfico

    with col_a:
        st.subheader("Las 15 habilidades más pedidas")                                    # título del primer gráfico
        por_habilidad = filtrados.explode("habilidades")                                  # una fila por cada habilidad de cada oferta (explode, recomendado por el profesor)
        por_habilidad = por_habilidad.drop_duplicates()                                   # quitamos las habilidades repetidas dentro de una misma oferta
        st.bar_chart(por_habilidad["habilidades"].value_counts().head(15), horizontal=True)  # las 15 habilidades más pedidas, en barras horizontales

    with col_b:
        st.subheader("Media de habilidades por puesto")                                   # título del segundo gráfico
        habilidades_puesto = filtrados.groupby("puesto")["num_habilidades"].mean().sort_values(ascending=False)  # media de habilidades de cada puesto, de más a menos
        st.bar_chart(habilidades_puesto, horizontal=True)                                 # en barras horizontales

# Paso 8. Una pregunta para el usuario
# 8.1 Una última pestaña con una pregunta, como "¿Cuánto cobrarías por tu piso?" o "¿Te habrías salvado?":
#     el usuario elige algo y la app le contesta con lo que dicen los datos.

with tab3:                                                                                # tercera pestaña: la pregunta para el usuario
    st.subheader("¿Qué te falta para el puesto que quieres?")                             # título de la pestaña
    mi_puesto = st.selectbox("¿Qué puesto quieres?", sorted(ofertas["puesto"].unique()))  # el usuario elige el puesto que quiere
    todas = ofertas.explode("habilidades")                                                # una fila por habilidad, para sacar la lista de todas las habilidades
    lista_habilidades = sorted(todas["habilidades"].dropna().unique())                    # la lista de habilidades, sin huecos, sin repetir y ordenada
    mi_habilidad = st.selectbox("¿Qué habilidad dominas mejor?", lista_habilidades)       # el usuario elige la habilidad que domina mejor
    del_puesto = ofertas[ofertas["puesto"] == mi_puesto]                                  # las ofertas del puesto elegido
    del_puesto = del_puesto[del_puesto["num_habilidades"] > 0]                            # solo las que dicen qué habilidades piden
    separadas = del_puesto.explode("habilidades").drop_duplicates()                       # una fila por habilidad, sin repetidas
    piden_la_mia = separadas[separadas["habilidades"] == mi_habilidad]                    # las ofertas que piden la habilidad del usuario
    porcentaje = round(len(piden_la_mia) / len(del_puesto) * 100, 1)                      # qué porcentaje de las ofertas del puesto piden su habilidad (round() redondea números normales)
    st.metric("Ofertas de este puesto", len(del_puesto))                                  # cuántas ofertas hay de ese puesto
    st.metric("Ofertas que piden tu habilidad", len(piden_la_mia))                        # cuántas piden su habilidad
    st.metric("Porcentaje que piden tu habilidad", porcentaje)                            # el porcentaje

if porcentaje >= 50:                                                                      # si la pide la mitad o más de las ofertas
    st.success("¡Tu habilidad es clave para este puesto!")                                # mensaje positivo, en verde
else:                                                                                     # si no
    st.error("Tu habilidad se pide poco para este puesto. Mira abajo cuáles se piden más")  # mensaje negativo, en rojo
