import pandas as pd
import numpy as np


def datos_a_dataframe(
    edad_h,
    edad_m,
    numero_hijos,
    viven_juntos,
    nivel_educ_h,
    nivel_educ_m,
    estatus_empleo_h,
    estatus_empleo_m,
    anio_matrimonio,
    mes_matrimonio,
):
    data = {
        "edad_h": edad_h,
        "edad_m": edad_m,
        "numero_hijos": numero_hijos,
        "viven_juntos": viven_juntos,
        "diferencia_edades": abs(edad_h - edad_m),
        "NE_h_OTRO": 1 if nivel_educ_h.upper() == "OTRO" else 0,
        "NE_h_PREPARATORIA": 1 if nivel_educ_h.upper() == "PREPARATORIA" else 0,
        "NE_h_PRIMARIA": 1 if nivel_educ_h.upper() == "PRIMARIA" else 0,
        "NE_h_PROFESIONAL": 1 if nivel_educ_h.upper() == "PROFESIONAL" else 0,
        "NE_h_SECUNDARIA": 1 if nivel_educ_h.upper() == "SECUNDARIA" else 0,
        "NE_h_SIN ESCOLARIDAD": 1 if nivel_educ_h.upper() == "SIN ESCOLARIDAD" else 0,
        "NE_m_OTRO": 1 if nivel_educ_m.upper() == "OTRO" else 0,
        "NE_m_PREPARATORIA": 1 if nivel_educ_m.upper() == "PREPARATORIA" else 0,
        "NE_m_PRIMARIA": 1 if nivel_educ_m.upper() == "PRIMARIA" else 0,
        "NE_m_PROFESIONAL": 1 if nivel_educ_m.upper() == "PROFESIONAL" else 0,
        "NE_m_SECUNDARIA": 1 if nivel_educ_m.upper() == "SECUNDARIA" else 0,
        "NE_m_SIN ESCOLARIDAD": 1 if nivel_educ_m.upper() == "SIN ESCOLARIDAD" else 0,
        "empleo_h_EMPLEADO": 1 if estatus_empleo_h.upper() == "EMPLEADO" else 0,
        "empleo_h_ESTABLECIMIENTO": 1
        if estatus_empleo_h.upper() == "ESTABLECIMIENTO"
        else 0,
        "empleo_h_JORNALERO O PEON": 1
        if estatus_empleo_h.upper() == "JORNALERO O PEON"
        else 0,
        "empleo_h_MIEMBRO DE COOPERATIVA": 1
        if estatus_empleo_h.upper() == "MIEMBRO DE COOPERATIVA"
        else 0,
        "empleo_h_NO TRABAJA": 1 if estatus_empleo_h.upper() == "NO TRABAJA" else 0,
        "empleo_h_OBRERO": 1 if estatus_empleo_h.upper() == "OBRERO" else 0,
        "empleo_h_PATRON O EMPRESARIO": 1
        if estatus_empleo_h.upper() == "PATRON O EMPRESARIO"
        else 0,
        "empleo_h_TRABAJA EN SU VIVIENDA": 1
        if estatus_empleo_h.upper() == "TRABAJA EN SU VIVIENDA"
        else 0,
        "empleo_h_TRABAJADOR NO REMUNERADO": 1
        if estatus_empleo_h.upper() == "TRABAJADOR NO REMUNERADO"
        else 0,
        "empleo_h_TRABAJADOR POR SU PROPIA CUENTA O EN VIA PUBLICA": 1
        if estatus_empleo_h.upper()
        == "TRABAJADOR POR SU PROPIA CUENTA O EN VIA PUBLICA"
        else 0,
        "empleo_m_EMPLEADO": 1 if estatus_empleo_m.upper() == "EMPLEADO" else 0,
        "empleo_m_ESTABLECIMIENTO": 1
        if estatus_empleo_m.upper() == "ESTABLECIMIENTO"
        else 0,
        "empleo_m_JORNALERO O PEON": 1
        if estatus_empleo_m.upper() == "JORNALERO O PEON"
        else 0,
        "empleo_m_MIEMBRO DE COOPERATIVA": 1
        if estatus_empleo_m.upper() == "MIEMBRO DE COOPERATIVA"
        else 0,
        "empleo_m_NO TRABAJA": 1 if estatus_empleo_m.upper() == "NO TRABAJA" else 0,
        "empleo_m_OBRERO": 1 if estatus_empleo_m.upper() == "OBRERO" else 0,
        "empleo_m_PATRON O EMPRESARIO": 1
        if estatus_empleo_m.upper() == "PATRON O EMPRESARIO"
        else 0,
        "empleo_m_TRABAJA EN SU VIVIENDA": 1
        if estatus_empleo_m.upper() == "TRABAJA EN SU VIVIENDA"
        else 0,
        "empleo_m_TRABAJADOR NO REMUNERADO": 1
        if estatus_empleo_m.upper() == "TRABAJADOR NO REMUNERADO"
        else 0,
        "empleo_m_TRABAJADOR POR CUENTA PROPIA EN VIA PUBLICA ": 1
        if estatus_empleo_m.upper()
        == "TRABAJADOR POR SU PROPIA CUENTA O EN VIA PUBLICA"
        else 0,
        "anio_matrimonio": anio_matrimonio,
        "mes_matrimonio": mes_matrimonio,
    }

    return pd.DataFrame(data, index=[0])


