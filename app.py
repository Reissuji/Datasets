import streamlit as st
import pandas as pd

# Diccionario de mapeo de sensaciones a tonalidades
sensaciones_a_tonalidades = {
    "Escandinavo": "Frío",
    "Tropical": "Cálido",
    "Bohemio": "Cálido",
    "Moderno": "Frío",
    "Contemporáneo": "Ambos",
    "Rústico": "Cálido",
    "Vintage": "Cálido",
    "Minimalista": "Frío",
    "Elegante": "Cálido",
    "Zen": "Frío",
    "Natural": "Frío",
    "Clásico": "Cálido",
    "Provenzal": "Cálido",
    "Mediterráneo": "Cálido",
    "Victoriano": "Cálido",
    "de Jardín": "Cálido"
}

# Mapeo de tonalidades a valores numéricos
tonalidades_a_valores = {
    "Cálido": 2.0,
    "Frío": 0.0,
    "Ambos": 1.0
}

def entrada_usuario():
    toxic = st.slider("¿Le importa que la planta sea tóxica?", 0, 1, 0)
    conocimiento = st.slider("¿Cuánto sabe sobre plantas?", 0, 3, 0)
    tiempo = st.slider("¿Cuánto tiempo libre tiene?", 0, 3, 0)
    clima = st.slider("¿Vive en un clima no seco?", 0, 1, 0)
    tonos_calidos = st.slider("¿Le gustan los tonos cálidos?", 0, 1, 0)
    tonos_frios = st.slider("¿Prefiere tonos fríos?", 0, 1, 0)
    tonos_indiferente = st.slider("¿Le son indiferentes los tonos?", 0, 1, 0)
    adosado = st.slider("¿Vive en un adosado?", 0, 1, 0)
    apartamento = st.slider("¿Vive en un apartamento?", 0, 1, 0)
    chalet = st.slider("¿Vive en un chalet?", 0, 1, 0)
    dificultad = st.slider("¿Cómo de complejo se atreve a que sea el cuidado de la planta?", 0, 3, 0)
    ubicacion = st.slider("¿Prefiere de interior o exterior?", 0, 1, 0)
    estatura = st.slider("¿Cómo de grande puede ser la planta?", 0, 2, 0)
    riego = st.slider("¿Cuánto estima que recordará el riego?", 0, 3, 0)
    mediterraneo = st.slider("¿Se encuentra en un clima mediterráneo seco?", 0, 1, 0)
    mascotas = st.slider("¿Tiene mascotas o hijos?", 0, 1, 0)
    
    sensacion_input = st.selectbox("Ingrese el estilo más representativo de su hogar", list(sensaciones_a_tonalidades.keys()))
    sensacion_tonalidad = sensaciones_a_tonalidades.get(sensacion_input, "Ambos")
    sensacion = tonalidades_a_valores[sensacion_tonalidad]

    return [
        toxic, conocimiento, tiempo, clima, tonos_calidos, tonos_frios, tonos_indiferente,
        adosado, apartamento, chalet, dificultad, ubicacion, estatura, riego,
        mediterraneo, mascotas, sensacion
    ]

def recomendar_planta_usuario(usuario, df, feature_columns):
    # Aquí debes implementar tu lógica de recomendación
    return "Ejemplo de Planta"

df = pd.DataFrame()  # Carga aquí tu dataframe
feature_columns = []  # Define aquí tus columnas de características

st.title("Sistema de Recomendación de Plantas")

if st.button("Obtener recomendación"):
    usuario = entrada_usuario()
    mejor_planta = recomendar_planta_usuario(usuario, df, feature_columns)
    st.write(f"La mejor planta recomendada es: {mejor_planta}")
