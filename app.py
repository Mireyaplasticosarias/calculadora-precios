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
    
    if material_opcion == "Liso":
        st.caption("Liso: mínimo 1,22 — máximo 1,55")
    else:
        st.caption("Impreso: mínimo 2 — máximo 2,46")
        
    st.metric(label="Markup", value=f"{markup_calculado:.3f}")

    usar_manual = st.checkbox("Modificar Markup propuesto", key="termo_mod")
    
    if usar_manual:
        markup_propuesto = st.number_input(
            "Markup propuesto",
            min_value=0.0,
            value=1.404,
            step=0.001,
            format="%.3f",
            key="termo_mprop"
        )
        if origen_material == "Fabricado":
            precio_venta_sugerido = coste_materia_prima * (markup_propuesto * 1.07)
        else:
            precio_venta_sugerido = coste_materia_prima * markup_propuesto
    else:
        if origen_material == "Fabricado":
            precio_venta_sugerido = coste_materia_prima * (markup_calculado * 1.07)
        else:
            precio_venta_sugerido = coste_materia_prima * markup_calculado

    st.metric(label="Precio de venta sugerido", value=f"{precio_venta_sugerido:.3f} €")

elif tipo_producto == "Laminado no estándar":
    st.header("1. Datos del Material - Laminado no estándar")
    
    tipo_lam_bolsa = st.selectbox("Lamina o bolsa", ["Lamina", "Bolsa"], key="lam_tipo")
    
    materiales_disponibles = ["PET", "Al", "PE", "PP", "PA", "PE-EVOH", "PP-EVOH", "PET saran"]
    densidades_dict = {
        "PET": 1400, "Al": 2300, "PE": 950, "PP": 950, 
        "PA": 1200, "PE-EVOH": 950, "PP-EVOH": 950, "PET saran": 1400
    }
    
    st.subheader("Configuración de Capas")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mat1 = st.selectbox("Material 1", materiales_disponibles, index=4, key="m1")
        micras1 = st.number_input("Micras", min_value=0.0, value=20.0, step=1.0, format="%.1f", key="mic1")
        coste1 = st.number_input("Coste €/kg", min_value=0.0, value=3.000, step=0.001, format="%.3f", key="cos1")
        dens1 = densidades_dict.get(mat1, 0)
        st.text(f"Densidad: {dens1}")
        
    with col2:
        mat2 = st.selectbox("Material 2", materiales_disponibles, index=2, key="m2")
        micras2 = st.number_input("Micras", min_value=0.0, value=30.0, step=1.0, format="%.1f", key="mic2")
        coste2 = st.number_input("Coste €/kg", min_value=0.0, value=2.700, step=0.001, format="%.3f", key="cos2")
        dens2 = densidades_dict.get(mat2, 0)
        st.text(f"Densidad: {dens2}")
        
    with col3:
        mat3 = st.selectbox("Material 3", ["(Ninguno)"] + materiales_disponibles, index=5, key="m3")
        if mat3 == "(Ninguno)":
            micras3 = 0.0
            coste3 = 0.0
            dens3 = 0
            st.number_input("Micras", min_value=0.0, value=0.0, step=1.0, format="%.1f", key="mic3", disabled=True)
            st.number_input("Coste €/kg", min_value=0.0, value=0.0, step=0.001, format="%.3f", key="cos3", disabled=True)
        else:
            micras3 = st.number_input("Micras", min_value=0.0, value=25.0, step=1.0, format="%.1f", key="mic3")
            coste3 = st.number_input("Coste €/kg", min_value=0.0, value=3.000, step=0.001, format="%.3f", key="cos3")
            dens3 = densidades_dict.get(mat3, 0)
        st.text(f"Densidad: {dens3}")
        
    with col4:
        mat4 = st.selectbox("Material 4", ["(Ninguno)"] + materiales_disponibles, index=0, key="m4")
        if mat4 == "(Ninguno)":
            micras4 = 0.0
            coste4 = 0.0
            dens4 = 0
            st.number_input("Micras", min_value=0.0, value=0.0, step=1.0, format="%.1f", key="mic4", disabled=True)
            st.number_input("Coste €/kg", min_value=0.0, value=0.0, step=0.001, format="%.3f", key="cos4", disabled=True)
        else:
            micras4 = st.number_input("Micras", min_value=0.0, value=0.0, step=1.0, format="%.1f", key="mic4")
            coste4 = st.number_input("Coste €/kg", min_value=0.0, value=0.0, step=0.001, format="%.3f", key="cos4")
            dens4 = densidades_dict.get(mat4, 0)
        st.text(f"Densidad: {dens4}")

    st.markdown("---")
    ancho_cliente = st.number_input("Ancho cliente en m.", min_value=0.0, value=0.715, step=0.001, format="%.3f", key="lam_ac")
    ancho_bobina = st.number_input("Ancho de la bobina en m.", min_value=0.0, value=0.840, step=0.001, format="%.3f", key="lam_ab")
    largo_bolsa = st.number_input("Largo en m. BOLSA", min_value=0.0, value=0.400, step=0.001, format="%.3f", key="lam_lb")
    largo_lamina = st.number_input("Largo LAMINA", min_value=0.0, value=1.000, step=0.001, format="%.3f", key="lam_ll")

    # Cortes exactos según Excel: =IF(C5="Lamina",INT(C12/C11),INT(C12/C13))
    if tipo_lam_bolsa == "Lamina":
        cortes = int(ancho_bobina // ancho_cliente) if ancho_cliente > 0 else 1
    else:
        cortes = int(ancho_bobina // largo_bolsa) if largo_bolsa > 0 else 1
    if cortes < 1: 
        cortes = 1

    st.metric(label="Cortes", value=f"{cortes}")

    capas_datos = []
    if mat1 != "(Ninguno)" and micras1 > 0:
        capas_datos.append((micras1, coste1, dens1))
    if mat2 != "(Ninguno)" and micras2 > 0:
        capas_datos.append((micras2, coste2, dens2))
    if mat3 != "(Ninguno)" and micras3 > 0:
        capas_datos.append((micras3, coste3, dens3))
    if mat4 != "(Ninguno)" and micras4 > 0:
        capas_datos.append((micras4, coste4, dens4))

    if len(capas_datos) > 0 and cortes > 0:
        suma_micras = sum([c[0] for c in capas_datos])
        suma_producto_densidad = sum([c[0] * c[2] for c in capas_datos])
        suma_producto_coste = sum([c[0] * c[1] for c in capas_datos])
        
        densidad_ponderada = suma_producto_densidad / suma_micras if suma_micras > 0 else 0
        coste_kg = suma_producto_coste / suma_micras if suma_micras > 0 else 0
        
        factor_largo_kg = largo_bolsa if tipo_lam_bolsa == "Bolsa" else largo_lamina
        factor_cantidad = 2000 if tipo_lam_bolsa == "Bolsa" else 1
        
        kg_materia_prima = (ancho_bobina / cortes) * factor_largo_kg * factor_cantidad * (suma_micras * 1e-6) * 1.03 * densidad_ponderada
        
        coste_kg_final = coste_kg
        
        if tipo_lam_bolsa == "Bolsa":
            coste_materia_prima_m = kg_materia_prima * (ancho_cliente / largo_bolsa) * coste_kg
        else:
            factor_largo_costem = largo_lamina
            coste_materia_prima_m = (ancho_bobina / cortes) * factor_largo_costem * factor_cantidad * (suma_micras * 1e-6) * 1.03 * densidad_ponderada * coste_kg
    else:
        kg_materia_prima = 0.0
        coste_kg_final = 0.0
        coste_materia_prima_m = 0.0

    st.markdown("---")
    st.metric(label="Kg materia prima", value=f"{kg_materia_prima:.4f} Kg")
    st.metric(label="Coste €/kg", value=f"{coste_kg_final:.3f} €")
    st.metric(label="Coste materia prima €/m", value=f"{coste_materia_prima_m:.3f} €")

    # --- 2. VARIABLES COMERCIALES ---
    st.markdown("---")
    st.header("2. Variables Comerciales")
    
    lam_material_opcion = st.selectbox("Material laminado o impreso", ["Liso", "Impreso"], key="lam_mat_op")
    lam_tipo_fabricante = st.selectbox("Tipo de fabricante", ["Multinacional", "Transformador", "Distribuidor"], key="lam_tipo_fab")
    lam_zona_cliente = st.selectbox("Zona del cliente", ["Norte", "Sur"], key="lam_zona_cli")
    lam_cantidad = st.selectbox("Cantidad", ["menos de 10000", "10000 - 20000", "20000 - 30000", "mas de 30000"], key="lam_cant")

    if tipo_lam_bolsa == "Lamina":
        if lam_material_opcion == "Liso":
            val_fab = {"Multinacional": 0.60, "Transformador": 0.59, "Distribuidor": 0.53}[lam_tipo_fabricante]
            val_zona = {"Norte": 0.63, "Sur": 0.53}[lam_zona_cliente]
            val_cant = {"menos de 10000": 0.56, "10000 - 20000": 0.52, "20000 - 30000": 0.48, "mas de 30000": 0.44}[lam_cantidad]
        else:
            val_fab = {"Multinacional": 0.89, "Transformador": 0.79, "Distribuidor": 0.70}[lam_tipo_fabricante]
            val_zona = {"Norte": 0.79, "Sur": 0.65}[lam_zona_cliente]
            val_cant = {"menos de 10000": 0.82, "10000 - 20000": 0.75, "20000 - 30000": 0.70, "mas de 30000": 0.65}[lam_cantidad]
    else:
        if lam_material_opcion == "Liso":
            val_fab = {"Multinacional": 0.69, "Transformador": 0.59, "Distribuidor": 0.50}[lam_tipo_fabricante]
            val_zona = {"Norte": 0.64, "Sur": 0.50}[lam_zona_cliente]
            val_cant = {"menos de 10000": 0.57, "10000 - 20000": 0.52, "20000 - 30000": 0.47, "mas de 30000": 0.42}[lam_cantidad]
        else:
            val_fab = {"Multinacional": 0.89, "Transformador": 0.79, "Distribuidor": 0.70}[lam_tipo_fabricante]
            val_zona = {"Norte": 0.79, "Sur": 0.65}[lam_zona_cliente]
            val_cant = {"menos de 10000": 0.82, "10000 - 20000": 0.75, "20000 - 30000": 0.70, "mas de 30000": 0.65}[lam_cantidad]

    markup_calculado_lam = val_fab + val_zona + val_cant

    # --- 3. MARKUP Y PRECIO DE VENTA ---
    st.markdown("---")
    st.header("3. Markup y Precio de Venta")
    
    if tipo_lam_bolsa == "Lamina":
            st.caption("Liso: mínimo 1,5 - Impreso: mínimo 2")
      
    else:
        st.caption("Liso: mínimo 1,42 - Impreso: mínimo 2")

    st.metric(label="Markup", value=f"{markup_calculado_lam:.3f}")

    usar_manual_lam = st.checkbox("Modificar Markup", key="lam_mod")
    
    if usar_manual_lam:
        markup_propuesto_lam = st.number_input(
            "Markup propuesto",
            min_value=0.0,
            value=markup_calculado_lam,
            step=0.001,
            format="%.3f",
            key="lam_mprop"
        )
        markup_final = markup_propuesto_lam
    else:
        markup_final = markup_calculado_lam

    precio_sugerido_m = coste_materia_prima_m * markup_final
    precio_sugerido_kg = coste_kg_final * markup_final

    st.metric(label="Precio de venta sugerido €/m", value=f"{precio_sugerido_m:.3f} €")
    st.metric(label="Precio de venta sugerido €/kg", value=f"{precio_sugerido_kg:.3f} €")

else:
    st.info(f"Configuración para '{tipo_producto}' en desarrollo.")
