import streamlit as st

st.set_page_config(page_title="Calculadora de Precios - Plásticos Arias", layout="centered")

st.title("Calculadora de Precios - Plásticos Arias")

# Selección del Producto
tipo_producto = st.selectbox(
    "Selecciona el Tipo de Producto:",
    ["Bolsas estándar-coextruido", "Retráctil", "Termoformado", "Laminado no estándar"]
)

st.divider()

if tipo_producto == "Bolsas estándar-coextruido":
    st.header("1. Parámetros y Costes - Bolsas estándar-coextruido")
    
    tipo_impresion = st.radio("Tipo de acabado:", ["Liso", "Impreso"], horizontal=True)
    
    # Inputs específicos del Excel para Coextruido
    coste_m2 = st.number_input("Coste (€/m2)", min_value=0.0, value=0.50, step=0.01)
    ancho_cliente = st.number_input("Ancho cliente en m", min_value=0.0, value=0.30, step=0.01)
    ancho_material = st.number_input("Ancho material en m", min_value=0.0, value=1.20, step=0.01)
    largo = st.number_input("Largo en m", min_value=0.0, value=0.50, step=0.01)
    
    # Cálculos automáticos
    # Cálculo de cortes (evitando división por cero)
    cortes = int(ancho_material // ancho_cliente) if ancho_cliente > 0 else 1
    if cortes < 1:
        cortes = 1
        
    # Coste de la materia prima (fórmula basada en dimensiones y cortes)
    # Área por bolsa / pieza ajustada por cortes y coste m2
    area_pieza = ancho_cliente * largo
    coste_materia_prima = (area_pieza * coste_m2) / cortes if cortes > 0 else 0.0

    st.markdown("---")
    st.subheader("Resultados de Cálculos de Materia Prima")
    st.metric(label="Número de Cortes", value=f"{cortes}")
    st.metric(label="Coste de la Materia Prima (€)", value=f"{coste_materia_prima:.4f} €")

    st.markdown("---")
    st.subheader("2. Costes Variables y Opciones de Markup")
    
    # Opciones de costes variables / selector de condiciones en función del Excel
    opcion_variable = st.selectbox(
        "Selecciona condición de proceso / variables:",
        ["Estándar", "Volumen alto / Optimizado", "Especial / Complejo"]
    )
    
    # Asignación de markup automático según opción seleccionada y tipo de impresión
    if tipo_impresion == "Liso":
        markup_base = 1.45 if opcion_variable == "Estándar" else (1.40 if opcion_variable == "Volumen alto / Optimizado" else 1.55)
    else:  # Impreso
        markup_base = 1.65 if opcion_variable == "Estándar" else (1.55 if opcion_variable == "Volumen alto / Optimizado" else 1.75)

    usar_markup_manual = st.checkbox("¿Modificar Markup manualmente?")
    
    if usar_markup_manual:
        markup_final = st.number_input(
            "Introduce Markup manual:",
            min_value=1.0,
            value=float(markup_base),
            step=0.01,
            help="El mínimo recomendado para este tipo es acorde a las reglas internas."
        )
        st.text(f"Markup sugerido por sistema: {markup_base:.2f}x")
    else:
        markup_final = markup_base
        st.text(f"Markup aplicado automáticamente: {markup_final:.2f}x")

    st.markdown("---")
    st.subheader("3. Precios de Venta Sugeridos")
    
    # Fórmulas finales de venta
    precio_venta_base = coste_materia_prima * markup_final
    
    # Supuestos de conversión a 1,000 bolsas y por metro lineal (ml)
    # (Ajustar según la fórmula exacta de vuestro Excel si difiere el factor multiplicador)
    precio_1000_bolsas = precio_venta_base * 1000
    precio_ml = precio_venta_base / largo if largo > 0 else 0.0

    st.metric(label="Precio de Venta Sugerido (1.000 bolsas)", value=f"{precio_1000_bolsas:,.2f} €")
    st.metric(label="Precio de Venta Sugerido por metro lineal (ml)", value=f"{precio_ml:,.4f} €")

else:
    # Espacio reservado para los otros 3 productos (Retráctil, Termoformado, Laminado)
    st.info(f"Configuración para '{tipo_producto}' en desarrollo o pendiente de integrar los inputs específicos.")
