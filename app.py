# app.py
import streamlit as st
from core.validators import PatternValidator
from core.extractor import PatternExtractor
from core.report import ReportGenerator

st.set_page_config(page_title="Validador de Patrones", layout="wide")

st.title("🔍 Proyecto — Búsqueda y Validación de Patrones")

tab = st.sidebar.radio("Selecciona una opción", ["Validar campo", "Extraer de texto", "Generar reporte"])

validator = PatternValidator()
extractor = PatternExtractor()
reporter = ReportGenerator()

# --- VALIDAR CAMPO ---
if tab == "Validar campo":
    st.header("✅ Validación individual")
    tipo = st.selectbox("Tipo de dato", [p.name for p in validator.patterns])
    texto = st.text_input("Ingrese el valor a validar")
    if st.button("Validar"):
        result = validator.validate_one(tipo, texto)
        st.write(f"**{result.message}**")

# --- EXTRAER ---
elif tab == "Extraer de texto":
    st.header("📄 Extracción masiva")
    texto = st.text_area("Pega aquí un texto para buscar patrones", height=250)
    if st.button("Extraer patrones"):
        df = extractor.extract_from_text(texto)
        st.dataframe(df)
        st.session_state["df"] = df
        st.success(f"{len(df)} coincidencias encontradas.")

# --- REPORTES ---
elif tab == "Generar reporte":
    st.header("🧾 Exportar resultados")
    if "df" in st.session_state:
        formato = st.selectbox("Formato", ["CSV", "JSON"])
        if st.button("Exportar"):
            df = st.session_state["df"]
            if formato == "CSV":
                archivo = reporter.export_csv(df)
            else:
                archivo = reporter.export_json(df)
            st.success(f"Reporte generado: {archivo}")
    else:
        st.warning("Primero extrae patrones antes de exportar.")
