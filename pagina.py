# Empezaremos bajando las librerías necesarias
# Libreria para usar los componentes de Streamlit
import streamlit as st
import pandas as pd
import numpy as np
from funciones import *

# Libreria para poder desempaquetar nuestro modelo
import pickle
from pickle import dump

st.title("Calcula cuánto durará tu matrimonio")

col1, col2, col3 = st.columns(3)

with col1:
    edadH = st.number_input("Edad hombre", step=1, min_value=0)

with col2:
    edadM = st.number_input("Edad mujer", step=1, min_value=0)

with col3:
    numHijos = st.number_input("Cantidad de hijos", step=1, min_value=0)

colAnio, colMes = st.columns(2)
with colAnio:
    anioCasados = st.number_input("Año en el que se casaron", step=1, min_value=0)

with colMes:
    mesCasados = st.number_input(
        "Mes en el que se casaron", step=1, min_value=1, max_value=12
    )

nivelEduH = st.selectbox(
    "Nivel de educación del hombre",
    (
        "Secundaria",
        "Profesional",
        "Preparatoria",
        "Primaria",
        "Otro",
        "Sin escolaridad",
    ),
)

nivelEduM = st.selectbox(
    "Nivel de educación de la mujer",
    (
        "Secundaria",
        "Profesional",
        "Preparatoria",
        "Primaria",
        "Otro",
        "Sin escolaridad",
    ),
)

estatusEmpH = st.selectbox(
    "Estatus de empleo del hombre",
    (
        "Obrero",
        "Empleado",
        "Establecimiento",
        "No trabaja",
        "Patron o empresario",
        "Trabajador por su propia cuenta o en via publica",
        "Trabaja en su vivienda",
        "Jornalero o peon",
        "Trabajador no remunerado",
        "Miembro de cooperativa",
    ),
)

estatusEmpM = st.selectbox(
    "Estatus de empleo de la mujer",
    (
        "Obrero",
        "Empleado",
        "Establecimiento",
        "No trabaja",
        "Patron o empresario",
        "Trabajador por su propia cuenta o en via publica",
        "Trabaja en su vivienda",
        "Jornalero o peon",
        "Trabajador no remunerado",
        "Miembro de cooperativa",
    ),
)

agree = st.checkbox("Viven juntos")
if agree:
    vivenJ = 1
else:
    vivenJ = 0

if st.button("Verificación"):
    df = pd.DataFrame(
        np.array(
            [
                [
                    edadH,
                    edadM,
                    numHijos,
                    anioCasados,
                    mesCasados,
                    nivelEduH,
                    nivelEduM,
                    estatusEmpH,
                    estatusEmpM,
                    vivenJ,
                ]
            ]
        ),
        columns=[
            "Edad hombre",
            "Edad mujer",
            "Cantidad de hijos",
            "Año en el que se casaron",
            "Mes en el que se casaron",
            "Nivel de educación del hombre",
            "Nivel de educación de la mujer",
            "Estatus de empleo del hombre",
            "Estatus de empleo de la mujer",
            "Viven juntos",
        ],
    )
    st.table(df)

# load the model from disk
filename = "divorcios_modelo.sav"
loaded_model = pickle.load(open(filename, "rb"))
print(loaded_model)

if st.button("Calcular"):
    resultado = predecir_anios(
        loaded_model,
        edadH,
        edadM,
        numHijos,
        vivenJ,
        nivelEduH,
        nivelEduM,
        estatusEmpH,
        estatusEmpM,
        anioCasados,
        mesCasados,
    )
    resultado = str(resultado)
    st.metric(
        label="Cuánto durará tu matrimonio",
        value=resultado + " Años",
        delta=None,
    )
