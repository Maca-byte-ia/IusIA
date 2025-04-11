
import streamlit as st
import json

st.set_page_config(page_title='Somnia Magna – IA Jurídica', layout='wide')

# --- Estilos ---
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
        }
        .css-1d391kg {
            background-color: #111;
        }
        .css-18e3th9 {
            padding: 2rem 2rem 2rem 2rem;
        }
        h1, h2, h3, h4 {
            color: #E3E3E3;
        }
    </style>
""", unsafe_allow_html=True)

# --- Menú lateral ---
menu = st.sidebar.radio("Menú", ["Interpretar Artículos", "Modo Estudio", "Simular Juicio", "Investigar Juicios", "Biblioteca"])

st.title("Somnia Magna – IA Jurídica")

# --- Sección 1: Interpretar Artículos ---
if menu == "Interpretar Artículos":
    st.header("Interpretación de Artículos")
    tipo = st.selectbox("Selecciona el cuerpo legal", ["Código Penal", "Código Civil", "Constitución Española"])
    articulo = st.text_input("Número de artículo")

    if st.button("Interpretar"):
        archivo = {
            "Código Penal": "codigo_penal_completo.json",
            "Código Civil": "codigo_civil_completo.json",
            "Constitución Española": "constitucion_espanola.json"
        }[tipo]

        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                resultados = [a for a in data["articulos"] if articulo in a["articulo"]]
                if resultados:
                    for r in resultados:
                        st.subheader(f"{r['articulo']}")
                        st.code(f"{r['texto']}")
                        st.info("Interpretación profesional: (simulada) Este artículo regula aspectos fundamentales dentro del marco legal...")
                else:
                    st.warning("Artículo no encontrado.")
        except:
            st.error("No se pudo cargar el archivo legal.")

# --- Sección 2: Modo Estudio ---
elif menu == "Modo Estudio":
    st.header("Modo Estudio")
    st.text_input("Pregunta jurídica")
    st.file_uploader("Sube apuntes o modelos de examen", type=["pdf", "docx", "txt"])
    st.success("Modo estudio activo. Esta es una demo visual.")

# --- Sección 3: Simular Juicio ---
elif menu == "Simular Juicio":
    st.header("Simulador de Juicio")
    st.selectbox("Elige tu rol", ["Juez", "Abogado", "Cliente", "Parte contraria"])
    st.text_area("Describe tu caso o deja que la IA lo genere automáticamente")
    st.button("Iniciar Simulación")
    st.success("Simulador cargado. Próximamente interactivo.")

# --- Sección 4: Investigar Juicios ---
elif menu == "Investigar Juicios":
    st.header("Investigación de Juicios Reales")
    try:
        with open("juicios_reales.json", "r", encoding="utf-8") as f:
            juicios = json.load(f)
            for j in juicios:
                st.subheader(f"{j['tipo']} – {j['resultado']}")
                st.write(f"Abogado: {j['abogado']}")
    except:
        st.warning("No se encontró el archivo de juicios.")

# --- Sección 5: Biblioteca Jurídica ---
elif menu == "Biblioteca":
    st.header("Biblioteca Jurídica")
    try:
        with open("biblioteca.json", "r", encoding="utf-8") as f:
            libros = json.load(f)
            for libro in libros:
                st.write(f"**{libro['titulo']}** – {libro['autor']}")
    except:
        st.warning("No se pudo cargar la biblioteca.")
