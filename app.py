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
    st.header("1. Datos del Material - Bolsas estándar")
    
    coste_m2 = st.number_input("Coste €/m2", min_value=0.0, value=0.273, step=0.001, format="%.3f")
    ancho_cliente = st.number_input("Ancho cliente en m", min_value=0.0, value=0.150, step=0.001, format="%.3f")
    ancho_material = st.number_input("Ancho material en m", min_value=0.0, value=1.200, step=0.001, format="%.3f")
    largo = st.number_input("Largo en m (Si es lámina = 1)", min_value=0.0, value=0.300, step=0.001, format="%.3f")
    
    cortes = int(ancho_material // largo) if largo > 0 else 0
        
    if cortes > 0:
        coste_materia_prima = coste_m2 * (ancho_material / cortes) * ancho_cliente * 1000 * 2
    else:
        coste_materia_prima = 0.0

    st.markdown("---")
    st.metric(label="Número de Cortes", value=f"{cortes}")
    st.metric(label="Coste materia prima", value=f"{coste_materia_prima:.3f} €")

    st.markdown("---")
    st.header("2. Variables Comerciales")
    
    material_opcion = st.selectbox("Material laminado o impreso", ["Liso", "Impreso"])
    tipo_fabricante = st.selectbox("Tipo de fabricante", ["Transformador", "Multinacional", "Distribuidor"])
    zona_cliente = st.selectbox("Zona del cliente", ["Sur", "Norte"])
    cantidad_bolsas = st.selectbox(
        "Cantidad bolsas", 
        ["menos de 10000", "10000 - 20000", "20000 - 30000", "mas de 30000"]
    )

    if material_opcion == "Liso":
        val_fab = {"Multinacional": 0.69, "Transformador": 0.59, "Distribuidor": 0.50}[tipo_fabricante]
        val_zona = {"Norte": 0.64, "Sur": 0.50}[zona_cliente]
        val_cant = {
            "menos de 10000": 0.57, 
            "10000 - 20000": 0.52, 
            "20000 - 30000": 0.47, 
            "mas de 30000": 0.42
        }[cantidad_bolsas]
    else:
        val_fab = {"Multinacional": 0.89, "Transformador": 0.79, "Distribuidor": 0.70}[tipo_fabricante]
        val_zona = {"Norte": 0.79, "Sur": 0.65}[zona_cliente]
        val_cant = {
            "menos de 10000": 0.82, 
            "10000 - 20000": 0.75, 
            "20000 - 30000": 0.70, 
            "mas de 30000": 0.65
        }[cantidad_bolsas]

    markup_calculado = val_fab + val_zona + val_cant

    st.markdown("---")
    st.header("3. Markup y Precio de Venta")
    
    st.caption("Liso: mínimo 1,42 — Impreso: mínimo 2")
    st.metric(label="Markup", value=f"{markup_calculado:.3f}")

    usar_manual = st.checkbox("Modificar Markup")
    
    if usar_manual:
        markup_propuesto = st.number_input(
            "Markup propuesto (C21)",
            min_value=0.0,
            value=1.400,
            step=0.001,
            format="%.3f"
        )
        precio_1000_bolsas = markup_propuesto * coste_materia_prima
    else:
        precio_1000_bolsas = markup_calculado * coste_materia_prima

    precio_ml = precio_1000_bolsas / 1000

    st.metric(label="Precio de venta sugerido 1000 bolsas", value=f"{precio_1000_bolsas:.3f} €")
    st.metric(label="Precio de venta sugerido ml", value=f"{precio_ml:.3f} €")

elif tipo_producto == "Retráctil":
    st.header("1. Datos del Material - Retráctil")
    
    coste_ml = st.number_input("Coste €/ml", min_value=0.0, value=0.500, step=0.001, format="%.3f")
    espesor = st.number_input("Espesor", min_value=0.0, value=45.0, step=1.0, format="%.1f")
    ancho = st.number_input("Ancho en m", min_value=0.0, value=0.200, step=0.001, format="%.3f")
    largo = st.number_input("Largo en m", min_value=0.0, value=0.400, step=0.001, format="%.3f")
    
    # Coste materia prima = C5 * C8 * 1000
    coste_materia_prima = coste_ml * largo * 1000

    st.markdown("---")
    st.metric(label="Coste materia prima", value=f"{coste_materia_prima:.3f} €")

    st.markdown("---")
    st.header("2. Variables Comerciales")
    
    material_opcion = st.selectbox("Material laminado o impreso", ["Liso", "Impreso"], key="ret_mat")
    tipo_fabricante = st.selectbox("Tipo de fabricante", ["Transformador", "Multinacional", "Distribuidor"], key="ret_fab")
    zona_cliente = st.selectbox("Zona del cliente", ["Sur", "Norte"], key="ret_zona")
    cantidad_bolsas = st.selectbox(
        "Cantidad", 
        ["menos de 10000", "10000 - 20000", "20000 - 30000", "mas de 30000"],
        key="ret_cant"
    )

    if material_opcion == "Liso":
        val_fab = {"Multinacional": 0.69, "Transformador": 0.59, "Distribuidor": 0.50}[tipo_fabricante]
        val_zona = {"Norte": 0.64, "Sur": 0.50}[zona_cliente]
        val_cant = {
            "menos de 10000": 0.57, 
            "10000 - 20000": 0.52, 
            "20000 - 30000": 0.47, 
            "mas de 30000": 0.42
        }[cantidad_bolsas]
    else:
        val_fab = {"Multinacional": 0.89, "Transformador": 0.79, "Distribuidor": 0.70}[tipo_fabricante]
        val_zona = {"Norte": 0.79, "Sur": 0.65}[zona_cliente]
        val_cant = {
            "menos de 10000": 0.82, 
            "10000 - 20000": 0.75, 
            "20000 - 30000": 0.70, 
            "mas de 30000": 0.65
        }[cantidad_bolsas]

    markup_calculado = val_fab + val_zona + val_cant

    st.markdown("---")
    st.header("3. Markup y Precio de Venta")
    
    st.caption("Liso: mínimo 1,42")
    st.metric(label="Markup", value=f"{markup_calculado:.3f}")

    usar_manual = st.checkbox("Modificar Markup propuesto", key="ret_mod")
    
    if usar_manual:
        markup_propuesto = st.number_input(
            "Markup propuesto",
            min_value=0.0,
            value=1.400,
            step=0.001,
            format="%.3f",
            key="ret_mprop"
        )
        precio_venta_sugerido = markup_propuesto * coste_materia_prima
    else:
        precio_venta_sugerido = markup_calculado * coste_materia_prima

    st.metric(label="Precio de venta sugerido", value=f"{precio_venta_sugerido:.3f} €")

else:
    st.info(f"Configuración para '{tipo_producto}' en desarrollo o pendiente de integrar los inputs específicos.")
