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
    
    # Inputs con 3 decimales
    coste_m2 = st.number_input("Coste €/m2 [C5]", min_value=0.0, value=0.500, step=0.001, format="%.3f")
    ancho_cliente = st.number_input("Ancho cliente en m [C6]", min_value=0.0, value=0.150, step=0.001, format="%.3f")
    ancho_material = st.number_input("Ancho material en m [C7]", min_value=0.0, value=1.200, step=0.001, format="%.3f")
    largo = st.number_input("Largo en m [C8]", min_value=0.0, value=0.300, step=0.001, format="%.3f")
    
    # Número de cortes = ENTERO(C7 / C8)
    cortes = int(ancho_material // largo) if largo > 0 else 0
        
    # Coste materia prima exacto del Excel: =C5 * (C7 / C9) * C6 * 1000 * 2
    if cortes > 0:
        coste_materia_prima = coste_m2 * (ancho_material / cortes) * ancho_cliente * 1000 * 2
    else:
        coste_materia_prima = 0.0

    st.markdown("---")
    st.metric(label="Número de Cortes [C9]", value=f"{cortes}")
    st.metric(label="Coste materia prima [C11]", value=f"{coste_materia_prima:.3f} €")

    st.markdown("---")
    st.header("2. Variables Comerciales")
    
    # C14: Material laminado o impreso
    material_opcion = st.selectbox("Material laminado o impreso [C14]", ["Liso", "Impreso"])
    
    # C15: Tipo de fabricante
    tipo_fabricante = st.selectbox("Tipo de fabricante [C15]", ["Multinacional", "Transformador", "Distribuidor"])
    
    # C16: Zona del cliente
    zona_cliente = st.selectbox("Zona del cliente [C16]", ["Norte", "Sur"])
    
    # C17: Cantidad bolsas
    cantidad_bolsas = st.selectbox(
        "Cantidad bolsas [C17]", 
        ["menos de 10000", "10000 - 20000", "20000 - 30000", "mas de 30000"]
    )

    # Lógica de tablas de búsqueda del Excel para el Markup exacto
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

    # Suma total del markup según fórmula de Excel
    markup_calculado = val_fab + val_zona + val_cant

    st.markdown("---")
    st.header("3. Markup y Precio de Venta")
    
    st.metric(label="Markup [C20]", value=f"{markup_calculado:.3f}")

    # Opción de sobreescritura manual (Markup propuesto)
    usar_markup_manual = st.checkbox("¿Modificar Markup manualmente? [C21]")
    
    if usar_markup_manual:
        markup_propuesto = st.number_input(
            "Markup propuesto [C21]:",
            min_value=1.0,
            value=float(markup_calculado),
            step=0.001,
            format="%.3f"
        )
        markup_final = markup_propuesto
    else:
        markup_final = markup_calculado

    # Fórmulas finales de precios de venta
    precio_1000_bolsas = coste_materia_prima * markup_final
    precio_ml = precio_1000_bolsas / 1000

    st.metric(label="Precio de venta sugerido 1000 bolsas [C23]", value=f"{precio_1000_bolsas:.3f} €")
    st.metric(label="Precio de venta sugerido ml [C24]", value=f"{precio_ml:.3f} €")

else:
    st.info(f"Configuración para '{tipo_producto}' en desarrollo o pendiente de integrar los inputs específicos.")
