import random
import streamlit as st
import time

st.set_page_config(page_title="Piedra, Papel y Tijera", page_icon="🏆")

st.title("Piedra, Papel y Tijera")

Rondas = 1
Victorias = 0
Vidas = 3
Rondas_Vidas = 10

Vida_3 = "❤️❤️❤️"
Vida_2 = "❤️❤️🖤"
Vida_1 = "❤️🖤🖤"
Vida_0 = "🖤🖤🖤"

def mostrar_vidas(i):
    if i == 3: return Vida_3
    if i == 2: return Vida_2
    if i == 1: return Vida_1
    else: return Vida_0

Vencer = {
    
    "📋 Papel 📋": "🪨 Piedra 🪨",
    "🪨 Piedra 🪨": "✂️ Tijera ✂️",
    "✂️ Tijera ✂️": "📋 Papel 📋"
    
}

Opciones = ["🪨 Piedra 🪨", "📋 Papel 📋", "✂️ Tijera ✂️"]

def resultado(Jugador, Bot):
    if Vencer[Jugador] == Bot:
        return "Jugador"
    if Jugador == Bot:
        return "Empate"
    else:
        return "Bot"

if "Vidas" not in st.session_state:
    st.session_state.Vidas = 3

if "Victorias" not in st.session_state:
    st.session_state.Victorias = 0

if "Rondas" not in st.session_state:
    st.session_state.Rondas = 1

if "Rondas_Vidas" not in st.session_state:
    st.session_state.Rondas_Vidas = 10

st.write(f"Vidas: **{mostrar_vidas(st.session_state.Vidas)}**")
st.write(f"🏅Victorias: **{st.session_state.Victorias}**🏅")
st.write(f"🎲Rondas: **{st.session_state.Rondas}**🎲")

if st.session_state.Vidas <= 0:
    st.error("Fin de la partida")
    if st.button("Reiniciar"):
        st.session_state.Vidas = 3
        st.session_state.Victorias = 0
        st.session_state.Rondas = 1
    st.stop()

st.write("Elige una opción:")
st.write("\n")

Jugador = ""

col_piedra, col_papel, col_tijera = st.columns(3)

with col_piedra:
    piedra = st.button("🪨 Piedra 🪨")
    
with col_papel:
    papel = st.button("📋 Papel 📋")
    
with col_tijera:
    tijera = st.button("✂️ Tijera ✂️")

Eleccion = None

if piedra:
    Eleccion = "🪨 Piedra 🪨"

elif papel:
    Eleccion = "📋 Papel 📋"

elif tijera:
    Eleccion = "✂️ Tijera ✂️"

st.write("\n")
    
st.write(f"Has elegido: {Eleccion}")

if Eleccion:
    time.sleep(1)
    st.write("Piedra...")
    time.sleep(1)
    st.write("Papel...")
    time.sleep(1)
    st.write("¡Tijera!")
    time.sleep(1)
    Bot = random.choice(Opciones)
    
    st.write(f"El bot elige: {Bot}")
    
    r = resultado(Eleccion, Bot)
    
    if r == "Empate":
        st.info("¡Empate!")
        st.session_state.Rondas += 1
        if st.session_state.Rondas >= st.session_state.Rondas_Vidas:
            if st.session_state.Vidas < 3:                
                st.session_state.Vidas += 1
            st.session_state.Rondas_Vidas += 10
        
    
    elif r == "Jugador":
        st.info("Ganaste")
        st.session_state.Victorias += 1
        st.session_state.Rondas += 1
        if st.session_state.Rondas >= st.session_state.Rondas_Vidas:
            if st.session_state.Vidas < 3:                
                st.session_state.Vidas += 1
            st.session_state.Rondas_Vidas += 10
    
    else:
        st.info("Derrota...")
        st.session_state.Vidas -= 1
        st.session_state.Rondas += 1
        if st.session_state.Rondas >= st.session_state.Rondas_Vidas:
            if st.session_state.Vidas < 3:                
                st.session_state.Vidas += 1
            st.session_state.Rondas_Vidas += 10
        
    if st.session_state.Vidas <= 0:
        st.session_state.Rondas -= 1
        st.error("Fin de la partida")
        if st.button("Reiniciar"):
            st.session_state.Vidas = 3
            st.session_state.Victorias = 0
            st.session_state.Rondas = 1
            st.session_state.Rondas_Vidas = 10
        
        
    
    


    
    







# Utiliza el comando "python -m streamlit run [ruta_del_fichero.py]" para activar la web