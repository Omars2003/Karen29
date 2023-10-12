import streamlit as st
from PIL import Image
import os
from streamlit.components.v1 import components
st.set_page_config(page_title="Dashboard",page_icon="Imagenes/Logo.png",layout="wide")
st.sidebar.image("Imagenes/Logo.png")
st.sidebar.success("Bienvenido a nuestro sitio web")
#st.sidebar.header("Paginas")





page_selection = st.sidebar.radio("EXPLORA", ["INICIO", "QUIENES SOMOS"])

# Contenido de la página de inicio
if page_selection == "INICIO":
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
        st.header("Plátano datil (dominico)")
        st.write("")
        st.write("")
        st.write("")
        st.image("Imagenes/dominico2.jpg")

    with col2:
        st.header("Plátanos, bananos para nacional y exportación")
        st.image("Imagenes/platanos3.jpeg")

    with col3:
        st.header("Plátanos machos para nacional y exportación")
        st.image("Imagenes/machos1.jpeg")



    st.markdown("<h1 style='text-align: center;'>🌏</h1>", unsafe_allow_html=True)
    st.markdown("""
                <div style='font-size: 24px; font-family: Arial;'>  
                Nuestros huertos estan ubicados en el corazón de la producción de plátanos, Chiapas y Tabasco, 
                las características inigualables de estas regiones nos permiten ofrecer plátanos de alta
                calidad durante todo el año. ¡Disfruta del sabor excepcional que solo estas regiones
                inigualables pueden ofrecer! 
                  <br><br>
                 </div>
                
                """,unsafe_allow_html=True
                ) 
    st.markdown("<h2 style='text-align: center;'>Contacto 📞</h2>",unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'><strong>Para mejor atención contáctanos a través de nuestras redes sociales </strong></h4>",unsafe_allow_html=True)
    st.markdown("")
  
    

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button(":red[LinkedIn]", "https://www.linkedin.com/company/98972830/admin/feed/posts/")
    with col2:
        st.link_button(":blue[Facebook]", "https://www.facebook.com/Magar.frutasmex.limited")
    with col3:
        #st.link_button(":red[Whats app]", "https://streamlit.io/gallery")
        imagen = "Imagenes/whats.jpeg"

# Muestra la imagen con un ancho específico
        st.image(imagen,width=200)
#------------------------------------------------------------------------------------------------------------------------
elif page_selection == "QUIENES SOMOS":

    st.title("Quienes Somos 🤗🌴")
    st.markdown("""
           <div style='font-size: 24px; font-family: Arial;'>  
                Es un placer para nosotros presentar nuestra empresa,somos
                 una empresa ubicada en la Ciudad de México dedicada a la comercialización 
                de Plátanos, Bananos, Bananas y derivados con certificados para exportar."
             <br><br>
           </div>
           
           """,unsafe_allow_html=True
           )
    st.markdown("""<div style='font-size: 24px; font-family: Arial;'>
                 <strong>🌏Misión:</strong> Ser un producto de calidad que 
                guste a todos los que lo consuman, ofreciendo un servicio
                 único en todo momento.</div>""",unsafe_allow_html=True)
    
    st.markdown("""<div style='font-size: 24px; font-family: Arial;'>
                <strong>🌏Visión:</strong> Posicionarnos como una marca en un mercado competitivo 
                que se ajusta a las necesidades del mercado.</div><br><br>""",unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(':red[Contacto]')
        st.markdown("""<div style='font-size: 24px; font-family: Arial;'>
                    Comercialización<br>Omar Martínez<br>
                    omar.paps3012003@gmail.com</div>""",unsafe_allow_html=True)
        st.link_button(":blue[Facebook]", "https://www.facebook.com/Magar.frutasmex.limited")
        st.link_button(":black[LinkedIn]", "https://www.linkedin.com/company/98972830/admin/feed/posts/")
        imagen = "Imagenes/whats.jpeg"

# Muestra la imagen con un ancho específico
        st.image(imagen,width=200)
        st.markdown("")
        st.markdown("")
    with col2:
        st.image("Imagenes/fondo3.jpg")
    
    col4, col5, col6 = st.columns(3)


    with col4:
   
     st.image("Imagenes/banana1.jpg")

    with col5:
   
     
     st.image("Imagenes/penca.jpg")

    with col6:
   
     st.image("Imagenes/cajas1.jpg")
        
    


# Contenido de la página de contacto
 #elif page_selection == "Contacto":
  ## st.write("Para contactarnos, envía un correo electrónico a contacto@frutasmex.com.")
 #   st.button("Go to gallery", "https://streamlit.io/gallery")
#
    