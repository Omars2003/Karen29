import streamlit as st
from PIL import Image
import os
from streamlit.components.v1 import components
st.set_page_config(page_title="Dashboard",page_icon="Imagenes/Logo.png",layout="wide")
st.sidebar.image("Imagenes/Logo.png")
st.sidebar.success("Conoce a detalle nuestros productos.")


with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
st.sidebar.header("Please filter")

page_selection = st.sidebar.radio("", ["Inicio", "Productos", "Contacto"])

# Contenido de la página de inicio
if page_selection == "Inicio":
    st.markdown("<h1 style='text-align: center;'>🍌Plátanos Magar🍌</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Productores-Empacadores-Distribuidores</h3><br>",unsafe_allow_html=True)


#st.sidebar.success("Conoce a detalle nuestros productos.")
# Crear dos columnas, una para el texto y otra para la imagen
    column1, column2 = st.columns([2, 2])  # La relación 2:1 indica que la primera columna ocupará el doble de espacio que la segunda

# Contenido de la primera columna (texto)
    with column1:
       

# Título con tamaño de letra grande, tipo de letra personalizado y color
       st.markdown("<h1 style='font-size: 36px; font-family: Arial, sans-serif; color: black;'>“Plátanos Magar FrutasMex ¡Sabor que brilla, calidad que encanta!”</h1>", unsafe_allow_html=True)

       st.markdown("")
       st.markdown(
        """
        <div style='font-size: 24px;'>
         Empresa mexicana que produce, selecciona, empaca y comercializa platanos de alta  calidad. 
        nuestra empresa se ha convertido en un referente en la industria de 
        la agricultura y la fruta tropical. Nos enorgullecemos de ofrecer una gran variedad de plátanos frescos, sabrosos y saludables
        que<strong> satisfacen los gustos de nuestros clientes en todo el mundo.</strong>
        </div>

        """,
        
       unsafe_allow_html=True
    )

# Contenido de la segunda columna (imagen)
    with column2:
         image = Image.open('Imagenes/fondo2.jpg')
         #nuevo_ancho = 200  # Cambia el ancho deseado
         #nuevo_alto = 200   # Cambia el alto deseado
         #image = image.resize((nuevo_ancho, nuevo_alto))
         #image.save('Imagenes/platanos1_redimensionado.jpeg')
         st.image(image, use_column_width=True)
         #st.image(image, caption='Sunrise by the mountains')
         st.markdown("")
         st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

#--------------------------------------------------------------------------------------------------------------------------------------------------------  
# 
# 
# 
    column1, column2 = st.columns([3.5, 1.5]) 
    with column2: #inverti las comlumnas
        st.markdown("<h1 style='text-align: center;'>🍌</h1>", unsafe_allow_html=True)

        st.markdown(
             
           """
           <div style='font-size: 24px; font-family: Arial;'>  
           

           <strong>Empleamos tecnología puntera para producir la fruta más exquisita.</strong>
             Nuestro proceso de empaque garantiza la seguridad alimentaria. Cumplimos con los estándares de calidad más altos, exportando solo la mejor fruta. 
           <strong>Todos nuestros productos se cultivan, seleccionan y empacan bajo estrictas normas de calidad y seguridad</strong>, utilizando tecnología avanzada.
           
           <br><br>
           </div>
           
           """,unsafe_allow_html=True
           )  
    with column1:
        image = Image.open('Imagenes/fondo6.jpg')
        st.image(image, use_column_width=True)




    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Platano datil (dominico)")
        st.write("")
        st.write("")
        st.write("")
        st.image("Imagenes/dominico2.jpg")

    with col2:
        st.header("Platanos, bananos para nacional y exportación")
        st.image("Imagenes/platanos3.jpeg")

    with col3:
        st.header("Platanos machos para nacional y exportación")
        st.image("Imagenes/machos1.jpeg")



    st.markdown("DONDE NOS UBICAMOS")
    st.markdown("")
    st.markdown("<h2 style='text-align: center;'>Contacto 📞</h2>",unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'><strong>Para mejor atención contactanos a traves de nuestras redes sociales</strong></h4>",unsafe_allow_html=True)
    st.markdown("")
  
    

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("   :red[LinkedIn]", "https://streamlit.io/gallery")

        
   



    with col2:
        st.link_button("   :blue[Facebook]", "https://streamlit.io/gallery")

    with col3:
        st.link_button("   :red[LinkedIn]", "https://streamlit.io/gallery")

    











elif page_selection == "Productos":
    st.title("Página de Productos")
    st.write("Aquí puedes encontrar información sobre nuestros producto")

    agree = st.checkbox('I agree')

    if agree:
     st.write('Great!')
    

# Contenido de la página de contacto
elif page_selection == "Contacto":
    st.title("Página de Contacto")
    st.write("Para contactarnos, envía un correo electrónico a contacto@frutasmex.com.")
    st.button("Go to gallery", "https://streamlit.io/gallery")

    

    

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Bananos Racimo Completo")
        st.image("https://static.streamlit.io/examples/cat.jpg")
        

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    

    