def predecir_anios(
    modelo,
    edad_h,
    edad_m,
    numero_hijos,
    viven_juntos,
    nivel_educ_h,
    nivel_educ_m,
    estatus_empleo_h,
    estatus_empleo_m,
    anio_matrimonio,
    mes_matrimonio,
):
    data = {
        "edad_h": edad_h,
        "edad_m": edad_m,
        "numero_hijos": numero_hijos,
        "viven_juntos": viven_juntos,
        "diferencia_edades": abs(edad_h - edad_m),
        "NE_h_OTRO": 1 if nivel_educ_h.upper() == "OTRO" else 0,
        "NE_h_PREPARATORIA": 1 if nivel_educ_h.upper() == "PREPARATORIA" else 0,
        "NE_h_PRIMARIA": 1 if nivel_educ_h.upper() == "PRIMARIA" else 0,
        "NE_h_PROFESIONAL": 1 if nivel_educ_h.upper() == "PROFESIONAL" else 0,
        "NE_h_SECUNDARIA": 1 if nivel_educ_h.upper() == "SECUNDARIA" else 0,
        "NE_h_SIN ESCOLARIDAD": 1 if nivel_educ_h.upper() == "SIN ESCOLARIDAD" else 0,
        "NE_m_OTRO": 1 if nivel_educ_m.upper() == "OTRO" else 0,
        "NE_m_PREPARATORIA": 1 if nivel_educ_m.upper() == "PREPARATORIA" else 0,
        "NE_m_PRIMARIA": 1 if nivel_educ_m.upper() == "PRIMARIA" else 0,
        "NE_m_PROFESIONAL": 1 if nivel_educ_m.upper() == "PROFESIONAL" else 0,
        "NE_m_SECUNDARIA": 1 if nivel_educ_m.upper() == "SECUNDARIA" else 0,
        "NE_m_SIN ESCOLARIDAD": 1 if nivel_educ_m.upper() == "SIN ESCOLARIDAD" else 0,
        "empleo_h_EMPLEADO": 1 if estatus_empleo_h.upper() == "EMPLEADO" else 0,
        "empleo_h_ESTABLECIMIENTO": 1
        if estatus_empleo_h.upper() == "ESTABLECIMIENTO"
        else 0,
        "empleo_h_JORNALERO O PEON": 1
        if estatus_empleo_h.upper() == "JORNALERO O PEON"
        else 0,
        "empleo_h_MIEMBRO DE COOPERATIVA": 1
        if estatus_empleo_h.upper() == "MIEMBRO DE COOPERATIVA"
        else 0,
        "empleo_h_NO TRABAJA": 1 if estatus_empleo_h.upper() == "NO TRABAJA" else 0,
        "empleo_h_OBRERO": 1 if estatus_empleo_h.upper() == "OBRERO" else 0,
        "empleo_h_PATRON O EMPRESARIO": 1
        if estatus_empleo_h.upper() == "PATRON O EMPRESARIO"
        else 0,
        "empleo_h_TRABAJA EN SU VIVIENDA": 1
        if estatus_empleo_h.upper() == "TRABAJA EN SU VIVIENDA"
        else 0,
        "empleo_h_TRABAJADOR NO REMUNERADO": 1
        if estatus_empleo_h.upper() == "TRABAJADOR NO REMUNERADO"
        else 0,
        "empleo_h_TRABAJADOR POR SU PROPIA CUENTA O EN VIA PUBLICA": 1
        if estatus_empleo_h.upper()
        == "TRABAJADOR POR SU PROPIA CUENTA O EN VIA PUBLICA"
        else 0,
        "empleo_m_EMPLEADO": 1 if estatus_empleo_m.upper() == "EMPLEADO" else 0,
        "empleo_m_ESTABLECIMIENTO": 1
        if estatus_empleo_m.upper() == "ESTABLECIMIENTO"
        else 0,
        "empleo_m_JORNALERO O PEON": 1
        if estatus_empleo_m.upper() == "JORNALERO O PEON"
        else 0,
        "empleo_m_MIEMBRO DE COOPERATIVA": 1
        if estatus_empleo_m.upper() == "MIEMBRO DE COOPERATIVA"
        else 0,
        "empleo_m_NO TRABAJA": 1 if estatus_empleo_m.upper() == "NO TRABAJA" else 0,
        "empleo_m_OBRERO": 1 if estatus_empleo_m.upper() == "OBRERO" else 0,
        "empleo_m_PATRON O EMPRESARIO": 1
        if estatus_empleo_m.upper() == "PATRON O EMPRESARIO"
        else 0,
        "empleo_m_TRABAJA EN SU VIVIENDA": 1
        if estatus_empleo_m.upper() == "TRABAJA EN SU VIVIENDA"
        else 0,
        "empleo_m_TRABAJADOR NO REMUNERADO": 1
        if estatus_empleo_m.upper() == "TRABAJADOR NO REMUNERADO"
        else 0,
        "empleo_m_TRABAJADOR POR CUENTA PROPIA EN VIA PUBLICA ": 1
        if estatus_empleo_m.upper()
        == "TRABAJADOR POR SU PROPIA CUENTA O EN VIA PUBLICA"
        else 0,
        "anio_matrimonio": anio_matrimonio,
        "mes_matrimonio": mes_matrimonio,
    }

    muestra = pd.DataFrame(data, index=[0])

    return int(modelo.predict(muestra)[0])
