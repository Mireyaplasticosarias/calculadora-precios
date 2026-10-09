import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Herramienta de Precios",
    page_icon="🧮",
    layout="wide"
)

# Estilo visual general
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem;
        color: #1f77b4;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 20px;
    }
    .rule-box {
        background-color: #f0f2f6;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 0.9rem;
        color: #31333F;
        margin-bottom: 20px;
        border-left: 5px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar el estado de la sesión para la navegación
if "opcion_seleccionada" not in st.session_state:
    st.session_state.opcion_seleccionada = None

def volver_inicio():
    st.session_state.opcion_seleccionada = None

# --- PANTALLA DE INICIO (MENÚ PRINCIPAL) ---
if st.session_state.opcion_seleccionada is None:
    st.markdown('<p class="main-title">🧮 Herramienta de Cálculo de Precios</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Selecciona el tipo de producto para comenzar el cálculo:</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📦 Bolsas estándar-coextruido", use_container_width=True, type="primary"):
            st.session_state.opcion_seleccionada = "Bolsas estándar-coextruido"
            st.rerun()
            
        if st.button("🌡️ Termoformado", use_container_width=True, type="primary"):
            st.session_state.opcion_seleccionada = "Termoformado"
            st.rerun()
            
    with col2:
        if st.button("🔄 Retráctil", use_container_width=True, type="primary"):
            st.session_state.opcion_seleccionada = "Retráctil"
            st.rerun()
            
        if st.button("📜 Laminado no estándar", use_container_width=True, type="primary"):
            st.session_state.opcion_seleccionada = "Laminado no estándar"
            st.rerun()

else:
    # --- PANTALLA DE CÁLCULO ---
    opcion = st.session_state.opcion_seleccionada
    
    # Barra lateral con botón de inicio
    with st.sidebar:
        st.subheader("Navegación")
        if st.button("⬅️ Volver al Inicio", use_container_width=True):
            volver_inicio()
            st.rerun()
        st.divider()
        st.info(f"Estás calculando:\n**{opcion}**")

    st.markdown(f'<p class="main-title">Calculadora: {opcion}</p>', unsafe_allow_html=True)
    st.markdown("---")

    # Mostrar el texto de las reglas de markup exactas según la opción seleccionada
    if opcion in ["Bolsas estándar-coextruido", "Retráctil"]:
        st.markdown('<div class="rule-box"><b>Regla de Markup:</b> En Bolsas estándar-coextruido o Retráctil, el markup mínimo si se pone a mano es <b>1,42</b> si es liso y <b>2</b> si es impreso.</div>', unsafe_allow_html=True)
        markup_liso = 1.42
        markup_impreso = 2.0
    elif opcion == "Termoformado":
        st.markdown('<div class="rule-box"><b>Regla de Markup:</b> Si es Termoformado, el markup mínimo si se pone a mano es <b>1,22</b> si es liso y <b>2</b> si es impreso.</div>', unsafe_allow_html=True)
        markup_liso = 1.22
        markup_impreso = 2.0
    elif opcion == "Laminado no estándar":
        st.markdown('<div class="rule-box"><b>Regla de Markup:</b> Si es Laminado no estándar, el markup mínimo si se pone a mano es <b>1,5</b> si es liso y <b>2</b> si es impreso.</div>', unsafe_allow_html=True)
        markup_liso = 1.5
        markup_impreso = 2.0

    # Layout de entradas de datos
    col_inputs, col_resultados = st.columns([1.2, 1])

    with col_inputs:
        st.subheader("1. Inputs y Variables")
        
        tipo_impresion = st.radio("Tipo de acabado:", ["Liso", "Impreso"], horizontal=True)
        
        # Inputs genéricos adaptados a la simulación de costes
        coste_materia_prima = st.number_input("Coste de Materia Prima / Fabricación (€)", min_value=0.0, value=50.0, step=1.0)
        costes_adicionales = st.number_input("Costes Indirectos / Manipulación (€)", min_value=0.0, value=10.0, step=1.0)
        
        # Markup automático por defecto según selección
        markup_sugerido_default = markup_liso if tipo_impresion == "Liso" else markup_impreso
        
        usar_markup_manual = st.checkbox("¿Modificar Markup manualmente?")
        
        if usar_markup_manual:
            markup_manual = st.number_input(
                "Introduce Markup manual:", 
                min_value=1.0, 
                value=float(markup_sugerido_default), 
                step=0.01,
                help=f"El mínimo recomendado para este tipo en modo {tipo_impresion} es {markup_sugerido_default}"
            )
            markup_final = markup_manual
        else:
            markup_final = markup_sugerido_default
            st.text(f"Markup aplicado automáticamente: {markup_final}")

    with col_resultados:
        st.subheader("2. Resultados")
        
        # Cálculos de precio de fabricación y venta
        precio_fabricacion = coste_materia_prima + costes_adicionales
        precio_venta = precio_fabricacion * markup_final
        beneficio = precio_venta - precio_fabricacion
        
        st.metric(label="Coste de Fabricación Total", value=f"{precio_fabricacion:.2f} €")
        st.metric(label="Markup Aplicado", value=f"{markup_final:.2f}x")
        st.metric(label="Precio de Venta Sugerido", value=f"{precio_venta:.2f} €")
        st.metric(label="Margen de Beneficio Estimado", value=f"{beneficio:.2f} €")
