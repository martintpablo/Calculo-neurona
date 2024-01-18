import streamlit as st

# st.image('https://img.freepik.com/vector-gratis/diagrama-celula-vastago-fondo-blanco_1308-15286.jpg', width=400)

st.title('**¡Hola neurona!**')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

# Tab1
with tab1:
    st.header("Una neurona con una entrada y un peso")
    w0 = st.slider('Peso', 0.0, 5.0, key="w0")
    x0 = st.number_input('Introduzca el valor de la entrada', step=0.1, key="x0")
    if st.button('Calcular la salida', key="b1"):
        y0 = w0 * x0
        st.text(f"La salida de la neurona es {y0}")

# Tab2
with tab2:
    c1, c2 = st.columns(2)
    w1 = c1.slider('Peso w₀', 0.0, 5.0, key="w1")
    x1 = c1.number_input('X₀', step=0.1, key="x1")
    w2 = c2.slider('Peso w₁', 0.0, 5.0, key="w2")
    x2 = c2.number_input('X₁', step=0.1, key="x2")
    if st.button('Calcular la salida', key="b2"):
        y1 = (x1 * w1) + (x2 * w2)
        st.text(f"La salida de la neurona es {y1}")

# Tab3
with tab3:
    c3, c4, c5 = st.columns(3)
    w3 = c3.slider('Peso w₀', 0.0, 5.0, key="w3")
    x3 = c3.number_input('X₀', step=0.1, key="x3")
    w4 = c4.slider('Peso w₁', 0.0, 5.0, key="w4")
    x4 = c4.number_input('X₁', step=0.1, key="x4")
    w5 = c5.slider('Peso w₂', 0.0, 5.0, key="w5")
    x5 = c5.number_input('X₂', step=0.1, key="x5")
    b = st.number_input('Introduzca el valor del sesgo', step=0.1)
    if st.button('Calcular la salida', key="b3"):
        y2 = (x3 * w3) + (x4 * w4) + (x5 * w5) + b
        st.text(f"La salida de la neurona es {y2}")
