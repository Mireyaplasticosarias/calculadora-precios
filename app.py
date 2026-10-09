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
        "Cantidad", 
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
    
    st.caption("Liso: mínimo 1,42 - Impreso: mínimo 2")
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
    ancho = st.number_input("Ancho en m", min_value=0.0, value=0.200, step=0.001, format="%.3f")
    largo = st.number_input("Largo en m", min_value=0.0, value=0.400, step=0.001, format="%.3f")
    
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
    
    st.caption("Liso: mínimo 1,42 - Impreso: mínimo 2")
    st.metric(label="Markup", value=f"{markup_calculado:.3f}")

    usar_manual = st.checkbox("Modificar Markup", key="ret_mod")
    
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

elif tipo_producto == "Termoformado":
    st.header("1. Datos del Material - Termoformado")
    
    origen_material = st.selectbox("Origen del material", ["Fabricado", "Comprado"], key="termo_origen")
    
    if origen_material == "Fabricado":
        coste_m2_repo = st.number_input("Coste €/m2 reposición", min_value=0.0, value=0.700, step=0.001, format="%.3f", key="termo_fab_c2")
        ancho_cliente = st.number_input("Ancho cliente (m.)", min_value=0.0, value=0.535, step=0.001, format="%.3f", key="termo_fab_c3")
        ancho_material = st.number_input("Ancho material (m.)", min_value=0.0, value=1.110, step=0.001, format="%.3f", key="termo_fab_c4")
        
        cortes = int(ancho_material // ancho_cliente) if ancho_cliente > 0 else 0
        
        if cortes > 0:
            coste_materia_prima = coste_m2_repo * ancho_material / cortes
        else:
            coste_materia_prima = 0.0

        st.metric(label="Número de Cortes", value=f"{cortes}")
        st.metric(label="Coste materia prima", value=f"{coste_materia_prima:.3f} €")
    else:
        coste_compra = st.number_input("Precio de compra (€ m.l.)", min_value=0.0, value=0.180, step=0.001, format="%.3f", key="termo_comp")
        coste_materia_prima = coste_compra
        st.metric(label="Coste materia prima", value=f"{coste_materia_prima:.3f} €")

    st.markdown("---")
    st.header("2. Variables Comerciales")
    
    material_opcion = st.selectbox("Material laminado o impreso", ["Liso", "Impreso"], key="termo_mat")
    tipo_fabricante = st.selectbox("Tipo de fabricante", ["Multinacional", "Transformador", "Distribuidor"], key="termo_fab")
    zona_cliente = st.selectbox("Zona del cliente", ["Norte", "Sur"], key="termo_zona")
    sector_cliente = st.selectbox("Sector", ["Pescado/pet food/quimicos", "Carne/lacteos/embutido"], key="termo_sec")
    tamano_cliente = st.selectbox("Tamaño", ["Pequeña", "Grande"], key="termo_tam")
    cantidad_opcion = st.selectbox(
        "Cantidad", 
        ["menos de 10000", "10000 - 20000", "20000 - 30000", "mas de 30000"],
        key="termo_cant"
    )

    if material_opcion == "Liso":
        val_fab = {"Multinacional": 0.317, "Transformador": 0.281, "Distribuidor": 0.244}[tipo_fabricante]
        val_zona = {"Norte": 0.281, "Sur": 0.244}[zona_cliente]
        val_sec = {"Pescado/pet food/quimicos": 0.281, "Carne/lacteos/embutido": 0.244}[sector_cliente]
        val_tam = {"Pequeña": 0.281, "Grande": 0.244}[tamano_cliente]
        val_cant = {
            "menos de 10000": 0.354, 
            "10000 - 20000": 0.317, 
            "20000 - 30000": 0.281, 
            "mas de 30000": 0.244
        }[cantidad_opcion]
    else:
        val_fab = {"Multinacional": 0.520, "Transformador": 0.461, "Distribuidor": 0.400}[tipo_fabricante]
        val_zona = {"Norte": 0.461, "Sur": 0.400}[zona_cliente]
        val_sec = {"Pescado/pet food/quimicos": 0.461, "Carne/lacteos/embutido": 0.400}[sector_cliente]
        val_tam = {"Pequeña": 0.461, "Grande": 0.400}[tamano_cliente]
        val_cant = {
            "menos de 10000": 0.580, 
            "10000 - 20000": 0.520, 
            "20000 - 30000": 0.461, 
            "mas de 30000": 0.400
        }[cantidad_opcion]

    markup_calculado = val_fab + val_zona + val_sec + val_tam + val_cant

    st.markdown("---")
    st.header("3. Markup y Precio de Venta")
    
    st.caption("Liso: mínimo 1,22 - Impreso: mínimo 2")
            
    st.metric(label="Markup", value=f"{markup_calculado:.3f}")



    usar_manual = st.checkbox("Modificar Markup", key="termo_mod")
    
    if usar_manual:
        markup_propuesto = st.number_input(
            "Markup propuesto",
            min_value=0.0,
            value=1.404,
            step=0.001,
            format="%.3f",
            key="termo_mprop"
        )
        precio_venta_sugerido = markup_propuesto * coste_materia_prima
    else:
        precio_venta_sugerido = markup_calculado * coste_materia_prima

    st.metric(label="Precio de venta sugerido", value=f"{precio_venta_sugerido:.3f} €")

else:
    st.info(f"Configuración para '{tipo_producto}' en desarrollo o pendiente de integrar los inputs específicos.")
