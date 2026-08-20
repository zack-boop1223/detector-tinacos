import streamlit as st
import pandas as pd
from datetime import datetime
import os
import random

st.set_page_config(
    page_title="Detector Supremo Mega Ultra Macizo de Tinacos",
    page_icon="🗿",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .roast-box {
        background: linear-gradient(135deg, #1a0000, #3d0000);
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #ff2222;
        font-size: 18px;
        margin: 10px 0;
    }
    .big-title {
        font-size: 2.4rem;
        font-weight: 800;
        text-align: center;
    }
    .nivel-tinaco {
        font-size: 1.3rem;
        font-weight: bold;
        color: #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.header("Panel del Juez")
    modo_competencia = st.toggle("Modo Competencia de Tinacos 🗣️🔥", value=False)
    mostrar_historial = st.checkbox("Mostrar historial completo", value=True)
    mostrar_ranking = st.checkbox("Mostrar ranking de peso", value=True)
    activar_sonidos = st.checkbox("Activar sonidos reales", value=True)
    st.markdown("---")
    st.write("Versión: **Tinaco ultra femboy 7000 pro mega 64 1.0 - Con memes incluidos**")
    st.caption("Creado por Zack con amor, gordofobia y cariño hacia ustedes 🗿")

# ====================== TÍTULO ======================
st.markdown('<p class="big-title">Que onda, llena los datos y NO TE ARDAS</p>', unsafe_allow_html=True)
st.caption("Si te ardes facilmente SAL AHORA de esta pagina, aqui no se aceptan niñitas lloronas 🗣️🔥")

# ====================== FORMULARIO ======================
st.subheader("Datos del futuro tinaco... o no")

col1, col2 = st.columns(2)

with col1:
    genero = st.selectbox(
        "Género",
        ["Selecciona una opción", "Hombre", "Mujer", "Otro", "Prefiero no decir", "Helicóptero de combate", "Entidad cósmica"]
    )
    edad = st.number_input("Edad", min_value=1, max_value=120, value=25, step=1)

with col2:
    altura = st.number_input("Altura (cm)", min_value=50, max_value=250, value=170, step=1)
    peso = st.number_input("Peso (kg)", min_value=20.0, max_value=500.0, value=70.0, step=0.5)

# ====================== CÁLCULOS ======================
def calcular_imc(peso, altura_cm):
    if altura_cm <= 0:
        return 0
    return round(peso / ((altura_cm / 100) ** 2), 1)

imc = calcular_imc(peso, altura)

def mensaje_por_peso(peso):
    if peso <= 45:
        return "Estás tan flaco que te pueden usar de tendedero 🥀", "info"
    elif peso <= 65:
        return "Flaco promedio. Aburrido pero aceptable 🔥", "success"
    elif peso <= 85:
        return "Todo bien... por ahora. No te confíes we", "success"
    elif peso <= 100:
        return "Ya se siente el olor a tinaco en el ambiente... precavido 🗿", "warning"
    elif peso <= 120:
        return "A poco y haces cosplay de tinaco de techo we, tírate unas buenas ensaladas y luego regresas 😭", "error"
    elif peso <= 140:
        return "Ya no es tinaco, es cisterna comunitaria. El techo de tu casa está pidiendo el divorcio 💔", "error"
    elif peso <= 170:
        return "Wey... el satélite te tiene catalogado como 'anomalía gravitacional'. Baja o te hacen parque nacional 🗿🗣️", "error"
    elif peso <= 200:
        return "Esto ya es un evento tectónico. Estás formando un nuevo relieve montañoso 😭🙏", "error"
    else:
        return "FELICIDADES, acabas de ser declarado CONTINENTE. La ONU quiere hablar contigo 🗿🌍", "error"

mensaje_peso, tipo = mensaje_por_peso(peso)

def mensaje_imc(imc):
    if imc == 0:
        return "Pon la altura bien o te doy de baja del sistema"
    elif imc < 18.5:
        return f"IMC {imc} → Modo esqueleto activado. Come algo que no sea luz solar 🥀"
    elif imc < 25:
        return f"IMC {imc} → Rango normal. Qué aburrido, ni para roast sirves 🔥"
    elif imc < 30:
        return f"IMC {imc} → Sobrepeso oficial. El tinaco ya está en fase de prototipo"
    elif imc < 35:
        return f"IMC {imc} → Obesidad grado 1. El cosplay ya tiene luces LED"
    elif imc < 40:
        return f"IMC {imc} → Obesidad grado 2. El tinaco ya tiene nombre propio"
    else:
        return f"IMC {imc} → Obesidad grado 3. Caso clínico + atracción turística 😭🥀"

def comentario_genero(g):
    dic = {
        "Hombre": "Clásico hombre que dice 'es puro músculo' mientras se le rompe la silla 🗿",
        "Mujer": "Mujer que lleva 4 años diciendo 'es retención de líquidos' 💔",
        "Otro": "Identidad compleja + densidad compleja = combo peligroso",
        "Prefiero no decir": "Misterioso como el fondo de un tinaco sin limpiar",
        "Helicóptero de combate": "Ah ya, por eso el peso. Perdón por dudar",
        "Entidad cósmica": "Tiene sentido... ningun humano pesa así"
    }
    return dic.get(g, "")

def comentario_edad(e):
    if e < 18:
        return "Menor de edad y ya en estas ligas... tus papás van a llorar 😭🙏"
    elif e < 28:
        return "En tu prime teórico... y aún así, así vas 🥀"
    elif e < 40:
        return "La crisis de los 30 ya no es emocional, es física"
    elif e < 55:
        return "A esta edad ya deberías tener más dignidad que peso we 😭🙏"
    else:
        return "Abuelo tinaco detectado. El IMSS está nervioso"

def comentario_altura(a):
    if a < 155:
        return "Bajito y denso = máxima concentración de tinaco por cm³"
    elif a < 170:
        return "Estatura promedio, peso no tanto..."
    elif a < 185:
        return "Altura decente, lastima el lastre 😭"
    else:
        return "Alto y pesado = eres un edificio de departamentos we 😭🙏"

def nivel_tinaco(peso, imc):
    puntos = 0
    if peso > 100: puntos += 30
    if peso > 130: puntos += 25
    if peso > 160: puntos += 25
    if peso > 200: puntos += 20
    if imc > 30: puntos += 15
    if imc > 35: puntos += 15
    if imc > 40: puntos += 20
    return min(puntos, 100)

nivel = nivel_tinaco(peso, imc)

# ====================== RESULTADOS ======================
st.markdown("---")
st.subheader("Diagnóstico Oficial por el medico Elpi Ton")

if tipo == "error":
    st.markdown(f'<div class="roast-box">{mensaje_peso}</div>', unsafe_allow_html=True)
elif tipo == "warning":
    st.warning(mensaje_peso)
elif tipo == "success":
    st.success(mensaje_peso)
else:
    st.info(mensaje_peso)

st.write(mensaje_imc(imc))

if genero != "Selecciona una opción":
    st.write(f"**Género:** {comentario_genero(genero)}")
st.write(f"**Edad:** {comentario_edad(edad)}")
st.write(f"**Altura:** {comentario_altura(altura)}")

# Medidor
st.markdown("---")
st.markdown(f'<p class="nivel-tinaco">Nivel de Tinaco: {nivel}/100</p>', unsafe_allow_html=True)
st.progress(nivel / 100)

if nivel >= 80:
    st.error("⚠️ ALERTA MÁXIMA: Estás en zona de extinción de sillas")
elif nivel >= 50:
    st.warning("El tinaco ya tiene derechos de autor")
elif nivel >= 20:
    st.info("Todavía hay esperanza... poquita, pero hay")

# ====================== MEMES ======================
st.markdown("---")
st.subheader("Meme del momento")

if nivel >= 70:
    st.image("https://i.kym-cdn.com/photos/images/newsfeed/001/431/201/40f.png", 
             caption="Cuando te pesas y sale el número...", use_container_width=True)
elif nivel >= 40:
    st.image("https://i.kym-cdn.com/photos/images/newsfeed/001/007/322/1d2.jpeg", 
             caption="Yo viendo mi peso y fingiendo que todo está bien", use_container_width=True)
else:
    st.info("Todavía no mereces meme de tinaco. Sigue así... o no.")

# ====================== SONIDOS ======================
if activar_sonidos and nivel >= 50:
    st.markdown("### Sonido de juicio LOL")
    st.audio("https://archive.org/download/vine-boom-sound-effect-longer-verison-for-real/Vine%20Boom%20Sound%20Effect%20%28Longer%20Verison%20For%20Real%29.mp3")

# ====================== BOTONES DE CAOS ======================
st.markdown("---")
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("💥 Dame otro roast (modo sadismo)"):
        roasts_extra = [
            "Tu báscula ya pidió cambio de carrera",
            "Hasta el eco tiene miedo de repetir tu peso",
            "Los zapatos ya hicieron un grupo de apoyo",
            "El elevador te ve y finge que está descompuesto",
            "Tu sombra pesa más que la mayoría de la gente",
            "Si te caes, se forma un cráter y declaran zona de desastre",
            "Los nutricionistas te usan como amenaza para los niños",
            "Hasta Google Maps te marca como 'obstáculo'"
        ]
        st.error(random.choice(roasts_extra))
        st.toast("Roast entregado 🗿", icon="💥")

with col_btn2:
    if st.button("Plan de dieta cruel", icon="🥀"):
        planes = [
            "Desayuno: arrepentimiento. Comida: culpa. Cena: vacío existencial.",
            "Solo se permite masticar el aire y llorar en posición fetal.",
            "Camina hasta que el GPS te marque como 'objeto en movimiento peligroso'.",
            "Cada vez que abras la refri, di en voz alta: 'No soy digno'.",
            "Tu nueva dieta se llama 'Supervivencia del más arrepentido'.",
            "Si sobrevives 30 días sin taquitos, te damos una medalla de cartón."
        ]
        st.error(random.choice(planes))
        st.balloons()
        st.toast("Plan generado... buena suerte 😭🥀🥀")

# ====================== GUARDAR ======================
archivo = "historial_tinacos.csv"

st.markdown("---")
if st.button("Guardar este tinaco en el historial",  icon="😭"):
    if genero == "Selecciona una opción":
        st.warning("Selecciona el género, no seas ratero de datos")
    else:
        nuevo = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "genero": genero,
            "edad": edad,
            "altura_cm": altura,
            "peso_kg": peso,
            "imc": imc,
            "nivel_tinaco": nivel
        }
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
            df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
        else:
            df = pd.DataFrame([nuevo])
        df.to_csv(archivo, index=False)
        st.success("Guardado. Ahora eres parte de la leyenda de los tinacos 🗿")
        st.toast("Tinaco registrado")

# ====================== RANKING E HISTORIAL ======================
if os.path.exists(archivo):
    df = pd.read_csv(archivo)
    
    if mostrar_ranking and len(df) > 0:
        st.markdown("---")
        st.subheader("Ranking de los Tinacos Más Pesados")
        ranking = df.sort_values("peso_kg", ascending=False).head(10).reset_index(drop=True)
        ranking.index = ranking.index + 1
        st.dataframe(ranking[["fecha", "genero", "edad", "peso_kg", "imc", "nivel_tinaco"]], use_container_width=True)
        
        campeon = ranking.iloc[0]
        st.error(f"**EL MAYOR GORDO ES:** {campeon['peso_kg']} kg — Nivel Tinaco {campeon['nivel_tinaco']}/100")

    if mostrar_historial:
        st.markdown("---")
        st.subheader("Historial completo de MAYORES TINACOS HISTORICOS 😭😭")
        st.dataframe(df.tail(15), use_container_width=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Borrar TODO el historial porque soy semejante tinaco y me ardi 😭🥀🥀🥀"):
                os.remove(archivo)
                st.success("Historial eliminado. Nadie sabrá nunca lo que pasó aquí. ")
                st.rerun()
        with col_b:
            st.download_button(
                "📥 Descargar historial CSV",
                df.to_csv(index=False).encode("utf-8"),
                "historial_tinacos.csv",
                "text/csv"
            )

# ====================== MODO COMPETENCIA ======================
if modo_competencia and os.path.exists(archivo):
    st.markdown("---")
    st.subheader("Modo Competencia de Tinacos")
    df_comp = pd.read_csv(archivo)
    if len(df_comp) >= 2:
        top3 = df_comp.sort_values("peso_kg", ascending=False).head(3)
        for i, row in enumerate(top3.itertuples(), 1):
            medalla = ["🥇", "🥈", "🥉"][i-1]
            st.write(f"{medalla} **Puesto {i}:** {row.peso_kg} kg — {row.genero} — Nivel {row.nivel_tinaco}")
    else:
        st.info("Se necesitan al menos 2 víctimas para iniciar la competencia")

# ====================== RESET ======================
st.markdown("---")
if st.button("🔄 Resetear formulario (me arrepentí de todo)"):
    st.rerun()

st.markdown("---")
st.caption("Pagina desarrollada con 0% de empatía y 100% de verdad cruda • Úsala bajo tu propio riesgo emocional")